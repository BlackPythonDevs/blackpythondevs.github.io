# Add a Partner

Partners are organizations that offer discounts or benefits to the Black Python
Devs community (course discounts, promo codes, etc.). They render in the
Partnerships grid on the Support page from `_data/partnerships.json`.

**Reference PRs:** #845 (partnerships fix); see also `_posts/2024-08-16-talkpython-training-partnership.md`

## Inputs you need

- Partner name
- Logo file (prefer `.webp`; `.png` acceptable for legacy assets)
- Landing page / offer URL
- Promo code (if the partner provides one)
- Offer description / blurb (the discount and the donation split, if any)

## Data shape

`_data/partnerships.json` is a flat list of objects. Each partner has:

```json
{
  "name": "TalkPython Training",
  "promo_code": "bpd-20pc-1c1da",
  "description": "Use the <a href=\"https://...\">landing page</a> or promo code <strong>bpd-20pc-1c1da</strong> at checkout for a discount. A portion is donated to Black Python Devs.",
  "url": "https://training.talkpython.fm/black-python-devs",
  "logo": "/assets/images/talkpython.webp"
}
```

- `description` may contain inline HTML — it is rendered unescaped in the grid.
- `logo` is a site-root path; a leading `/` is preferred (e.g.
  `/assets/images/<partner>.webp`).

## Steps

1. **Get the logo asset**

   - Drop the raw logo in `tmp/` (git-ignored staging area).
   - Optimize it into `assets/images/`:
     ```
     just optimize-image tmp/<partner>.png
     ```
     This rewrites it as a webp and removes the original. Move/rename the
     result into `assets/images/<partner>.webp` if needed.
   - Prefer a transparent background so it works with the site theme.

2. **Add the partner to the JSON**

   - Append a new object to the list in `_data/partnerships.json`.
   - Fill in `name`, `promo_code`, `description`, `url`, and `logo`.
   - If the partner has no promo code, set `"promo_code": ""`.
   - Point `logo` at the asset from step 1 (e.g. `/assets/images/<partner>.webp`).

3. **(Optional) Write an announcement post**

   - If the partnership is being announced, create
     `_posts/YYYY-MM-DD-<partner>-partnership.md`.
   - Pattern the frontmatter and body after
     `_posts/2024-08-16-talkpython-training-partnership.md`.

4. **Run checks**

   - `just test` — validates the JSON parses.
   - `just serve` → confirm the logo and blurb render in the Partnerships
     section of the Support page.

5. **Open a PR** titled `Add <Partner> as a partner`. Reference any
   intake/coordination issues that tracked the partnership.

## Gotchas

- `_data/partnerships.json` must stay valid JSON — a trailing comma or an
  unescaped quote inside `description` will break the build. Escape inner
  quotes as `\"`.
- The grid caps logos at `max-height: 80px` with `object-fit: contain`, so
  wide or tall logos are scaled to fit — no per-partner CSS is needed.
- Large PNGs should be converted to `.webp` before committing.
