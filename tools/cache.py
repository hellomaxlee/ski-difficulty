"""
Disk-based cache for processed trail results.

Saves the full API response for each resort to cache/{resort_id}.json.
Survives server restarts — first fetch takes ~3-4 min, all subsequent
loads (including after deploys) are instant reads from disk.
"""

import json
from pathlib import Path
from typing import Optional

CACHE_DIR = Path(__file__).parent.parent / "cache"


def _path(resort_id: str) -> Path:
    return CACHE_DIR / f"{resort_id}.json"


def load(resort_id: str) -> Optional[dict]:
    """Return cached result for resort, or None if not cached."""
    p = _path(resort_id)
    if p.exists():
        return json.loads(p.read_text())
    return None


def save(resort_id: str, data: dict) -> None:
    """Persist result to disk."""
    CACHE_DIR.mkdir(exist_ok=True)
    _path(resort_id).write_text(json.dumps(data))


def clear(resort_id: str) -> bool:
    """Delete cached file. Returns True if a file was deleted."""
    p = _path(resort_id)
    if p.exists():
        p.unlink()
        return True
    return False
