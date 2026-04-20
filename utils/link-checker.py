#!/usr/bin/env python3
"""
SSCS Link Checker
Scans all markdown files in the docs/ directory and reports broken internal
and external links, with warnings for redirects.

Resolution strategy:
- File links (.md, .png, .jpg, etc.) are resolved relative to the SOURCE FILE's directory
- Page links (no extension, directory-style) are resolved relative to the PAGE URL directory
  mimicking MkDocs' URL-based resolution behavior
"""

import posixpath
import re
import sys
from pathlib import Path

import requests

# ─── ANSI Colors ─────────────────────────────────────────────
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ─── Config ──────────────────────────────────────────────────
REQUEST_TIMEOUT = 10
HEADERS = {"User-Agent": "SSCS-LinkChecker/1.0"}


def find_project_root():
    """
    Walk up the directory tree from the script's location to find
    the project root, identified by the presence of mkdocs.yml
    """
    current = Path(__file__).resolve().parent
    while True:
        if (current / "mkdocs.yml").exists():
            return current
        parent = current.parent
        if parent == current:
            raise FileNotFoundError(
                "Could not find mkdocs.yml in any parent directory."
            )
        current = parent


def find_docs_dir(project_root):
    """Locate the docs/ directory under the project root."""
    docs_dir = project_root / "docs"
    if docs_dir.exists():
        return docs_dir
    raise FileNotFoundError(
        "Could not find a 'docs/' directory under the project root."
    )


def extract_links(content):
    """
    Extract all markdown links and image references from content.
    Handles both regular links [text](url) and images ![text](url).
    Returns list of (full_match, text, url) tuples.
    """
    return re.findall(r"!?(\[([^\]]*)\]\(([^)]+)\))", content)


def get_all_md_files(docs_dir):
    """Recursively find all markdown files under docs/."""
    return list(docs_dir.rglob("*.md"))


def get_all_docs_files(docs_dir):
    """Recursively find all files under docs/ (for static asset resolution)."""
    return [p for p in docs_dir.rglob("*") if p.is_file()]


def md_file_to_page_url(md_file, docs_dir):
    """
    Convert a markdown file path to its MkDocs rendered page URL (directory-style).

    MkDocs renders pages as directory URLs by default, e.g.:
      docs/index.md                -> ""  (site root)
      docs/jobs/overview.md        -> "jobs/overview/"
      docs/jobs/index.md           -> "jobs/"
    """
    rel = md_file.relative_to(docs_dir).as_posix()

    if rel == "index.md":
        return ""
    if rel.endswith("/index.md"):
        return rel[: -len("index.md")]
    if rel.endswith(".md"):
        return rel[:-3] + "/"
    return rel


def build_indexes(docs_dir, md_files):
    """
    Build lookup sets used during link resolution:
    - md_rel_paths   : relative paths of all .md files (e.g. "jobs/overview.md")
    - page_urls      : MkDocs page URLs for all .md files (e.g. "jobs/overview/")
    - static_rel_paths: relative paths of ALL files under docs/ (for image/asset checks)
    """
    md_rel_paths = set()
    page_urls = set()
    static_rel_paths = set()

    for md_file in md_files:
        md_rel_paths.add(md_file.relative_to(docs_dir).as_posix())
        page_urls.add(md_file_to_page_url(md_file, docs_dir))

    for f in get_all_docs_files(docs_dir):
        static_rel_paths.add(f.relative_to(docs_dir).as_posix())

    return md_rel_paths, page_urls, static_rel_paths


def normalize_posix_path(path_str):
    """
    Normalize a POSIX path, collapsing ../ and ./ segments.
    Returns empty string instead of "." for the current directory.
    """
    normalized = posixpath.normpath(path_str)
    return "" if normalized == "." else normalized


def resolve_internal_link(
    link, source_file, docs_dir, md_rel_paths, page_urls, static_rel_paths
):
    """
    Resolve an internal link and check whether its target exists.

    Two resolution strategies are used depending on link type:

    1. FILE LINKS (.md, .png, .jpg, .svg, .pdf, etc.)
       Resolved relative to the SOURCE FILE's directory on disk.
       This matches how browsers and editors resolve relative file paths.
       Example: from docs/jobs/overview.md, "../assets/img.png" -> docs/assets/img.png

    2. PAGE LINKS (no extension, or trailing slash)
       Resolved relative to the PAGE URL directory, mimicking MkDocs' URL routing.
       MkDocs renders pages as directories, so "jobs/overview.md" becomes "jobs/overview/".
       Example: from jobs/overview/ (page URL), "../submitting-jobs/" -> jobs/submitting-jobs/

    In both cases, leading "./" segments are stripped first since MkDocs treats
    "./" as a no-op — i.e., "./../foo" behaves the same as "../foo".
    """
    # Strip the anchor fragment (#section) — we only check the file/page target
    link_no_anchor = link.split("#", 1)[0].strip()

    # Anchor-only links (e.g. "#section") are always valid — they refer to the current page
    if not link_no_anchor:
        return True, "Anchor-only link"

    # Strip leading ./ segments — MkDocs treats ./ as a no-op per path segment
    # e.g. ./../foo -> ../foo, ./../../foo -> ../../foo
    path = link_no_anchor
    while path.startswith("./"):
        path = path[2:]

    # Strip trailing slash for uniform processing
    path = path.rstrip("/")

    # Determine if this is a file link (has extension) or a page link (no extension)
    suffix = Path(path).suffix.lower()
    is_file_link = suffix != ""

    if is_file_link:
        # ── File links (.md, .png, etc.) ─────────────────────────────────────
        # Resolve relative to the SOURCE FILE's directory
        source_rel_dir = source_file.relative_to(docs_dir).parent.as_posix()
        combined = posixpath.join(source_rel_dir, path)
        resolved = normalize_posix_path(combined)

        # Reject paths that escape the docs/ root
        if resolved.startswith("../") or resolved == "..":
            return False, "Resolved outside docs/"

        # Check against known markdown files and static assets
        if resolved in static_rel_paths or resolved in md_rel_paths:
            return True, f"File exists: {resolved}"
        return False, f"Could not resolve file: {resolved}"

    else:
        # ── Page links (no extension / directory-style) ───────────────────────
        # Resolve relative to the PAGE URL directory (MkDocs URL routing)
        source_page_url = md_file_to_page_url(source_file, docs_dir)

        # Important: use dirname WITHOUT rstrip so that the trailing slash is preserved.
        # e.g. "jobs/common-workflows/" -> dirname = "jobs/common-workflows"
        # This means ../ correctly navigates up to "jobs/", matching MkDocs behavior.
        source_page_dir = posixpath.dirname(source_page_url)

        combined = posixpath.join(source_page_dir, path)
        resolved = normalize_posix_path(combined)

        # Reject paths that escape the docs/ root
        if resolved.startswith("../") or resolved == "..":
            return False, "Resolved outside docs/"

        # Check all plausible variants of the resolved path
        candidates = [
            resolved + "/",  # directory-style page URL
            resolved,  # exact match
            resolved + ".md",  # markdown source file
            resolved + "/index.md",  # section index
        ]

        for cand in candidates:
            if cand in page_urls or cand in md_rel_paths:
                return True, f"Page exists: {cand}"

        return False, f"Could not resolve page: {resolved}"


def check_external_link(url):
    """
    Perform an HTTP GET request to check if an external URL is reachable.

    Returns a (status, message) tuple where status is one of:
    - 'ok'       : URL is reachable and returns 200 with no redirects
    - 'redirect' : URL is reachable but redirects to a different URL (3xx)
    - 'broken'   : URL returns a non-200 HTTP status code
    - 'error'    : Request failed due to network error, timeout, etc.
    """
    try:
        response = requests.get(
            url,
            timeout=REQUEST_TIMEOUT,
            headers=HEADERS,
            allow_redirects=True,
        )
        if response.status_code == 200:
            if response.history:
                return (
                    "redirect",
                    f"Redirects to {response.url} [{response.status_code}]",
                )
            return "ok", f"{response.status_code}"
        return "broken", f"HTTP {response.status_code}"
    except requests.exceptions.ConnectionError:
        return "error", "Connection error"
    except requests.exceptions.Timeout:
        return "error", "Timed out"
    except requests.exceptions.RequestException as e:
        return "error", str(e)


def print_summary(results):
    """Print a color-coded summary report of all link check results."""
    total_links = results["total_links"]
    broken = results["broken"]
    redirects = results["redirects"]
    errors = results["errors"]
    ok_count = total_links - len(broken) - len(redirects) - len(errors)

    print(f"\n{'─' * 60}")
    print(f"{BOLD}Link Check Summary{RESET}")
    print(f"{'─' * 60}")
    print(f"  Files scanned  : {results['total_files']}")
    print(f"  Links checked  : {total_links}")
    print(f"  {GREEN}OK{RESET}           : {ok_count}")
    print(f"  {YELLOW}Redirects{RESET}    : {len(redirects)}")
    print(f"  {RED}Broken{RESET}        : {len(broken)}")
    print(f"  {RED}Errors{RESET}        : {len(errors)}")
    print(f"{'─' * 60}")

    if redirects:
        print(f"\n{YELLOW}{BOLD}Redirects:{RESET}")
        for r in redirects:
            print(f"  [EXTERNAL] {CYAN}{r['file']}{RESET}")
            print(f"    Text : {r['text']}")
            print(f"    Link : {r['url']}")
            print(f"    Info : {r['message']}\n")

    if broken or errors:
        print(f"\n{RED}{BOLD}Broken / Errors:{RESET}")
        for b in broken + errors:
            print(f"  [{b['type'].upper()}] {CYAN}{b['file']}{RESET}")
            print(f"    Text : {b['text']}")
            print(f"    Link : {b['url']}")
            print(f"    Info : {b['message']}\n")

    if not broken and not errors:
        print(f"\n{GREEN}{BOLD}All links are valid!{RESET}\n")


def main():
    print(f"\n{BOLD}=== SSCS Link Checker ==={RESET}\n")

    project_root = find_project_root()
    docs_dir = find_docs_dir(project_root)
    md_files = get_all_md_files(docs_dir)
    md_rel_paths, page_urls, static_rel_paths = build_indexes(docs_dir, md_files)

    results = {
        "total_files": len(md_files),
        "total_links": 0,
        "broken": [],
        "redirects": [],
        "errors": [],
    }

    for md_file in md_files:
        relative_file = md_file.relative_to(project_root)
        content = md_file.read_text(encoding="utf-8")
        raw_links = extract_links(content)
        links = [(text, url) for _, text, url in raw_links]

        if not links:
            continue

        print(f"  Scanning: {CYAN}{relative_file}{RESET} ({len(links)} links)")

        for text, url in links:
            results["total_links"] += 1
            url = url.strip()

            # ── External links ────────────────────────────────────────────────
            if url.startswith("http://") or url.startswith("https://"):
                status, message = check_external_link(url)
                if status == "redirect":
                    results["redirects"].append(
                        {
                            "type": "external",
                            "file": str(relative_file),
                            "text": text,
                            "url": url,
                            "message": message,
                        }
                    )
                elif status in ("broken", "error"):
                    results["errors" if status == "error" else "broken"].append(
                        {
                            "type": "external",
                            "file": str(relative_file),
                            "text": text,
                            "url": url,
                            "message": message,
                        }
                    )

            # ── Skip special schemes and pure anchor links ────────────────────
            elif (
                url.startswith("mailto:")
                or url.startswith("tel:")
                or url.startswith("javascript:")
                or url.startswith("#")
            ):
                continue

            # ── Internal links ────────────────────────────────────────────────
            else:
                is_valid, message = resolve_internal_link(
                    url, md_file, docs_dir, md_rel_paths, page_urls, static_rel_paths
                )
                if not is_valid:
                    results["broken"].append(
                        {
                            "type": "internal",
                            "file": str(relative_file),
                            "text": text,
                            "url": url,
                            "message": message,
                        }
                    )

    print_summary(results)
    # Exit with code 1 if broken links found — useful for CI/CD integration
    sys.exit(1 if results["broken"] or results["errors"] else 0)


if __name__ == "__main__":
    main()
