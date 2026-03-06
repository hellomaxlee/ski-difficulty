"""
Fetch downhill trail geometry and official difficulty from OpenStreetMap
for Sugarbush Resort using the Overpass API.
"""

import requests

# Bounding box derived from OpenSkiMap resort polygon (44.1276-44.1796°N, 72.886-72.928°W)
# Covers both Lincoln Peak and Mt. Ellen with margin
# (lat_min, lon_min, lat_max, lon_max)
SUGARBUSH_BBOX = (44.12, -72.94, 44.19, -72.88)

OSM_DIFFICULTY_MAP = {
    "novice": "Green",
    "easy": "Green",
    "intermediate": "Blue",
    "advanced": "Black",
    "expert": "Double Black",
}


def fetch_trails():
    """
    Query Overpass API for all named, classified downhill trails at Sugarbush.
    Returns a list of trail dicts with name, official difficulty, and geometry.
    """
    lat_min, lon_min, lat_max, lon_max = SUGARBUSH_BBOX
    query = f"""
    [out:json];
    (
      way["piste:type"="downhill"]({lat_min},{lon_min},{lat_max},{lon_max});
    );
    out geom;
    """
    response = requests.post(
        "https://overpass-api.de/api/interpreter",
        data={"data": query},
        timeout=30
    )
    response.raise_for_status()
    elements = response.json()["elements"]

    trails = []
    for el in elements:
        tags = el.get("tags", {})
        name = tags.get("name") or tags.get("piste:name")
        difficulty_tag = tags.get("piste:difficulty", "")
        official_color = OSM_DIFFICULTY_MAP.get(difficulty_tag)
        geometry = el.get("geometry", [])

        if not name or not official_color or len(geometry) < 2:
            continue

        trails.append({
            "name": name,
            "official": official_color,
            "geometry": geometry,
        })

    return trails
