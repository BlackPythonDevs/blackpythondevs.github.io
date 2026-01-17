---
title: I've reverted it back to 2025. I just realized that the year should be updated via app.py (where it's set dynamically), not hardcoded in footer.html.
state: closed
state_reason: COMPLETED
synced_at: 2026-01-09T15:22:57.570796Z
info:
  author: kjaymiller
  created_at: 2026-01-04T19:28:19Z
  updated_at: 2026-01-09T14:41:59Z
---

I've reverted it back to 2025. I just realized that the year should be updated via app.py (where it's set dynamically), not hardcoded in footer.html.

I think we should use the `{{ year }}` variable instead:

`<small>&copy; 2025 Black Python Devs</small>` -> `<small>&copy; {{ year }} Black Python Devs</small>`

I'll open a separate issue to address this.

_Originally posted by @danielcristho in https://github.com/BlackPythonDevs/blackpythondevs.github.io/pull/782#discussion_r2659148678_
