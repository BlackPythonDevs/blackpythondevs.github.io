# Add or Update a Sponsored Event

Sponsored events are listed on the homepage and the About page, rendered from
`_data/sponsored_events.json`.

**Reference PRs:** #863 (2026 update), #854 (typo fix)

## Data shape

`_data/sponsored_events.json` has two top-level keys:

- `bpd` — list of BPD-owned events (objects with `title` + `url` pointing at
  a page under `/bpd-events/`).
- `sponsored` — dict keyed by year, then by region (Africa, North America,
  South America, …), each a list of event-name strings.

## Add a sponsored event

1. Open `_data/sponsored_events.json`.
2. Find the current year and the region.
3. Append the event name. If the region doesn't exist for that year yet, add it.
4. If it's the first event of a new year, add the year key with region sub-keys.

Event names are plain strings — no URL is rendered. If you want a linked page,
use the `bpd` list instead and create the corresponding event page under
`events/` (e.g. `events/leadership-summit-2026-ohio.md`).

## Add a BPD-owned event

1. Create the event markdown at `events/<slug>.md`. Reference existing ones
   like `events/leadership-summit-2026-ohio.md` for frontmatter.
2. Add an entry to the `bpd` array in `sponsored_events.json`:
   ```json
   { "title": "<Event Title>", "url": "/bpd-events/<slug>.html" }
   ```

## Checks

- `just test` — validates JSON.
- `just serve` — confirm the event appears in the sponsored-events include on
  the homepage / About page.

## Gotchas

- Don't re-order historical years; only edit the year you're changing.
- Event name strings must match whatever is publicly promoted — these are
  shown verbatim.
