# Add a Corporate Sponsor

Corporate sponsors appear in the Corporate Sponsors grid on the homepage and
get an announcement blog post.

**Reference PRs:** #888 (JetBrains), #866 (Anaconda), #864 (Anaconda announcement)

## Inputs you need

- Sponsor name
- Logo file (prefer `.webp`; `.png` acceptable for legacy assets)
- Sponsorship blurb / announcement text
- A featured banner image for the blog post (1200×630 recommended)

## Steps

1. **Add the logo asset**

   - Place the logo in `assets/images/` — e.g. `assets/images/jetbrains.webp`.
   - Use a transparent background where possible so it works on the site theme.

2. **Add the sponsor to the grid**

   - Edit `_layouts/_includes/sponsors.html`.
   - Under `<h3>Corporate Sponsors</h3>` add a new `<article class="sponsor">`
     with an `<img>` pointing at the new asset. Keep `style="height: 2rem"` to
     match the other logos.

3. **Write the announcement post**

   - Create `_posts/YYYY-MM-DD-<sponsor>-corporate-sponsorship.md`.
   - Frontmatter needs: `author`, `date`, `description`, `featured_image`, `title`.
   - Add the featured image (e.g. `assets/images/corporate-sponsorship-<sponsor>.webp`).
   - Pattern the body after `_posts/2026-04-16-jetbrains-corporate-sponsorship.md`.

4. **Run checks**

   - `just pre-commit`
   - `just test`
   - `just serve` → confirm the logo shows on the homepage and the post renders.

5. **Open a PR** titled `Add <Sponsor> as corporate sponsor`. Reference any
   intake/coordination issues that tracked the sponsorship.

## Gotchas

- Logo height must match the existing `2rem` inline style so the grid doesn't
  jitter. Do not introduce a new CSS class just for one sponsor.
- If you also need to remove a prior sponsor, do it in the same PR so the
  grid stays coherent.
- Large PNGs should be converted to `.webp` before committing.
