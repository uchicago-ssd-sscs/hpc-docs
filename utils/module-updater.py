#!/usr/bin/env python3
"""
SSCS Module Page Updater
Reads available modules from a .txt file (output of module avail), parses them, and updates a specific section in a markdown file.
"""

import re
import os
from pathlib import Path
from datetime import datetime, timezone

UPDATE_MD = "modules.md"
MODULES_TXT = "modules.txt"
SECTION_START = "<!-- MODULES_START -->"
SECTION_END = "<!-- MODULES_END -->"


def find_project_root():
    """Walk up from script location to find mkdocs.yml"""
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


def find_modules_txt(project_root):
    """Search for modules.txt under the project root"""
    for dirpath, _, filenames in os.walk(project_root):
        if MODULES_TXT in filenames:
            return Path(dirpath) / MODULES_TXT
    raise FileNotFoundError(
        f"Could not find '{MODULES_TXT}' anywhere under project root."
    )


def find_modules_md(project_root):
    """Search for modules.md under docs/software/."""
    for f in (project_root / "docs").rglob(UPDATE_MD):
        if "software" in f.parts:
            return f
    raise FileNotFoundError("Could not find 'modules.md' under docs/software/.")


def parse_modules(txt_path):
    """
    Parse module names and versions from module avail output
    Returns list of (name, version) tuples, sorted by name
    """
    content = txt_path.read_text(encoding="utf-8")
    modules = []

    for line in content.splitlines():
        # Skip header lines and key/legend lines
        if line.startswith("-") or line.startswith("Key:") or not line.strip():
            continue
        if "=module-alias" in line or "(symbolic-version)" in line:
            continue

        # Extract all module/version tokens from the line
        tokens = line.split()
        for token in tokens:
            # Strip annotations like (@), (default)
            token = re.sub(r"\(.*?\)", "", token).strip()
            if not token:
                continue
            if "/" in token:
                name, version = token.split("/", 1)
                modules.append((name.strip(), version.strip()))

    # Sort by module name
    modules.sort(key=lambda x: x[0].lower())
    return modules


def build_markdown_table(modules):
    """
    Build a two-column-pair markdown table with grouped versions
    Format: | Module | Versions | | Module | Versions |
    """
    timestamp = datetime.now(timezone.utc).strftime("%B %d, %Y at %H:%M UTC")

    # Group versions by module name
    grouped = {}
    for name, version in modules:
        grouped.setdefault(name, []).append(version)

    # Sort versions for each module
    for name in grouped:
        grouped[name] = sorted(grouped[name])

    # Convert to list of (name, versions_str) pairs
    entries = [
        (name, "<br>".join(f"`{v}`" for v in versions))
        for name, versions in sorted(grouped.items(), key=lambda x: x[0].lower())
    ]

    # Split into two halves
    mid = (len(entries) + 1) // 2
    left = entries[:mid]
    right = entries[mid:]

    lines = [
        f"**Last updated**: {timestamp}",
        "",
        "| Module | Version(s) | &nbsp; | Module | Version(s) |",
        "|--------|------------|:------:|--------|------------|",
    ]

    for i in range(mid):
        l_name, l_ver = left[i]
        if i < len(right):
            r_name, r_ver = right[i]
            r_name_fmt = f"`{r_name}`"
        else:
            r_name_fmt, r_ver = "", ""
        lines.append(f"| `{l_name}` | {l_ver} | | {r_name_fmt} | {r_ver} |")

    return "\n".join(lines)


def update_markdown_section(md_path, new_content):
    """
    Replace content between MODULES_START and MODULES_END markers
    in the markdown file.
    """
    content = md_path.read_text(encoding="utf-8")

    if SECTION_START not in content or SECTION_END not in content:
        raise ValueError(
            f"Could not find section markers '{SECTION_START}' and '{SECTION_END}' "
            f"in {md_path}.\n"
            f"Please add them to the markdown file where you want the table to appear."
        )

    pattern = re.compile(
        rf"{re.escape(SECTION_START)}.*?{re.escape(SECTION_END)}", re.DOTALL
    )

    replacement = f"{SECTION_START}\n\n{new_content}\n\n{SECTION_END}"
    updated = pattern.sub(replacement, content)
    md_path.write_text(updated, encoding="utf-8")


def main():
    print("=== SSCS Module Page Updater ===\n")

    project_root = find_project_root()
    txt_path = find_modules_txt(project_root)
    md_path = find_modules_md(project_root)

    print(f"  Reading modules from : {txt_path.relative_to(project_root)}")
    print(f"  Updating             : {md_path.relative_to(project_root)}")

    modules = parse_modules(txt_path)
    # Count unique module names
    unique_modules = len(set(name for name, _ in modules))
    print(f"  Modules found        : {unique_modules} ({len(modules)} total versions)")

    table = build_markdown_table(modules)
    update_markdown_section(md_path, table)

    print(f"\nSuccessfully updated modules section in {md_path.name}")


if __name__ == "__main__":
    main()
