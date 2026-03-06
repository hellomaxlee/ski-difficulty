# run — Strategy Plan

## Goal
Start the Sugarbush Trail Analyzer FastAPI web server in development mode
with auto-reload enabled for easy debugging.

## Usage
```bash
uv run python tools/run.py
```

## What It Does
1. Launches uvicorn pointing at `tools.app:app`
2. Enables `--reload` so code changes restart the server automatically
3. Serves on `http://localhost:8000`

## Endpoints
| Route          | Description                          |
|----------------|--------------------------------------|
| `GET /`        | Serves the trail analyzer website    |
| `GET /api/trails` | Returns JSON array of all trail results |

## First-Load Behavior
- On the first `GET /api/trails` request, the full pipeline runs:
  1. `fetch_trails` — OSM query (~2s)
  2. `fetch_elevations` — elevation API (~1–3 min depending on trail count)
  3. `score_trails` — normalization and scoring (~instant)
- Results are cached in memory; subsequent requests return instantly
- The website shows a spinner during first load

## Stopping the Server
Press `Ctrl+C` in the terminal where the server is running.
