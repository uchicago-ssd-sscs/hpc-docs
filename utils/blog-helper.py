#!/usr/bin/env python3
"""
SSCS Blog Post Generator
Creates a new blog post with correct frontmatter and filename
"""

import os
import re
from datetime import date

CATEGORIES = ["Infrastructure", "Software", "Maintenance", "General"]


def slugify(title):
    return re.sub(r"[-\s]+", "-", re.sub(r"[^\w\s-]", "", title.lower())).strip("-")


def select_category():
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    while True:
        choice = input("Select category (number): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("Invalid choice, try again...")


def find_project_root():
    """Walk up from script location to find mkdocs.yml (project root)"""
    current = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.exists(os.path.join(current, "mkdocs.yml")):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            raise FileNotFoundError(
                "Could not find mkdocs.yml in any parent directory."
            )
        current = parent


def find_posts_dir(project_root):
    """Search for the blog posts directory under the project root"""
    for dirpath, dirnames, _ in os.walk(project_root):
        if os.path.basename(dirpath) == "posts" and "blog" in dirpath:
            return dirpath
    raise FileNotFoundError("Could not find a 'posts' directory under a 'blog' folder.")


def main():
    print("=== SSCS Blog Post Generator ===\n")

    project_root = find_project_root()
    POSTS_DIR = find_posts_dir(project_root)

    title = input("Post title: ").strip()
    excerpt = input("Excerpt (1-2 sentences shown on index): ").strip()
    category = select_category()

    today = date.today().isoformat()
    slug = slugify(title)
    filename = f"{today}-{slug}.md"
    filepath = os.path.join(POSTS_DIR, filename)

    os.makedirs(POSTS_DIR, exist_ok=True)

    content = f"""---
date: {today}
categories:
- {category}
---

# {title}

{excerpt}

<!-- more -->

_Add full content here._
"""

    with open(filepath, "w") as f:
        f.write(content)

    print(f"\nPost created: {filepath}")
    print("Open the file and replace '_Add full content here._' with your content.")


if __name__ == "__main__":
    main()
