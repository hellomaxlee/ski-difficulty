# cache — Strategy Plan

## Goal
Persist processed trail results to disk so that server restarts and subsequent
page loads are instant — without re-hitting OSM or the elevation API.

## Cache Location
`cache/{resort_id}.json` relative to the project root.

## Behavior
- **Load**: if file exists, read and return parsed JSON immediately
- **Save**: after fresh fetch+score, write result to disk as JSON
- **Clear**: delete the file for a specific resort (triggered by POST /api/refresh)

## Data Stored
The full API response object per resort:
```json
{
    "trails": [...],
    "official_distribution": {...},
    "default_weights": {...}
}
```

## Why Disk (not just memory)
- Server restarts (deploys, crashes) lose in-memory state
- First fetch for any resort takes ~3–4 minutes; disk cache makes all
  subsequent loads instant regardless of how the server was started
- Safe for single-process deployment (no concurrency issues with simple file I/O)

## Invalidation
- Manual only: `POST /api/refresh?resort={id}` deletes the cache file
- No TTL — trail geometry and elevation data change rarely
