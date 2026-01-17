---
title: Add permissiosn to workflows at the issue level
labels:
  - security
state: open
state_reason: null
synced_at: 2026-01-07T18:48:39.090011Z
info:
  author: kjaymiller
  created_at: 2024-10-05T21:08:48Z
  updated_at: 2024-10-05T21:49:47Z
---

Actions should have issue

## Why

We have settings that allow for actions to create Pull Requests against our code using GitHub actions.

By Setting restrictions only where they are needed and setting actions to read otherwise will reduce the action space in which this can be applied.

#### Remediation (click "Show more" below):

> Set top-level permissions as read-all or contents: read as described in GitHub's [documentation](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#permissions).

Set this if there if GITHUB_TOKEN is not being used.

> Set any required write permissions at the job-level. Only set the permissions required for that job; do not set permissions: write-all at the job level.

For actions where GITHUB_TOKEN is being used then we need to set the permissions in the job where it is required.

> To help determine the permissions needed for your workflows, you may use [StepSecurity's online tool](https://app.stepsecurity.io/secureworkflow/) by ticking the "Restrict permissions for GITHUB_TOKEN". You may also tick the "Pin actions to a full length commit SHA" to fix issues found by the Pinned-dependencies check.
