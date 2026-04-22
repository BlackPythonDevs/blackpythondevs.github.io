# Add a Foundational Supporter

Foundational Supporters are individuals who financially back BPD for a given
calendar year. They render on the Support page from `_data/foundational_supporters.json`.

**Reference PRs:** #893 (Carol Willing), #879 (Jay Miller), #870 (Sarah Drasner)

## Steps

1. Open `_data/foundational_supporters.json`.
2. Find the entry for the current year (e.g. `"2026": [...]`). If it does not
   yet exist, add a new top-level key for the year with an empty array.
3. Add the supporter's full name to the array. Keep the array alphabetically
   sorted by first name to match existing convention.
4. Save. No other files need to change — the `foundational_supporters` include
   renders directly from this JSON.
5. Run `just test` to confirm JSON is valid and site builds.
6. Commit with a message like `Add <Name> to <year> foundational supporters`
   and open a PR.

## Verification

- `just serve` → visit `/support` and confirm the name renders in the right year.
- No image asset is needed for foundational supporters.

## Gotchas

- Do not reorder prior years' lists; only touch the current year.
- Names are rendered verbatim — match the spelling/capitalization the supporter requests.
