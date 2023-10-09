# https://en.wikipedia.org/wiki/GeoJSON
# https://realpython.com/python-folium-web-maps-from-data/#create-a-choropleth-map-with-your-data
# https://geopandas.org/en/stable/gallery/polygon_plotting_with_folium.html
import functools
import json
import random
from pathlib import Path

import faker
import folium
import geopy
import pandas as pd
import requests

fake = faker.Faker()

continents = ["Africa", "Asia", "Australia", "Europe", "North America", "South America"]
# Based on Discord members
num_users = 165
users = []
users_path = Path(__file__).parent / "users.json"
membership_path = Path(__file__).parent / "membership_map.html"

print("[Faker] Generating fake users...")

for _ in range(num_users):
    user = {"full_name": fake.name()}
    user["discord_username"] = f"{fake.user_name()}#{random.randint(1000, 9999)}"
    user["continent_location"] = random.choices(
        continents, weights=[0.15, 0.15, 0.3, 0.5, 0.7, 0.25], k=1
    )[0]
    users.append(user)

users_json = json.dumps(users, indent=2)

with users_path.open("w") as f:
    f.write(users_json)

print("Saved to users.json")

users_df = pd.read_json(users_path)
geolocator = geopy.Nominatim(user_agent="blackpythondevs.github.io")


# @lru_cache decorator with a maxsize of 6 (the number of continents)
@functools.lru_cache(maxsize=6)
def get_continent_coords(continent):
    location = geolocator.geocode(continent)
    return (location.latitude, location.longitude)


print("[geopy] Getting coordinates of continents...")

users_df["continent_coords"] = users_df["continent_location"].apply(
    get_continent_coords
)
# Group the DataFrame by continent location and count the number of users
# Also keep the first value of the continent coordinates for each group
users_by_continent = users_df.groupby("continent_location").agg(
    user_count=("full_name", "count"),
    continent_coords=("continent_location", lambda x: get_continent_coords(x.iloc[0])),
)

print("Members per continent:")
print(f"{users_by_continent}\n")

m = folium.Map(location=[0, 0], zoom_start=2)
# heat_data = []
geo_data = json.loads(
    requests.get(
        "https://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
    ).text
)

for index, row in users_by_continent.iterrows():
    continent = index
    user_count = row["user_count"]
    coords = row["continent_coords"]
    # heat_data.append([coords[0], coords[1], user_count])
    # Marker with the coordinates and a popup text
    marker = folium.Marker(
        location=coords,
        popup=f"{continent}: {user_count} members",
        icon=folium.Icon(color="blue"),
    )
    marker.add_to(m)


# heat_map = plugins.HeatMap(
#     heat_data,
#     radius=50,
#     gradient={0.4: "blue", 0.65: "lime", 1: "red"},
#     min_opacity=0.5,
# )
# heat_map.add_to(m)

users_by_continent = users_by_continent.reset_index(names=["continent"])

folium.Choropleth(
    geo_data=geo_data,
    name="choropleth",
    data=users_by_continent,
    columns=["continent", "user_count"],
    key_on="feature.properties.continent",  # by name
    fill_color="YlOrRd",  # ‘YlGn’, ‘YlOrRd’, ‘BuPu’
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Number of members by continent",
).add_to(m)

folium.LayerControl().add_to(m)

m.save(membership_path)
print(f"{membership_path} saved.")
