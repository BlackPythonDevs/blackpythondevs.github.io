---
title: Update unless tag
state: open
state_reason: null
synced_at: 2026-01-07T18:48:39.09374Z
info:
  author: kjaymiller
  created_at: 2025-06-26T21:16:31Z
  updated_at: 2025-06-26T21:16:31Z
---

Currently not breaking anything (maybe a11y)

The condition in the 'unless' tag is malformed; it likely should be written as {% unless entry.platform == "rss" %}.

```suggestion
  <a {% unless entry.platform == "rss" %}rel="me" {% endunless %}href="{{ entry.user_url }}" target="_blank" title="{{ entry.title | default: entry.platform }}">
```

_Originally posted by @Copilot in https://github.com/BlackPythonDevs/blackpythondevs.github.io/pull/717#discussion_r2169998093_
