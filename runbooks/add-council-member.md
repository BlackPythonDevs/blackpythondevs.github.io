# Add a BPD Council Member

Adding a Council member requires three coordinated changes: data, image asset,
and an announcement post.

**Reference PRs:** #853 (Ariane), #851 (Edmond), #849 (Israel)

## Stage inputs in `tmp/`

`tmp/` is the standard staging area for inputs to people-related runbooks
(council members, foundational supporters, sponsor logos, etc.). It is
git-ignored, so drop the raw bio and photo a maintainer sends you there:

```
tmp/
  ariza-profile.md       # bio copy, draft notes, intake email, etc.
  Valen__Laura-9.jpg     # original photo from the member
```

Nothing under `tmp/` ever gets committed — the script copies the optimized
image into `assets/images/` and writes the bio into `_posts/`.

### Optimize the image first

Photos from members are typically large originals (multi-MB JPEGs). Before
handing one to the script, optimize it down to a 512×512 webp:

```bash
mv tmp/Valen__Laura-9.jpg tmp/laura-council.jpg   # rename to the slug you want
just optimize-image tmp/laura-council.jpg          # rewrites in place -> tmp/laura-council.webp
```

`just optimize-image` wraps ImageMagick (`magick`); install it with
`brew install imagemagick` if missing. It writes a 512×512 webp next to the
source and removes the original. Equivalent one-liner if you prefer:

```bash
magick tmp/laura-council.jpg -resize '512x512^' -gravity center \
    -extent 512x512 -strip -quality 82 tmp/laura-council.webp
```

`cwebp`, `squoosh`, or any other tool is fine — the goal is a square webp
under ~80 KB. Avoid committing the unoptimized original to `assets/images/`.

## Recommended: use the script

`scripts/add_council_member.py` automates all three steps:

```bash
just add-council-member \
    --name "First Last" \
    --image tmp/laura-council.webp \
    --bio-file tmp/laura-profile.md \
    --linkedin "https://linkedin.com/in/..." \
    --date 2026-04-20
```

`--bio-file` reads the bio from disk (recommended — avoids shell-quoting
issues with multiline markdown). Pass `--bio "..."` instead if you'd rather
inline a short string. The two flags are mutually exclusive.

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
