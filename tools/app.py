"""
FastAPI app for the Sugarbush Trail Analyzer.
Run with: uv run uvicorn tools.app:app --reload
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json

from tools.sugarbush_trail_analyzer import analyze_trails

app = FastAPI(title="Sugarbush Trail Analyzer")

# Cache results so we don't re-fetch on every request
_cached_trails = None


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
