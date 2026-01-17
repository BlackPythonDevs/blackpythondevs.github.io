---
title: "[Remove] lang reference"
state: open
state_reason: null
synced_at: 2026-01-07T18:48:39.093894Z
info:
  author: kjaymiller
  created_at: 2025-06-26T21:17:45Z
  updated_at: 2025-06-26T21:17:45Z
---

Multiple languages were removed... this should be removed.

The condition comparing 'lang' to itself is always true; consider comparing the loop variable to the current page language (e.g. {% if page.lang == lang %}).

_Originally posted by @Copilot in https://github.com/BlackPythonDevs/blackpythondevs.github.io/pull/717#discussion_r2169998101_
