# Publish a Blog Post / Announcement

Blog posts live in `_posts/` and are rendered under `/news/` (formerly `/blog/`).

**Reference PRs:** #888 (sponsor announcement), #864 (Anaconda announcement),
plus all council-member posts.

## Filename

`_posts/YYYY-MM-DD-<kebab-case-slug>.md`

The date must be correct — render-engine uses it for ordering and feed dates.

## Frontmatter

Minimum fields, based on recent posts:

```markdown
---
author:
  - Jay Miller
date: 2026-04-16
description: One-line summary used for SEO and the post list preview.
featured_image: /assets/images/<post-image>.webp
title: Human-readable post title
---
```

- `author` is a list; each entry must match a `name` in `_data/authors.json`.
  If the author isn't there yet, add them (see "Adding an author" below).
- `featured_image` is optional but recommended for share previews.
- Do **not** include `layout:` — the default post layout is applied automatically.

## Adding an author

Edit `_data/authors.json` and append an object with at least `name` and `bio`.
Add `bpd_role` and `social` links if known. `scripts/check_author_list.py`
runs under `just test` and will fail the build if a post references an
unknown author.

## Body

Standard Markdown. Images referenced in the body go in `assets/images/` and
are linked with absolute paths (e.g. `![alt](/assets/images/foo.webp)`).

## Checks

- `just pre-commit` — runs frontmatter and formatting checks.
- `just test` — includes the author-list check.
- `just serve` — confirm the post shows on `/news/` and its featured image renders.

## PR title

Short and descriptive, e.g. `Add JetBrains corporate sponsorship post` or
`Publish 2024 recap`.
