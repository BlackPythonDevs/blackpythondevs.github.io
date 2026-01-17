---
title: I reran the test suite with verbose logging to investigate the failures. Most of the failures are test-related issues introduced during the migration from Jekyll to Render Engine .
state: open
state_reason: null
synced_at: 2026-01-07T18:48:39.095509Z
info:
  author: kjaymiller
  created_at: 2026-01-04T19:30:42Z
  updated_at: 2026-01-04T19:30:42Z
---

I reran the test suite with verbose logging to investigate the failures. Most of the failures are test-related issues introduced during the migration from Jekyll to Render Engine .

Test fixed:

- Updated the email link selector from email to contact@blackpythondevs.com
- Fixed the blog description test to match the actual HTML structure (article elements instead of p.post-description
- Corrected title format expectations to match actual output ('Page | Black Python Devs' instead of 'Black Python Devs | Page')

Remaining issues:

- Blog post URL generation tests still assume filename-based URLs (e.g. /blog/2024-05-25-filename.html), while the Render Engine generates title-based slugs (e.g. /blog/title-based-slug.html) -> 29 failing tests
- Missing language attribute: pages currently render lang="" instead of lang="en"
- I still need to verify whether there are any accessibility issues beyond test assumptions

Let me know how you'd like to proceed on the remaining items.

_Originally posted by @danielcristho in https://github.com/BlackPythonDevs/blackpythondevs.github.io/issues/782#issuecomment-3707405095_
