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

Use the `add_conference` script — it updates `sponsored_events.json`,
`map_data.json`, and regenerates `assets/map.html` in one step:

```
just add-conference --title "PyCon Cameroon" --year 2026 --continent "Africa" --country "Cameroon"
```

Or call the script directly (required when the title contains spaces and
dashes, since `just` splits positional args):

```
uv run python scripts/add_conference.py \
    --title "Django Girls - Tamale" \
    --year 2026 \
    --continent "Africa" \
    --country "Ghana"
```

The country name is fuzzy-matched to an ISO_A3 code via `pycountry`. Valid
continents: Africa, Antarctica, Asia, Europe, North America, Oceania,
South America.

Event names are plain strings — no URL is rendered. If you want a linked page,
use the `bpd` list instead and create the corresponding event page under
`events/` (e.g. `events/leadership-summit-2026-ohio.md`).

### Manual edit (fallback)

If the script is unavailable, edit `_data/sponsored_events.json` directly:
find the year and region under `sponsored`, append the event name, and add
the year/region keys if missing. Then update `_data/map_data.json` and
re-run `uv run python scripts/map.py` to regenerate the map.

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
