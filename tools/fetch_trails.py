"""
Fetch downhill trail geometry and official difficulty from OpenStreetMap
for a given ski resort using the Overpass API.
"""

import time
import requests
from typing import List

from tools.resorts import assign_zone

OSM_DIFFICULTY_MAP = {
    "novice": "Green",
    "easy": "Green",
    "intermediate": "Blue",
    "advanced": "Black",
    "expert": "Double Black",
    "extreme": "Double Black",   # cliff drops, extreme chutes; capped at Double Black for scoring
    "freeride": "Double Black",  # unmapped off-piste; treat as most difficult
}

# Grooming values indicating ungroomed / challenging off-piste conditions
UNGROOMED_VALUES = {"mogul", "backcountry", "freeride"}


def fetch_trails(resort: dict) -> List[dict]:
    """
    Query Overpass API for all named, classified downhill trails within the
    resort's bounding box. Returns trail dicts with name, official difficulty,
    mountain zone, grooming, and geometry.
    """
    lat_min, lon_min, lat_max, lon_max = resort["bbox"]
    query = f"""
    [out:json];
    (
      way["piste:type"="downhill"]({lat_min},{lon_min},{lat_max},{lon_max});
    );
    out geom;
    """
    for attempt in range(4):
        response = requests.post(
            "https://overpass-api.de/api/interpreter",
            data={"data": query},
            timeout=60,
        )
        if response.status_code in (429, 502, 503, 504):
            wait = 5 * (attempt + 1)
            print(f"  Overpass returned {response.status_code}, retrying in {wait}s...")
            time.sleep(wait)
            continue
        response.raise_for_status()
        break

    elements = response.json()["elements"]

    # Group ways by (name, official color) — OSM often splits one trail into
    # multiple ways at lift crossings or intersections
    groups = {}
    for el in elements:
        tags = el.get("tags", {})
        name = tags.get("name") or tags.get("piste:name")
        difficulty_tag = tags.get("piste:difficulty", "")
        official_color = OSM_DIFFICULTY_MAP.get(difficulty_tag)
        geometry = el.get("geometry", [])

        if not name or not official_color or len(geometry) < 2:
            continue

        grooming = tags.get("piste:grooming", "")
        key = (name, official_color)
        groups.setdefault(key, []).append((geometry, grooming))

    trails = []
    for (name, official_color), way_tuples in groups.items():
        geometries = [g for g, _ in way_tuples]
        # Prefer any ungroomed grooming value found across merged ways
        groomings = [g for _, g in way_tuples if g]
        grooming = next(
            (g for g in groomings if g in UNGROOMED_VALUES),
            groomings[0] if groomings else "",
        )
        merged = _stitch_ways(geometries)
        avg_lat = sum(n["lat"] for n in merged) / len(merged)
        mountain = assign_zone(avg_lat, resort["zones"])

        trails.append({
            "name": name,
            "official": official_color,
            "mountain": mountain,
            "grooming": grooming,
            "geometry": merged,
        })

    return trails


def _stitch_ways(ways: list) -> list:
    """
    Stitch a list of OSM way geometries into a single continuous polyline.
    Each geometry is a list of {"lat", "lon"} node dicts. Ways are joined by
    matching endpoints; each way may be reversed if needed.
    """
    if len(ways) == 1:
        return ways[0]

    def endpoint(way, end):
        n = way[-1] if end == "tail" else way[0]
        return (n["lat"], n["lon"])

    chain = [list(w) for w in ways]
    result = chain.pop(0)

    while chain:
        tail = endpoint(result, "tail")
        best_idx, best_rev, best_dist = None, False, float("inf")

        for i, way in enumerate(chain):
            head = endpoint(way, "head")
            tail_w = endpoint(way, "tail")
            d_head = abs(tail[0] - head[0]) + abs(tail[1] - head[1])
            d_tail = abs(tail[0] - tail_w[0]) + abs(tail[1] - tail_w[1])
            if d_head < best_dist:
                best_dist, best_idx, best_rev = d_head, i, False
            if d_tail < best_dist:
                best_dist, best_idx, best_rev = d_tail, i, True

        way = chain.pop(best_idx)
        if best_rev:
            way = list(reversed(way))
        start = 1 if endpoint(result, "tail") == (way[0]["lat"], way[0]["lon"]) else 0
        result.extend(way[start:])

    return result
