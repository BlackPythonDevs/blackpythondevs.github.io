---
title: Make local development significantly easier
labels:
  - help wanted
projects:
  - Black Python Devs Planning
state: open
state_reason: null
synced_at: 2026-01-07T18:48:39.089122Z
info:
  author: kjaymiller
  created_at: 2024-08-29T13:15:57Z
  updated_at: 2024-12-31T14:24:07Z
---

I'm not sure why but I am completely unable to run this project outside of a devcontainer or codespace.

I'm not sure if it's issues with my local Ruby setup or not.

I'm open to different suggestions on this but the more we force folks to use codespaces then we limit their contribution based on what they are willing to pay for.

### Suggestions

#### Diagram

We need a diagram of the infrastructure to better understand the different tools that we're using.

- [x] #402

#### Dockerfile

Beauty of a dockerfile is that it can be the source for the codespace (we don't have access to the existing codespace dockerfile so we'd likely need to start over. It also means that we can implement this across operating systems as well.

#### Make or Invoke

I don't have a preference on this but we should make it simple to `setup`, `test`, `lint` and `run` services regardless of the language.

I would probably be more comfortable with invoke since it's python code but if someone knows enough about make to make it easy to follow I wouldn't mind.
