"""
Metrics for path quality: length, coverage uniformity, min radius, crossings, distance to borders.
See docs/04_cad_pipeline.md for criteria.
"""

from __future__ import annotations

import numpy as np
from typing import List, Sequence, Tuple
from shapely.geometry import LineString, Polygon, Point


def total_length(polylines: Sequence[Sequence[Tuple[float, float]]]) -> float:
    """Sum of lengths of all polyline segments."""
    total = 0.0
    for pl in polylines:
        if len(pl) < 2:
            continue
        ls = LineString(pl)
        total += ls.length
    return total


def min_distance_to_border(
    polyline: Sequence[Tuple[float, float]],
    polygon: Polygon,
) -> float:
    """Minimum distance from any point on the polyline to the boundary of the polygon."""
    if len(polyline) < 2:
        return float("inf")
    boundary = polygon.boundary
    if boundary.is_empty:
        return float("inf")
    ls = LineString(polyline)
    return ls.distance(boundary)


def min_radius_of_curvature(
    polyline: Sequence[Tuple[float, float]],
    step: int = 1,
) -> float:
    """
    Approximate minimum radius of curvature using three consecutive points.
    step: index step (1 = every point). Returns minimum R (or inf if not computable).
    """
    pts = np.array(polyline)
    if len(pts) < 3:
        return float("inf")
    R_min = float("inf")
    for i in range(step, len(pts) - step):
        p0 = pts[i - step]
        p1 = pts[i]
        p2 = pts[i + step]
        v1 = p1 - p0
        v2 = p2 - p1
        n1 = np.linalg.norm(v1)
        n2 = np.linalg.norm(v2)
        if n1 < 1e-12 or n2 < 1e-12:
            continue
        # Approximate curvature: 2*sin(angle/2) / (d/2) with d = (|v1|+|v2|)/2
        cos_a = np.dot(v1, v2) / (n1 * n2)
        cos_a = np.clip(cos_a, -1.0, 1.0)
        angle = np.arccos(cos_a)
        d = (n1 + n2) * 0.5
        if d < 1e-12:
            continue
        R = d / (2 * np.sin(angle / 2)) if angle > 1e-12 else float("inf")
        if R < R_min:
            R_min = R
    return R_min if R_min != float("inf") else 0.0


def count_self_crossings(polylines: Sequence[Sequence[Tuple[float, float]]]) -> int:
    """Count pairwise intersections between segments of the same or different polylines."""
    count = 0
    segments: List[LineString] = []
    for pl in polylines:
        for i in range(len(pl) - 1):
            segments.append(LineString([pl[i], pl[i + 1]]))
    for i in range(len(segments)):
        for j in range(i + 1, len(segments)):
            if segments[i].crosses(segments[j]) or segments[i].intersects(segments[j]):
                inter = segments[i].intersection(segments[j])
                if inter.geom_type == "Point" or inter.geom_type == "MultiPoint":
                    count += 1
    return count


def coverage_distances(
    polygon: Polygon,
    polylines: Sequence[Sequence[Tuple[float, float]]],
    n_samples: int = 500,
) -> np.ndarray:
    """
    Sample points inside polygon and compute distance to nearest polyline.
    Returns array of distances (for uniformity: std, histogram).
    """
    minx, miny, maxx, maxy = polygon.bounds
    rng = np.random.default_rng(42)
    distances = []
    for _ in range(n_samples):
        x = rng.uniform(minx, maxx)
        y = rng.uniform(miny, maxy)
        pt = Point(x, y)
        if not polygon.contains(pt):
            continue
        d_min = float("inf")
        for pl in polylines:
            ls = LineString(pl)
            d = pt.distance(ls)
            if d < d_min:
                d_min = d
        distances.append(d_min)
    return np.array(distances) if distances else np.array([0.0])
