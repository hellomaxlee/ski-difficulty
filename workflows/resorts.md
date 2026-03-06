# resorts — Strategy Plan

## Goal
Central configuration registry for all supported ski resorts. Each entry
provides everything needed to fetch, label, and theme a resort's trail data.

## Data per Resort
```python
{
    "name": str,               # Display name, e.g. "Killington Resort"
    "location": str,           # "Town, State"
    "bbox": (lat_min, lon_min, lat_max, lon_max),  # Overpass query bounds
    "zones": [                 # Geographic mountain/peak splits, checked in order
        {"name": str, "lat_threshold": float},     # trail avg_lat < threshold → this zone
    ],
    "theme": {                 # CSS custom property overrides (7 vars)
        "bg", "surface", "surface2", "border", "text", "muted", "accent"
    }
}
```

## Zone Assignment
- Compute avg latitude of merged trail geometry
- Iterate zones in order; assign the first zone whose `lat_threshold` exceeds avg_lat
- Single-mountain resorts have one zone with `lat_threshold: inf`

## Supported Resorts (top 15 US by skiable acreage + Sugarbush)
| ID              | Resort                  | State |
|-----------------|-------------------------|-------|
| sugarbush       | Sugarbush Resort        | VT    |
| killington      | Killington Resort       | VT    |
| stowe           | Stowe Mountain Resort   | VT    |
| vail            | Vail Mountain           | CO    |
| breckenridge    | Breckenridge            | CO    |
| park_city       | Park City Mountain      | UT    |
| snowbird        | Snowbird                | UT    |
| big_sky         | Big Sky Resort          | MT    |
| jackson_hole    | Jackson Hole            | WY    |
| mammoth         | Mammoth Mountain        | CA    |
| heavenly        | Heavenly Mountain       | CA/NV |
| steamboat       | Steamboat Resort        | CO    |
| copper_mountain | Copper Mountain         | CO    |
| sun_valley      | Sun Valley              | ID    |
| keystone        | Keystone Resort         | CO    |

## Color Themes
Each resort has a unique palette reflecting its regional character:
- Vermont resorts: forest greens, burgundy, navy
- Colorado resorts: blues, purples, copper tones
- Utah resorts: desert oranges, icy blues
- Other western: Montana pine, Wyoming ochre, Idaho sage, California gold

`accent` replaces `--gold` as the primary highlight color.
