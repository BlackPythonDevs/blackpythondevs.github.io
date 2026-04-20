"""
Add a sponsored conference to the events data and regenerate the activity map.

Updates:
1. _data/sponsored_events.json — appends the conference under sponsored.<year>.<continent>
2. _data/map_data.json — adds/updates the country entry with the conference and year
3. assets/map.html — regenerates via scripts/map.py

Usage:
    uv run python scripts/add_conference.py \\
        --title "PyCon Brazil" \\
        --year 2026 \\
        --continent "South America" \\
        --country "Brazil"

The ISO_A3 country code is resolved from --country via pycountry.
"""

import json
from pathlib import Path

import click
import pycountry

from map import generate_map

ROOT = Path(__file__).resolve().parent.parent
SPONSORED_JSON = ROOT / "_data" / "sponsored_events.json"
MAP_JSON = ROOT / "_data" / "map_data.json"

CONTINENTS = [
    "Africa",
    "Antarctica",
    "Asia",
    "Europe",
    "North America",
    "Oceania",
    "South America",
]


def update_sponsored_events(title: str, year: int, continent: str) -> None:
    data = json.loads(SPONSORED_JSON.read_text())
    year_key = str(year)
    sponsored = data.setdefault("sponsored", {})
    year_bucket = sponsored.setdefault(year_key, {})
    continent_list = year_bucket.setdefault(continent, [])
    if title in continent_list:
        click.echo(
            f"  sponsored_events.json: '{title}' already listed for {continent} {year_key}"
        )
    else:
        continent_list.append(title)
        click.echo(
            f"  sponsored_events.json: added '{title}' to {continent} {year_key}"
        )
    SPONSORED_JSON.write_text(json.dumps(data, indent=2) + "\n")


def resolve_country(country: str) -> tuple[str, str]:
    """Return (ISO_A3, canonical_name) for a country name, using fuzzy matching."""
    try:
        matches = pycountry.countries.search_fuzzy(country)
    except LookupError as exc:
        raise click.ClickException(f"Could not resolve country '{country}'.") from exc
    match = matches[0]
    name = getattr(match, "common_name", match.name)
    return match.alpha_3, name


def update_map_data(title: str, year: int, iso: str, country: str) -> None:
    data = json.loads(MAP_JSON.read_text())
    entry = data.setdefault(iso, {})
    entry["Name"] = country
    sponsored = entry.setdefault("Sponsored", {})
    years = sponsored.setdefault(title, [])
    if year in years:
        click.echo(f"  map_data.json: '{title}' already has year {year} for {iso}")
    else:
        years.append(year)
        years.sort()
        click.echo(f"  map_data.json: added {year} to '{title}' under {iso}")
    MAP_JSON.write_text(json.dumps(data, indent=2) + "\n")


@click.command(help="Add a sponsored conference and regenerate the activity map.")
@click.option("--title", required=True, help="Conference title.")
@click.option("--year", type=int, required=True, help="Year sponsored.")
@click.option(
    "--continent",
    required=True,
    type=click.Choice(CONTINENTS, case_sensitive=False),
    help="Continent grouping for sponsored_events.json.",
)
@click.option(
    "--country",
    required=True,
    help="Country name (fuzzy-matched to ISO_A3 via pycountry).",
)
def main(title: str, year: int, continent: str, country: str) -> None:
    iso, canonical = resolve_country(country)
    click.echo(f"Resolved '{country}' → {canonical} ({iso})")
    click.echo(f"Adding '{title}' ({year}, {continent}, {iso})")
    update_sponsored_events(title, year, continent)
    update_map_data(title, year, iso, canonical)
    click.echo("Regenerating assets/map.html ...")
    generate_map()
    click.echo("Done.")


if __name__ == "__main__":
    main()
