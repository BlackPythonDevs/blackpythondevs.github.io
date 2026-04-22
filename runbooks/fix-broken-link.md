# Fix a Broken Link or 404

Broken links break search rankings and trust. The recent fixes followed one
of two patterns: update the link in the template, or create a redirect stub.

**Reference PRs:** #892 (partnerships 404), #890 (community 404), #856
(broken events links)

## Triage

1. Reproduce the 404. Note the exact URL.
2. Decide:
   - **Link is wrong** → fix the href in the template.
   - **Old URL is indexed / linked externally** → create a redirect stub so
     existing links keep working.

## Pattern A — fix the link in the template

1. Grep for the broken URL:
   ```bash
   rg "old-url" _layouts/ *.html pages/ _posts/
   ```
2. Update the `href` to the correct target.
3. If the link was in `_layouts/_includes/footer.html` or `header.html`, also
   check that nav items in `app.py` still agree.
4. Add a test in `tests/test.py` asserting the new path returns the right
   status (the existing tests use render-engine's build output — mirror them).

## Pattern B — add a redirect stub

Used when an old top-level page (e.g. `community.html`, `partnerships.html`)
was merged into another page but external links still hit the old URL.

1. Create an HTML file at the old path (e.g. `community.html`) at the repo root.
   Use a meta refresh or a short script; see the existing `community.html` and
   `partnerships.html` for the exact shape.
2. Register the page in `app.py`:
   ```python
   @app.page
   class Community(Page):
       content_path = "community.html"
   ```
3. Add the old→new mapping to `redirects.json` so the pattern stays documented.
4. Update any internal links (footer, header, CONTRIBUTING) to point at the
   new canonical URL rather than the redirect.
5. Extend `tests/test.py` to assert the redirect page exists in the build output.

## Checks

- `just build` and inspect `output/` to confirm the page/redirect is there.
- `just test` for the new assertion.
- Click through the link in `just serve`.

## PR title

`Fix <page>.html 404 with redirect` or `Fix broken <area> links`.
