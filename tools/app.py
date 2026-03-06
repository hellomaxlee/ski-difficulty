"""
FastAPI app for the Ski Trail Analyzer.
Run with: uv run uvicorn tools.app:app --reload --host 0.0.0.0 --port 8000
"""

from collections import Counter

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from pathlib import Path

from tools.resorts import RESORTS
from tools.fetch_trails import fetch_trails
from tools.fetch_elevations import add_elevations_to_trails
from tools.score_trails import score_trails, WEIGHTS
import tools.cache as cache

app = FastAPI(title="Ski Trail Analyzer")

# In-memory layer on top of disk cache; keyed by resort_id
_mem_cache: dict = {}


def analyze_resort(resort_id: str) -> dict:
    """Fetch, score, and return full trail data for one resort."""
    resort = RESORTS[resort_id]

    print(f"Fetching trails from OpenStreetMap for {resort['name']}...")
    trails = fetch_trails(resort)
    print(f"Found {len(trails)} named, classified trails.")

    print("Fetching elevation data...")
    trails_with_elevations = add_elevations_to_trails(trails)

    print("Scoring trails...")
    scored = score_trails(trails_with_elevations)

    counts = Counter(t["official"] for t in scored)
    total = len(scored)
    official_distribution = {k: round(v / total, 4) for k, v in counts.items()}

    return {
        "trails": scored,
        "official_distribution": official_distribution,
        "default_weights": WEIGHTS,
        "resort": {
            "id": resort_id,
            "name": resort["name"],
            "location": resort["location"],
            "theme": resort["theme"],
            "zones": [z["name"] for z in resort["zones"]],
        },
    }


@app.get("/api/resorts")
def list_resorts():
    """Return the full list of available resorts for the selector."""
    return [
        {"id": rid, "name": r["name"], "location": r["location"]}
        for rid, r in RESORTS.items()
    ]


@app.get("/api/trails")
def get_trails(resort: str = Query(default="sugarbush")):
    if resort not in RESORTS:
        raise HTTPException(status_code=404, detail=f"Unknown resort: {resort}")

    # Memory cache hit
    if resort in _mem_cache:
        return _mem_cache[resort]

    # Disk cache hit
    cached = cache.load(resort)
    if cached is not None:
        _mem_cache[resort] = cached
        return cached

    # Full fetch
    result = analyze_resort(resort)
    cache.save(resort, result)
    _mem_cache[resort] = result
    return result


@app.post("/api/refresh")
def refresh(resort: str = Query(default="sugarbush")):
    if resort not in RESORTS:
        raise HTTPException(status_code=404, detail=f"Unknown resort: {resort}")
    _mem_cache.pop(resort, None)
    cache.clear(resort)
    return {"status": "cache cleared", "resort": resort}


@app.get("/", response_class=HTMLResponse)
def index():
    template_path = Path(__file__).parent / "templates" / "index.html"
    return template_path.read_text()
