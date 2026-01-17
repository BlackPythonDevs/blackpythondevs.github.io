---
title: Add blog posts to snapshot tests
labels:
  - testing
state: open
state_reason: null
synced_at: 2026-01-07T18:48:39.090429Z
info:
  author: kjaymiller
  created_at: 2024-11-06T14:19:48Z
  updated_at: 2024-11-06T14:19:59Z
---

#566 was detected after seeing the changes affected on the blog.

We have #483 which made it easy to view the static pages but blog posts were excluded...

#563 shows how to iterate through the blog. We so we could generate snapshots of blog posts as well. This would help check for issues in blog posts..

#### Why check ALL the blog posts

It's true that checking every blog post may seem excessive. Sadly we've had issues that snuck by us due to metadata being incorrect.
