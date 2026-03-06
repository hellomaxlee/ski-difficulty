# fetch_trails — Strategy Plan

## Goal
Query OpenStreetMap via the Overpass API to fetch all downhill ski trail geometries
and official difficulty classifications for Sugarbush Resort.

## Data Source
- **API:** Overpass API (`https://overpass-api.de/api/interpreter`)
- **Query tag:** `piste:type=downhill` within Sugarbush bounding box
- **Bounding box:** `44.12, -72.94, 44.19, -72.88`
  - Derived from OpenSkiMap resort polygon: `44.1276–44.1796°N, 72.886–72.928°W`
  - Covers both Lincoln Peak and Mt. Ellen with margin
- **Response format:** `out geom` — includes full node geometry per way

## OSM Difficulty Tag Mapping
| OSM `piste:difficulty` | Display Color |
|------------------------|---------------|
| novice                 | Green         |
| easy                   | Green         |
| intermediate           | Blue          |
| advanced               | Black         |
| expert                 | Double Black  |

## Output
List of trail dicts:
```python
{
    "name": str,        # from tags["name"] or tags["piste:name"]
    "official": str,    # "Green" / "Blue" / "Black" / "Double Black"
    "geometry": list,   # [{"lat": float, "lon": float}, ...]
}
```

## Filtering
- Skip trails with no name
- Skip trails with no recognized difficulty tag
- Skip trails with fewer than 2 geometry nodes
