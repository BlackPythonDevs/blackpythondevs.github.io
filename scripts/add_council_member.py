"""
Script to add a new BPD Council member.

Steps performed:
1. Adds the member's name to the Council list in _data/leadership.json
2. Copies/converts the provided image to assets/images/
3. Creates a blog post announcement in _posts/

Usage:
    python scripts/add_council_member.py \
        --name "First Last" \
        --image /path/to/photo.webp \
        --bio "Their bio text here..." \
        [--linkedin "https://linkedin.com/in/..."] \
        [--date 2026-03-22]
"""

import argparse
import json
import shutil
import subprocess
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEADERSHIP_JSON = ROOT / "_data" / "leadership.json"
POSTS_DIR = ROOT / "_posts"
IMAGES_DIR = ROOT / "assets" / "images"

COUNCIL_BLURB = (
    "The BPD council is the sounding board for decisions that need to be made "
    "in Black Python Devs. They are the advisory group who share how our actions "
    "can impact their communities. The council is made up of organizers, BPD leaders "
    "and those in leadership positions around the Python world."
)


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def copy_image(source: Path, name_slug: str) -> str:
    """Copy the image to assets/images as webp and return the site-relative path."""
    dest_name = f"{name_slug}-council.webp"
    dest = IMAGES_DIR / dest_name

    if source.suffix.lower() == ".webp":
        shutil.copy2(source, dest)
    else:
        subprocess.run(
            ["magick", str(source), str(dest)],
            check=True,
        )

    return f"/assets/images/{dest_name}"


def update_leadership(name: str) -> None:
    """Add the name to the Council list in leadership.json."""
    data = json.loads(LEADERSHIP_JSON.read_text())

    if name in data["Council"]:
        print(f"⚠ {name} is already in the Council list, skipping update.")
        return

    data["Council"].append(name)
    LEADERSHIP_JSON.write_text(json.dumps(data, indent=2) + "\n")
    print(f"✓ Added {name} to leadership.json Council list.")


def create_blog_post(
    name: str,
    bio: str,
    image_path: str,
    linkedin: str | None = None,
    post_date: date | None = None,
) -> Path:
    """Create the announcement blog post."""
    post_date = post_date or date.today()
    name_slug = slugify(name)
    filename = f"{post_date.isoformat()}-{name_slug}-added-to-bpd-council.md"
    filepath = POSTS_DIR / filename

    # Build the name link
    if linkedin:
        name_link = f"[{name}]({linkedin})"
    else:
        name_link = name

    first_name = name.split()[0]

    content = f"""---
author:
  - Jay Miller
date: {post_date.isoformat()}
description: The BPD Council has recognized the work of {name} and invited
  them to join the Council.
featured_image: {image_path}
title: {name} Added to BPD Council
---

Congratulations to {name_link} for recognition and consideration for the BPD Council!

{bio}

{COUNCIL_BLURB}

Congratulations again to {first_name}!
"""

    filepath.write_text(content)
    print(f"✓ Created blog post: {filepath.relative_to(ROOT)}")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Add a new member to the BPD Council")
    parser.add_argument(
        "--name", required=True, help="Full name of the new council member"
    )
    parser.add_argument("--image", required=True, help="Path to the member's photo")
    parser.add_argument(
        "--bio", required=True, help="Bio paragraph(s) for the blog post"
    )
    parser.add_argument(
        "--linkedin", default=None, help="LinkedIn profile URL (optional)"
    )
    parser.add_argument(
        "--date",
        default=None,
        help="Post date in YYYY-MM-DD format (defaults to today)",
    )
    args = parser.parse_args()

    post_date = date.fromisoformat(args.date) if args.date else date.today()
    image_source = Path(args.image).expanduser().resolve()

    if not image_source.exists():
        parser.error(f"Image file not found: {image_source}")

    name_slug = slugify(args.name)

    # 1. Copy image
    image_path = copy_image(image_source, name_slug)
    print(f"✓ Image saved to {image_path}")

    # 2. Update leadership.json
    update_leadership(args.name)

    # 3. Create blog post
    create_blog_post(
        name=args.name,
        bio=args.bio,
        image_path=image_path,
        linkedin=args.linkedin,
        post_date=post_date,
    )

    print("\nDone! Review the changes and commit when ready.")


if __name__ == "__main__":
    main()
