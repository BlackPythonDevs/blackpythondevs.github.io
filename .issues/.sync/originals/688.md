---
title: Add all contributors
labels:
  - good first issue
milestone: PyCon Sprints 2025
state: open
state_reason: null
synced_at: 2026-01-07T18:48:39.093113Z
info:
  author: kjaymiller
  created_at: 2025-05-18T21:52:05Z
  updated_at: 2025-07-19T16:14:01Z
---

## Description

We should implement the [all-contributors](https://allcontributors.org/) specification to recognize all people who contribute to our project, not just code contributors. This will help us acknowledge various types of contributions including documentation, design, testing, and more.

## Motivation

- Properly recognize all contributors regardless of contribution type
- Create a more inclusive environment that values all forms of contribution
- Provide clear documentation of who has helped with the project and how
- Encourage more diverse contributions by showing we value all types of help

## Implementation Plan

- [ ] Initialize the specification: `npx all-contributors init`
- [ ] Add existing contributors using the CLI: `npx all-contributors add <username> <contribution-type>`
- [ ] Set up a .all-contributorsrc configuration file
- [ ] Add the contributors table to our README.md
- [ ] Document the process for adding new contributors in CONTRIBUTING.md

## Additional Details

- Contribution types to recognize: code, doc, design, bug, test, ideas, review, talk, tutorial, etc.
- CLI will maintain both .all-contributorsrc and README.md files automatically
- We can configure the bot to automatically suggest adding new contributors

## Questions

- Should we use the all-contributors bot for automated PRs?
- What emoji/acknowledgment style should we use for the contributors table?
- Should we include the contributors table at the top or bottom of the README?

## Resources

- [all-contributors documentation](https://allcontributors.org/docs/en/overview)
- [Example repositories using all-contributors](https://github.com/all-contributors/all-contributors/blob/master/README.md#who-uses-it)
