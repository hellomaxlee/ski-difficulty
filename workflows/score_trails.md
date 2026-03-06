# score_trails — Strategy Plan

## Goal
Compute steepness metrics for each trail, normalize them, produce a weighted
composite difficulty score, and compare against official Sugarbush ratings.

## Input
Trails with `points` (sampled lat/lon) and `elevations` (SRTM meters per point).

## Computed Metrics

### 1. Vertical Drop
`(max_elevation - min_elevation) * 3.28084` → feet

### 2. Average Slope Angle
Mean of `arctan(|Δelev| / haversine_distance)` across all consecutive point pairs → degrees

### 3. Max Slope Angle
Maximum of the above across all consecutive point pairs → degrees

## Normalization
Min-max normalize each metric across all trails to a 0–1 scale.

## Weighted Composite Score
```
score = 0.15 * norm(vertical_drop)
      + 0.35 * norm(avg_slope)
      + 0.50 * norm(max_slope)
```

### NSAA Rationale
Weights derived from NSAA official trail rating guidelines:
- **Max slope (50%):** Primary criterion — NSAA rates trails by their steepest section
- **Avg slope (35%):** Secondary — sustained difficulty across the full run
- **Vertical drop (15%):** Not a direct NSAA rating factor; proxy for fatigue/stamina only

Source: NSAA adopted Disney's 3-tier system (1968); green <25% grade (~15°),
blue 25–40% (~15–22°), black 40%+ (~22°+). Ratings are based on steepest section.

## Computed Classification Thresholds
| Score Range | Computed Color  |
|-------------|-----------------|
| 0.00 – 0.25 | Green           |
| 0.25 – 0.50 | Blue            |
| 0.50 – 0.75 | Black           |
| 0.75 – 1.00 | Double Black    |

## Verdict
- **Accurate:** official == computed
- **Overestimated:** official harder than computed (trail easier than rated)
- **Underestimated:** official easier than computed (trail harder than rated)

## Output
List of result dicts sorted by composite score descending:
```python
{
    "name": str,
    "official": str,
    "vertical_drop_ft": float,
    "avg_slope_deg": float,
    "max_slope_deg": float,
    "composite_score": float,   # 0–1
    "computed": str,
    "verdict": str,
}
```
