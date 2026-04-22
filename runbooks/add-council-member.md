# Add a BPD Council Member

Adding a Council member requires three coordinated changes: data, image asset,
and an announcement post.

**Reference PRs:** #853 (Ariane), #851 (Edmond), #849 (Israel)

## Recommended: use the script

`scripts/add_council_member.py` automates all three steps:

```bash
uv run python scripts/add_council_member.py \
    --name "First Last" \
    --image /path/to/photo.webp \
    --bio "Their bio text here..." \
    --linkedin "https://linkedin.com/in/..." \
    --date 2026-04-20
```

The script:

1. Adds the name to the `Council` list in `_data/leadership.json`.
2. Copies/converts the image to `assets/images/<slug>-council.webp` (requires
   `magick` / ImageMagick if the source is not already `.webp`).
3. Creates `_posts/YYYY-MM-DD-<slug>-added-to-bpd-council.md`.

Review the generated diff, add a banner image if desired (see below), then
`just pre-commit` / `just test` / open a PR.

## Manual fallback

If you can't run the script:

1. **Leadership data** — Edit `_data/leadership.json` and append to the
   `Council` array. Required fields: `name`, `image`, `alt`, `title` (use
   `"Council"` unless the person has a specific role). Optional: `linkedin`.
2. **Image** — Add `assets/images/<slug>-council.webp`. 512×512 square works
   well. Convert non-webp sources with `magick input.png output.webp`.
3. **(Optional) banner image** — Some announcements include a wider social
   banner at `assets/images/banner_<firstname>.webp` (see PR #853, #852).
4. **Post** — Create `_posts/YYYY-MM-DD-<slug>-added-to-bpd-council.md` with
   frontmatter matching existing council posts. Reference one of the recent
   ones like `2026-02-13-edmond-makolle-added-to-bpd-council.md` for the
   exact shape.

## Checks

- `just pre-commit`
- `just test` — the author list check in `scripts/check_author_list.py` will
  fail if the new member authors a post but isn't listed in `_data/authors.json`.
  Council members are the _subject_, not the author, so this rarely triggers.
- `just serve` → confirm the About page grid renders the new card.

## PR conventions

- Title: `Add <Name> to BPD Council`
- Link the intake issue for the member in the PR body.
