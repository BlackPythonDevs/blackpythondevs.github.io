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
                    if k == "Name":
                        continue
                    # If the value is exactly True, show only the key name.
                    if v is True:
                        html += f"{k}<br>"
                        continue

                    # If the value is a list of years (or any list), show the key once.
                    # This keeps event names from repeating with each year.
                    if isinstance(v, list):
                        html += f"{k}<br>"
                        continue

                    # Otherwise recurse for nested structures.
                    html += f"<br><strong>{k}:</strong> <br>{render(v)}<br>"
                return html

        return render(data)

    # Filter + minimize features
    filtered_features = []
    for feature in geojson_data["features"]:
        props = feature["properties"]
        iso = props.get("ISO_A3")
        if iso == "-99":
            iso = props.get("ISO_A3_EH", iso)

        if iso in map_data:
            name = props.get("NAME", iso)
            data = map_data[iso]

            minimal_feature = {
                "type": "Feature",
                "properties": {
                    "ISO_A3": iso,
                    "Country": name,
                    "popup_html": f"<strong><span style='text-decoration: underline; font-size: 14px;'>{name}</span></strong><br>{build_popup_html(data)}",
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
        "#FFDA63",  # Pale Gold - Very light, almost a yellow-gold. Great for subtle highlights.
        "#FFB347",  # Peach Gold - A warmer, softer gold. Good for adding a gentle glow.
        "#FFC107",  # Amber Gold - A brighter, more saturated gold, leaning towards amber.
        "#FFD700",  # Gold - Classic, vibrant gold. Use sparingly for key landmarks or strong accents.
        "#E6CA00",  # Dark Gold - A deeper, richer gold with a hint of brown.  Excellent for shadows and adding depth.
        "#B8860B",  # Bronze Gold - A muted, aged gold with brown undertones.  Adds a sense of history and realism.
        "#8B4513",  # Saddle Gold - A dark, warm gold Best for deep shadows and distant elements.
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
            "color": "#ffffff",
            "weight": 0.7,
            "fillOpacity": 0.75,
        },
        tooltip=folium.GeoJsonTooltip(fields=["Country"]),
        popup=folium.GeoJsonPopup(fields=["popup_html"], labels=False, parse_html=True),
    ).add_to(m)

    # Add reset zoom control using a direct approach
    # This script will be added at the end and executed immediately
    reset_control_script = folium.Element("""
    <script>
    (function() {
        var attempts = 0;
        var maxAttempts = 50;
        
        function addResetControl() {
            attempts++;
            
            // Check if Leaflet is loaded
            if (typeof L === 'undefined' || !L.Control) {
                if (attempts < maxAttempts) {
                    setTimeout(addResetControl, 100);
                }
                return;
            }
            
            // Define the control if not already defined
            if (!L.Control.ResetZoom) {
                L.Control.ResetZoom = L.Control.extend({
                    options: { position: 'topleft' },
                    onAdd: function(map) {
                        var container = L.DomUtil.create('div', 'leaflet-bar leaflet-control');
                        var link = L.DomUtil.create('a', '', container);
                        link.href = '#';
                        link.title = 'Reset map zoom';
                        link.innerHTML = '↺';
                        link.style.width = '30px';
                        link.style.height = '30px';
                        link.style.lineHeight = '30px';
                        link.style.textAlign = 'center';
                        link.style.fontSize = '18px';
                        link.style.cursor = 'pointer';
                        
                        L.DomEvent.on(link, 'click', function(e) {
                            L.DomEvent.preventDefault(e);
                            map.setView([20, 0], 2);
                        });
                        L.DomEvent.on(link, 'mouseover', function() {
                            link.style.backgroundColor = '#f4f4f4';
                        });
                        L.DomEvent.on(link, 'mouseout', function() {
                            link.style.backgroundColor = '';
                        });
                        L.DomEvent.disableClickPropagation(link);
                        return container;
                    }
                });
                L.control.resetZoom = function(opts) {
                    return new L.Control.ResetZoom(opts);
                };
            }
            
            // Find all map divs and add the control
            var mapDivs = document.querySelectorAll('[id^="map_"]');
            var added = false;
            mapDivs.forEach(function(mapDiv) {
                var mapId = mapDiv.id;
                if (window[mapId] && typeof window[mapId].addControl === 'function') {
                    try {
                        window[mapId].addControl(L.control.resetZoom());
                        added = true;
                    } catch(e) {
                        // Control might already be added
                    }
                }
            });
            
            // If we couldn't add and still have attempts, try again
            if (!added && attempts < maxAttempts) {
                setTimeout(addResetControl, 100);
            }
        }
        
        // Start the process
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', addResetControl);
        } else {
            // DOM already loaded
            setTimeout(addResetControl, 50);
        }
    })();
    </script>
    """)
    
    m.get_root().html.add_child(reset_control_script)

    # Save
    map_path = "assets/map.html"
    m.save(map_path)

    logging.info(f"Map saved as {map_path}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    generate_map()
