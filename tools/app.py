"""
FastAPI app for the Sugarbush Trail Analyzer.
Run with: uv run python tools/run.py
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

from tools.fetch_trails import fetch_trails
from tools.fetch_elevations import add_elevations_to_trails
from tools.score_trails import score_trails

app = FastAPI(title="Sugarbush Trail Analyzer")

# Cache results in memory — cleared on server restart
_cached_trails = None


def analyze_trails():
    print("Fetching trails from OpenStreetMap...")
    trails = fetch_trails()
    print(f"Found {len(trails)} named, classified trails.")
    print("Fetching elevation data...")
    trails_with_elevations = add_elevations_to_trails(trails)
    print("Scoring trails...")
    return score_trails(trails_with_elevations)


@app.get("/api/trails")
def get_trails():
    global _cached_trails
    if _cached_trails is None:
        _cached_trails = analyze_trails()
    return _cached_trails


@app.get("/", response_class=HTMLResponse)
def index():
    template_path = Path(__file__).parent / "templates" / "index.html"
    return template_path.read_text()
