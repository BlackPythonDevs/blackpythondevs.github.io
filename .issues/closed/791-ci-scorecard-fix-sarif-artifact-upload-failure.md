---
title: "ci(scorecard): fix SARIF artifact upload failure"
state: closed
state_reason: COMPLETED
synced_at: 2026-01-09T15:22:57.573527Z
info:
  author: danielcristho
  created_at: 2026-01-09T03:17:51Z
  updated_at: 2026-01-09T14:41:59Z
---

When running the Scorecard Action, the workflow fails during the artifact upload step with an error indicating that the artifact name is invalid.

This happens even when using artifact names that should be valid (no spaces, lowercase, alphanumeric, dashes/underscores).

## Error Message

Error: Create Artifact Container failed: The artifact name SARIF file is not valid. Request URL https://pipelinesghubeus6.actions.githubusercontent.com/iy4Z8D0GvaulvD6DIxMLnT5xBJC6xgz4ekGRxUSJ6YnGhcqqKU/_apis/pipelines/workflows/20839594535/artifacts?api-version=6.0-preview
