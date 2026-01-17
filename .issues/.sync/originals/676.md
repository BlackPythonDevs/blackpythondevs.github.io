---
title: Migrate Site to Render Engine
milestone: PyCon Sprints 2025
state: open
state_reason: null
synced_at: 2026-01-07T18:48:39.091319Z
info:
  author: kjaymiller
  created_at: 2025-05-18T04:13:49Z
  updated_at: 2025-05-18T21:31:47Z
---

We've been looking about making this change for some time.

It would be great to simplify the codebase by moving the code to one language.

My suggestion is to use [Render-Engine](https://github.com/render-engine/render-engine) (Disclosure I am the maintainer of Render Engine)

## Pros

- Completely removes ruby from build
- Modern SSG built in Python
- Actively encourages developers to support an ecosystem created by a BPD member

## Cons

- Not a popular web framework
