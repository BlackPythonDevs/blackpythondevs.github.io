"""

This script generates an interactive HTML world map using country-level GeoJSON
data and a custom dataset defined in `_data/data/map_data.json`.

Each country is shaded with a unique color and supports rich HTML popups
displaying structured event data (e.g., BPD events, sponsored conferences).

------------------------------------------------------------
DATA INPUT
------------------------------------------------------------

The map is driven entirely by:

    _data/data/map_data.json

This file must be structured as a dictionary keyed by ISO_A3 country codes:

Example:
{
  "USA": {
    "BPD": ["Event A", "Event B"],
    "Sponsored": ["Event X"]
  },
  "NGA": {
    "Sponsored": ["Event Y"]
  }
}

------------------------------------------------------------
HOW TO ADD OR UPDATE DATA
------------------------------------------------------------

1. Add a new country:
   - Use ISO_A3 country code as the key (e.g., "BRA", "KEN", "IND")
   - Ensure the country exists in the GeoJSON dataset

2. Add events:
   - Under each country, use category keys such as:
     - "Sponsored"

3. Example update:
   "BRA": {
     "Sponsored": [
       "PyCon Brazil",
       "Django Girls Brazil"
     ]
   }

4. Save the file:
   - Re-run this script ` python scripts/map.py` to regenerate the map:
       assets/map.html

------------------------------------------------------------
OUTPUT
------------------------------------------------------------

- Generates: assets/map.html
- Each country is color-coded
- Hover shows country name
- Click shows structured event popup with formatted HTML

------------------------------------------------------------
NOTES
------------------------------------------------------------

- Country codes must match ISO_A3 values in the GeoJSON file
- Popups support nested dictionaries and lists
- Designed for dark-mode basemaps (CartoDB dark_matter)
- Map is restricted from infinite horizontal scrolling
"""

import json
import logging

import folium
import requests


def generate_map():
    with open("_data/map_data.json") as f:
        map_data = json.load(f)

    GEOJSON_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_0_countries.geojson"

    response = requests.get(GEOJSON_URL, timeout=30)
    response.raise_for_status()
    geojson_data = response.json()

    # Reduce coordinate precision
    def round_coords(coords, precision=2):
        if isinstance(coords[0], list):
            return [round_coords(c, precision) for c in coords]
        return [round(c, precision) for c in coords]

    # Build popup HTML
    def build_popup_html(data):
        def render(value):
            if isinstance(value, dict):
                html = ""
                for k, v in value.items():
                    html += f"<strong>{k}:</strong> {render(v)}<br>"
                return html

            elif isinstance(value, list):
                return (
                    "<div style='margin-left:10px'>"
                    + "<br>".join(f"• {render(v)}" for v in value)
                    + "</div>"
                )

            elif isinstance(value, (int, float, str, bool)):
                return str(value)

            else:
                return str(value)

        return render(data)

    # Filter + minimize features
    filtered_features = []
    for feature in geojson_data["features"]:
        props = feature["properties"]
        iso = props.get("ISO_A3")

        if iso in map_data:
            name = props.get("NAME", iso)
            data = map_data[iso]

            minimal_feature = {
                "type": "Feature",
                "properties": {
                    "ISO_A3": iso,
                    "Country": name,
                    "popup_html": f"<strong><span style='text-decoration: underline; font-size: 14px;'>{name}</span></strong><br><br>{build_popup_html(data)}",
                },
                "geometry": {
                    "type": feature["geometry"]["type"],
                    "coordinates": round_coords(feature["geometry"]["coordinates"], 4),
                },
            }
            filtered_features.append(minimal_feature)

    countries_geo = {"type": "FeatureCollection", "features": filtered_features}

    # Curated high-contrast palette (dark-mode friendly)
    palette = [
        "#4E79A7",  # blue
        "#F28E2B",  # orange
        "#E15759",  # red
        "#76B7B2",  # teal
        "#59A14F",  # green
        "#EDC948",  # yellow
        "#B07AA1",  # purple
        "#FF9DA7",  # pink
        "#9C6ADE",  # violet
        "#17BECF",  # cyan
        "#FFBF00",  # amber
        "#2ECC71",  # bright green
        "#1F77B4",  # strong blue
        "#FF7F0E",  # vivid orange
        "#D62728",  # strong red
    ]

    iso_codes = (f["properties"]["ISO_A3"] for f in countries_geo["features"])

    country_colors = {iso: palette[i % len(palette)] for i, iso in enumerate(iso_codes)}

    m = folium.Map(
        location=[20, 0],
        zoom_start=2,
        min_zoom=2,
        max_zoom=8,
        tiles="CartoDB dark_matter",
        no_wrap=True,
        max_bounds=True,
    )

    folium.GeoJson(
        countries_geo,
        style_function=lambda feature: {
            "fillColor": country_colors.get(feature["properties"]["ISO_A3"]),
            "color": "#666",
            "weight": 0.7,
            "fillOpacity": 0.9,
        },
        tooltip=folium.GeoJsonTooltip(fields=["Country"]),
        popup=folium.GeoJsonPopup(fields=["popup_html"], labels=False, parse_html=True),
    ).add_to(m)

    # Save
    map_path = "assets/map.html"
    m.save(map_path)

    logging.info(f"Map saved as {map_path}")
