"""
Resort configuration registry for the Trail Analyzer.

Each entry defines the resort's display name, OSM bounding box, geographic
zone splits (for multi-mountain resorts), UI color theme, and official
terrain mix (resort-published difficulty distribution).

Zone assignment: trail's avg latitude is compared against each zone's
lat_threshold in order — the first zone whose threshold exceeds the avg lat
is used. Single-mountain resorts have one zone with lat_threshold=inf.

terrain_mix: Official resort-published percentages for each difficulty tier.
These are used for classification thresholds instead of counting OSM tags,
which are crowd-sourced and often inaccurate. Values are fractions summing
to 1.0. Where resorts publish only a combined "advanced/expert" number,
the split between Black and Double Black is estimated from resort materials.
"""

import math

RESORTS = {
    "sugarbush": {
        "name": "Sugarbush Resort",
        "location": "Warren, VT",
        "bbox": (44.12, -72.94, 44.19, -72.88),
        "terrain_mix": {"Green": 0.23, "Blue": 0.43, "Black": 0.27, "Double Black": 0.07},
        "zones": [
            {"name": "Lincoln Peak", "lat_threshold": 44.155},
            {"name": "Mt. Ellen",    "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#0b120e", "surface": "#111a14", "surface2": "#162019",
            "border": "#243028", "text": "#cdd9c8", "muted": "#5e7a62", "accent": "#c4a05a",
        },
    },
    "killington": {
        "name": "Killington Resort",
        "location": "Killington, VT",
        "bbox": (43.58, -72.90, 43.70, -72.77),
        "terrain_mix": {"Green": 0.17, "Blue": 0.40, "Black": 0.32, "Double Black": 0.11},
        "zones": [
            {"name": "Bear Mountain",    "lat_threshold": 43.607},
            {"name": "Killington Peak",  "lat_threshold": 43.628},
            {"name": "Skye Peak",        "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#120a0b", "surface": "#1c1013", "surface2": "#231419",
            "border": "#361a1e", "text": "#d9c4c6", "muted": "#8a5560", "accent": "#c44a55",
        },
    },
    "stowe": {
        "name": "Stowe Mountain Resort",
        "location": "Stowe, VT",
        "bbox": (44.50, -72.84, 44.57, -72.74),
        "terrain_mix": {"Green": 0.16, "Blue": 0.55, "Black": 0.17, "Double Black": 0.12},
        "zones": [
            {"name": "Spruce Peak",   "lat_threshold": 44.527},
            {"name": "Mt. Mansfield", "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#090b12", "surface": "#0f1220", "surface2": "#141828",
            "border": "#1e2540", "text": "#c8cdd9", "muted": "#4a5a8a", "accent": "#5a7ac4",
        },
    },
    "vail": {
        "name": "Vail Mountain",
        "location": "Vail, CO",
        "bbox": (39.57, -106.47, 39.69, -106.32),
        "terrain_mix": {"Green": 0.18, "Blue": 0.29, "Black": 0.49, "Double Black": 0.04},
        "zones": [
            {"name": "Back Bowls",   "lat_threshold": 39.620},
            {"name": "Front Side",   "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#080c14", "surface": "#0e1422", "surface2": "#13192e",
            "border": "#1a2540", "text": "#c4ccd9", "muted": "#4a6080", "accent": "#4a90c4",
        },
    },
    "breckenridge": {
        "name": "Breckenridge",
        "location": "Breckenridge, CO",
        "bbox": (39.44, -106.12, 39.54, -106.02),
        "terrain_mix": {"Green": 0.12, "Blue": 0.21, "Black": 0.27, "Double Black": 0.40},
        "zones": [
            {"name": "Peaks 6 & 7", "lat_threshold": 39.500},
            {"name": "Peaks 8–10",  "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#0a0b14", "surface": "#111320", "surface2": "#161928",
            "border": "#202540", "text": "#c4c8d9", "muted": "#505880", "accent": "#7a6ac4",
        },
    },
    "park_city": {
        "name": "Park City Mountain",
        "location": "Park City, UT",
        "bbox": (40.59, -111.63, 40.72, -111.48),
        "terrain_mix": {"Green": 0.08, "Blue": 0.41, "Black": 0.28, "Double Black": 0.23},
        "zones": [
            {"name": "Park City Side", "lat_threshold": 40.655},
            {"name": "Canyons Side",   "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#130e08", "surface": "#201608", "surface2": "#281c0c",
            "border": "#3a2810", "text": "#d9ccc4", "muted": "#8a7050", "accent": "#c47a3a",
        },
    },
    "snowbird": {
        "name": "Snowbird",
        "location": "Alta, UT",
        "bbox": (40.55, -111.69, 40.62, -111.60),
        "terrain_mix": {"Green": 0.08, "Blue": 0.22, "Black": 0.43, "Double Black": 0.27},
        "zones": [
            {"name": "Hidden Peak", "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#0a0e14", "surface": "#0f1520", "surface2": "#141c28",
            "border": "#1e2a3c", "text": "#c8d4e0", "muted": "#5a7090", "accent": "#8ab8e0",
        },
    },
    "big_sky": {
        "name": "Big Sky Resort",
        "location": "Big Sky, MT",
        "bbox": (45.22, -111.47, 45.34, -111.33),
        "terrain_mix": {"Green": 0.15, "Blue": 0.25, "Black": 0.42, "Double Black": 0.18},
        "zones": [
            {"name": "Andesite Mountain", "lat_threshold": 45.278},
            {"name": "Lone Peak",         "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#080f0a", "surface": "#0d1510", "surface2": "#111c14",
            "border": "#1a2c1e", "text": "#c4d4c8", "muted": "#3a6040", "accent": "#5aab6a",
        },
    },
    "jackson_hole": {
        "name": "Jackson Hole",
        "location": "Teton Village, WY",
        "bbox": (43.55, -110.90, 43.65, -110.77),
        "terrain_mix": {"Green": 0.04, "Blue": 0.41, "Black": 0.38, "Double Black": 0.17},
        "zones": [
            {"name": "Apres Vous",       "lat_threshold": 43.594},
            {"name": "Rendezvous Mtn",   "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#100d08", "surface": "#1a1510", "surface2": "#221c15",
            "border": "#342a1e", "text": "#d4ccbf", "muted": "#7a6a50", "accent": "#c4a068",
        },
    },
    "mammoth": {
        "name": "Mammoth Mountain",
        "location": "Mammoth Lakes, CA",
        "bbox": (37.59, -119.08, 37.67, -119.00),
        "terrain_mix": {"Green": 0.25, "Blue": 0.40, "Black": 0.20, "Double Black": 0.15},
        "zones": [
            {"name": "Main Lodge Side", "lat_threshold": 37.630},
            {"name": "Canyon Lodge",    "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#120a0a", "surface": "#1e0f0f", "surface2": "#251414",
            "border": "#3a1c1c", "text": "#d4c4c4", "muted": "#8a4a4a", "accent": "#c46060",
        },
    },
    "heavenly": {
        "name": "Heavenly Mountain",
        "location": "South Lake Tahoe, CA/NV",
        "bbox": (38.88, -119.98, 38.97, -119.87),
        "terrain_mix": {"Green": 0.07, "Blue": 0.60, "Black": 0.28, "Double Black": 0.05},
        "zones": [
            {"name": "California Side", "lat_threshold": 38.930},
            {"name": "Nevada Side",     "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#130f08", "surface": "#201808", "surface2": "#28200c",
            "border": "#3c3010", "text": "#d9d0c4", "muted": "#8a7a50", "accent": "#d4a030",
        },
    },
    "steamboat": {
        "name": "Steamboat Resort",
        "location": "Steamboat Springs, CO",
        "bbox": (40.43, -106.84, 40.51, -106.75),
        "terrain_mix": {"Green": 0.14, "Blue": 0.42, "Black": 0.40, "Double Black": 0.04},
        "zones": [
            {"name": "Christie Peak", "lat_threshold": 40.462},
            {"name": "Storm Peak",    "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#100d08", "surface": "#1c1810", "surface2": "#241e14",
            "border": "#362c1c", "text": "#d4ccbf", "muted": "#7a6a50", "accent": "#c48040",
        },
    },
    "copper_mountain": {
        "name": "Copper Mountain",
        "location": "Frisco, CO",
        "bbox": (39.47, -106.21, 39.54, -106.10),
        "terrain_mix": {"Green": 0.21, "Blue": 0.25, "Black": 0.36, "Double Black": 0.18},
        "zones": [
            {"name": "West Village", "lat_threshold": 39.500},
            {"name": "East Village", "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#120e08", "surface": "#1e1610", "surface2": "#261c14",
            "border": "#3a2a1c", "text": "#d4ccbf", "muted": "#8a7060", "accent": "#c47840",
        },
    },
    "sun_valley": {
        "name": "Sun Valley",
        "location": "Ketchum, ID",
        "bbox": (43.68, -114.42, 43.75, -114.30),
        "terrain_mix": {"Green": 0.36, "Blue": 0.42, "Black": 0.20, "Double Black": 0.02},
        "zones": [
            {"name": "Dollar Mountain", "lat_threshold": 43.710},
            {"name": "Bald Mountain",   "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#090e0a", "surface": "#0f1610", "surface2": "#141c15",
            "border": "#1e2c20", "text": "#c4d0c8", "muted": "#508060", "accent": "#80a870",
        },
    },
    "keystone": {
        "name": "Keystone Resort",
        "location": "Keystone, CO",
        "bbox": (39.58, -106.02, 39.65, -105.90),
        "terrain_mix": {"Green": 0.12, "Blue": 0.39, "Black": 0.43, "Double Black": 0.06},
        "zones": [
            {"name": "Dercum Mountain", "lat_threshold": 39.613},
            {"name": "North Peak",      "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#090c12", "surface": "#0f1420", "surface2": "#141c28",
            "border": "#1e2a38", "text": "#c4ccd8", "muted": "#506070", "accent": "#6090a0",
        },
    },
    "aspen_snowmass": {
        "name": "Aspen Snowmass",
        "location": "Aspen, CO",
        # Covers all four mountains: Snowmass, Highlands, Buttermilk, Aspen (Ajax)
        "bbox": (39.14, -106.97, 39.26, -106.78),
        "terrain_mix": {"Green": 0.06, "Blue": 0.43, "Black": 0.17, "Double Black": 0.34},
        "zones": [
            {"name": "Aspen / Highlands / Buttermilk", "lat_threshold": 39.196},
            {"name": "Snowmass",                        "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#0c0c12", "surface": "#131320", "surface2": "#181828",
            "border": "#26263c", "text": "#d0d0e0", "muted": "#6060a0", "accent": "#b0a0d8",
        },
    },
    "camelback": {
        "name": "Camelback Resort",
        "location": "Tannersville, PA",
        "bbox": (41.02, -75.37, 41.07, -75.30),
        "terrain_mix": {"Green": 0.39, "Blue": 0.26, "Black": 0.26, "Double Black": 0.09},
        "zones": [
            {"name": "Camelback Mountain", "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#0a0c10", "surface": "#10141c", "surface2": "#151a24",
            "border": "#202836", "text": "#c4ccd8", "muted": "#506070", "accent": "#5080b0",
        },
    },
    "palisades_tahoe": {
        "name": "Palisades Tahoe",
        "location": "Olympic Valley, CA",
        "bbox": (39.13, -120.28, 39.21, -120.18),
        "zones": [
            {"name": "Alpine Meadows", "lat_threshold": 39.175},
            {"name": "Palisades",      "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#081012", "surface": "#0e181e", "surface2": "#122028",
            "border": "#1a3040", "text": "#c4d8e0", "muted": "#4a7888", "accent": "#5ac0d8",
        },
    },
    "mt_bachelor": {
        "name": "Mt. Bachelor",
        "location": "Bend, OR",
        "bbox": (43.96, -121.72, 44.01, -121.66),
        "zones": [
            {"name": "South Side", "lat_threshold": 43.985},
            {"name": "Summit",     "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#0e0c0a", "surface": "#181410", "surface2": "#201a14",
            "border": "#30281e", "text": "#d4ccc4", "muted": "#7a6a58", "accent": "#c08a50",
        },
    },
    "winter_park": {
        "name": "Winter Park Resort",
        "location": "Winter Park, CO",
        "bbox": (39.84, -105.80, 39.89, -105.75),
        "zones": [
            {"name": "Mary Jane",    "lat_threshold": 39.867},
            {"name": "Winter Park",  "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#080e0a", "surface": "#0e1810", "surface2": "#142014",
            "border": "#1e301e", "text": "#c4d4c4", "muted": "#4a704a", "accent": "#68b060",
        },
    },
    "northstar": {
        "name": "Northstar California",
        "location": "Truckee, CA",
        "bbox": (39.24, -120.16, 39.28, -120.09),
        "zones": [
            {"name": "Backside",  "lat_threshold": 39.262},
            {"name": "Frontside", "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#12100a", "surface": "#1e1a10", "surface2": "#262014",
            "border": "#38301c", "text": "#d8d0c0", "muted": "#887848", "accent": "#d4a830",
        },
    },
    "alta": {
        "name": "Alta Ski Area",
        "location": "Alta, UT",
        "bbox": (40.57, -111.64, 40.60, -111.56),
        "zones": [
            {"name": "Albion Basin",    "lat_threshold": 40.585},
            {"name": "Collins / Wildcat", "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#0a0e12", "surface": "#10161e", "surface2": "#141e28",
            "border": "#1e2e3c", "text": "#d0dce8", "muted": "#6080a0", "accent": "#90c0e8",
        },
    },
    "telluride": {
        "name": "Telluride Ski Resort",
        "location": "Telluride, CO",
        "bbox": (37.88, -107.87, 37.95, -107.81),
        "zones": [
            {"name": "Town Side",        "lat_threshold": 37.915},
            {"name": "Mountain Village", "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#120a08", "surface": "#1e100c", "surface2": "#281614",
            "border": "#3c201a", "text": "#d8c8c0", "muted": "#8a5848", "accent": "#c46840",
        },
    },
    "deer_valley": {
        "name": "Deer Valley Resort",
        "location": "Park City, UT",
        "bbox": (40.60, -111.53, 40.66, -111.46),
        "zones": [
            {"name": "Snow Park",    "lat_threshold": 40.635},
            {"name": "Empire Canyon", "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#0c0c0e", "surface": "#141418", "surface2": "#1a1a20",
            "border": "#282830", "text": "#d0d0d8", "muted": "#686878", "accent": "#a0a0c0",
        },
    },
    "crested_butte": {
        "name": "Crested Butte",
        "location": "Crested Butte, CO",
        "bbox": (38.87, -106.97, 38.92, -106.93),
        "zones": [
            {"name": "Front Side",     "lat_threshold": 38.900},
            {"name": "North Face",     "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#100a12", "surface": "#1a1020", "surface2": "#201628",
            "border": "#30203c", "text": "#d4c8d8", "muted": "#7a5090", "accent": "#b870d0",
        },
    },
    "arapahoe_basin": {
        "name": "Arapahoe Basin",
        "location": "Dillon, CO",
        "bbox": (39.61, -105.89, 39.65, -105.85),
        "zones": [
            {"name": "Pallavicini",     "lat_threshold": 39.630},
            {"name": "Montezuma Bowl",  "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#0a0c10", "surface": "#101420", "surface2": "#141a28",
            "border": "#1e2838", "text": "#c8d0dc", "muted": "#506880", "accent": "#6898c0",
        },
    },
    "taos": {
        "name": "Taos Ski Valley",
        "location": "Taos Ski Valley, NM",
        "bbox": (36.56, -105.47, 36.60, -105.43),
        "zones": [
            {"name": "Lower Mountain",  "lat_threshold": 36.575},
            {"name": "Kachina Peak",    "lat_threshold": math.inf},
        ],
        "theme": {
            "bg": "#120c08", "surface": "#1e1610", "surface2": "#261c14",
            "border": "#3a2a1c", "text": "#d8ccbf", "muted": "#8a6850", "accent": "#c87840",
        },
    },
}


def assign_zone(avg_lat, zones):
    """Return the zone name for a trail based on its average latitude."""
    for zone in zones:
        if avg_lat < zone["lat_threshold"]:
            return zone["name"]
    return zones[-1]["name"]
