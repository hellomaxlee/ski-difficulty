"""
Compute steepness metrics per trail, normalize across all trails, apply
NSAA-derived composite scoring, and compare against official difficulty ratings.
"""

import math
import numpy as np

from tools.fetch_elevations import haversine_distance

DIFFICULTY_ORDER = ["Green", "Blue", "Black", "Double Black"]

# Weights derived from NSAA official trail rating guidelines:
# - Max slope (50%): primary criterion — NSAA rates trails by their steepest section
# - Avg slope (35%): secondary — sustained difficulty across the full run
# - Vertical drop (15%): not a direct NSAA factor; proxy for fatigue/stamina only
WEIGHTS = {"vertical_drop": 0.15, "avg_slope": 0.35, "max_slope": 0.50}


def compute_metrics(points, elevations):
    """
    Compute vertical drop (ft), average slope (deg), and max slope (deg) for one trail.
    Returns None if no valid elevation data is available.
    """
    valid = [e for e in elevations if e is not None]
    if not valid:
        return None

    vertical_drop_ft = (max(valid) - min(valid)) * 3.28084

    slopes = []
    for i in range(1, len(points)):
        if elevations[i] is None or elevations[i - 1] is None:
            continue
        horiz = haversine_distance(
            points[i - 1][0], points[i - 1][1],
            points[i][0], points[i][1]
        )
        vert = abs(elevations[i] - elevations[i - 1])
        if horiz > 0:
            slopes.append(math.degrees(math.atan(vert / horiz)))

    return {
        "vertical_drop_ft": round(vertical_drop_ft, 1),
        "avg_slope_deg": round(float(np.mean(slopes)), 2) if slopes else 0.0,
        "max_slope_deg": round(float(np.max(slopes)), 2) if slopes else 0.0,
    }


def classify_score(score):
    """Map a 0–1 composite score to a difficulty color."""
    if score < 0.25:
        return "Green"
    if score < 0.50:
        return "Blue"
    if score < 0.75:
        return "Black"
    return "Double Black"


def verdict(official, computed):
    """Return Accurate / Overestimated / Underestimated."""
    if official not in DIFFICULTY_ORDER or computed not in DIFFICULTY_ORDER:
        return "Unknown"
    o = DIFFICULTY_ORDER.index(official)
    c = DIFFICULTY_ORDER.index(computed)
    if o == c:
        return "Accurate"
    return "Overestimated" if o > c else "Underestimated"


def score_trails(trails_with_elevations):
    """
    Compute metrics for each trail, normalize across all trails, apply weighted
    composite scoring, classify difficulty, and compare to official ratings.
    Returns a list of result dicts sorted by composite score descending.
    """
    computed = []
    for trail in trails_with_elevations:
        metrics = compute_metrics(trail["points"], trail["elevations"])
        if not metrics:
            continue
        computed.append({"name": trail["name"], "official": trail["official"], **metrics})

    if not computed:
        return []

    vd = np.array([r["vertical_drop_ft"] for r in computed])
    ag = np.array([r["avg_slope_deg"] for r in computed])
    ms = np.array([r["max_slope_deg"] for r in computed])

    def norm(arr):
        rng = arr.max() - arr.min()
        return (arr - arr.min()) / rng if rng > 0 else np.zeros_like(arr)

    composite = (
        WEIGHTS["vertical_drop"] * norm(vd)
        + WEIGHTS["avg_slope"] * norm(ag)
        + WEIGHTS["max_slope"] * norm(ms)
    )

    for i, result in enumerate(computed):
        score = float(composite[i])
        computed_color = classify_score(score)
        result["composite_score"] = round(score, 3)
        result["computed"] = computed_color
        result["verdict"] = verdict(result["official"], computed_color)

    computed.sort(key=lambda r: r["composite_score"], reverse=True)
    return computed
