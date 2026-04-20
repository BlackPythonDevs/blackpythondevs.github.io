# Update Site Navigation

The main nav is driven by the `navigation` list at the top of `app.py`. Header
and footer templates read `site_vars["navigation"]` and render links from it.

**Reference PRs:** #844 (remove BPD Events + Sponsored Events from header),
#840 (remove Community from header), #830 (remove Home), #829 (rename Blog → News),
#832 (combine Events links), #831 (combine Discounts + Support)

## Rename a nav item

1. In `app.py`, edit the `text` field of the matching entry in `navigation`.
2. If the rename also changes the URL (e.g. `/blog/` → `/news/`), update `url`
   too and add a redirect for the old path (see `fix-broken-link.md`).
3. Search the codebase for hard-coded references to the old label in footer,
   CONTRIBUTING, and posts — update where user-visible.

## Remove a nav item

1. Delete the entry from `navigation` in `app.py`.
2. Remove any footer/header references to the page (e.g. `_layouts/_includes/footer.html`).
3. If the page still exists and is linked externally, leave the page file but
   remove it from nav. If the page itself is being retired, add a redirect
   (see `fix-broken-link.md`).
4. Update tests in `tests/test.py` that asserted the old nav entry existed.

## Add a nav item

1. Append a new object to `navigation`:
   ```python
   {"text": "<Label>", "url": "/<path>.html", "icon": "iconoir-<name>"}
   ```
2. Icons come from the Iconoir set — pick one consistent with the existing
   entries.
3. Ensure the target URL resolves in the built site.

## Combine pages

Pattern used for Events (#832) and Support (#831):

1. Decide the canonical destination page.
2. Move the content from the sibling page into it.
3. Remove the sibling `@app.page` class from `app.py`.
4. Add a redirect stub for the retired URL.
5. Update the `navigation` list so there's a single entry.

## Checks

- `just build` — verify the nav renders in the generated output.
- `just test` — update/add assertions about the nav.
- `just serve` — click every nav entry and confirm none 404.
