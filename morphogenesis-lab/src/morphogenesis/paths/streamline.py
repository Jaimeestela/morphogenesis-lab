"""
Streamlines from a scalar field phi: grad(phi) or rotated field, with step and separation control.
Clipping to Shapely polygon and handling of holes (obstacles).
"""

from __future__ import annotations

import logging
import numpy as np
from typing import List, Tuple, Optional, Callable
from shapely.geometry import Point, Polygon, LineString
from shapely.ops import unary_union

from morphogenesis.grids import make_xy
from morphogenesis.fields import gradient_2d, rotated_gradient_2d, vector_field_at_points

logger = logging.getLogger(__name__)


def _integrate_streamline(
    x0: float,
    y0: float,
    get_velocity: Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]],
    polygon: Polygon,
    step: float,
    max_steps: int,
    forward: bool = True,
) -> List[Tuple[float, float]]:
    """
    Integrate one streamline from (x0,y0) using Euler with step.
    get_velocity(x_arr, y_arr) -> (vx, vy). Clips to polygon. Stops when leaving or max_steps.
    """
    pts: List[Tuple[float, float]] = [(x0, y0)]
    sign = 1 if forward else -1
    for _ in range(max_steps - 1):
        x_arr = np.array([pts[-1][0]])
        y_arr = np.array([pts[-1][1]])
        vx, vy = get_velocity(x_arr, y_arr)
        vx, vy = vx[0], vy[0]
        n = np.hypot(vx, vy)
        if n < 1e-12:
            break
        vx, vy = vx / n, vy / n
        x_new = pts[-1][0] + sign * step * vx
        y_new = pts[-1][1] + sign * step * vy
        pt = Point(x_new, y_new)
        if not polygon.contains(pt) and not polygon.boundary.contains(pt):
            # Clip to boundary if we crossed
            line = LineString([pts[-1], (x_new, y_new)])
            inter = polygon.boundary.intersection(line)
            if not inter.is_empty:
                if inter.geom_type == "Point":
                    pts.append((inter.x, inter.y))
                elif inter.geom_type == "MultiPoint":
                    pt_geom = inter.geoms[0]
                    pts.append((pt_geom.x, pt_geom.y))
            break
        pts.append((x_new, y_new))
    return pts


def streamlines_in_polygon(
    polygon: Polygon,
    vx: np.ndarray,
    vy: np.ndarray,
    x_1d: np.ndarray,
    y_1d: np.ndarray,
    step: float = 0.5,
    separation: float = 1.0,
    max_steps: int = 2000,
    seed_points: Optional[List[Tuple[float, float]]] = None,
    n_seed: int = 30,
    holes: Optional[List[Polygon]] = None,
) -> List[List[Tuple[float, float]]]:
    """
    Generate streamlines inside polygon from vector field (vx, vy) on grid (x_1d, y_1d).
    - step: integration step length.
    - separation: minimum distance between seed points (approximate).
    - seed_points: if provided, use these as seeds; else generate n_seed points inside polygon.
    - holes: optional list of polygons to exclude (obstacles); streamline stops when entering.
    Returns list of polylines (each a list of (x,y)).
    """
    if holes:
        domain = polygon
        for h in holes:
            domain = domain.difference(h)
        if domain.is_empty or domain.geom_type == "GeometryCollection":
            domain = polygon
        else:
            polygon = domain if isinstance(domain, Polygon) else polygon
    bounds = polygon.bounds
    minx, miny, maxx, maxy = bounds

    def get_vel(x_pts: np.ndarray, y_pts: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        return vector_field_at_points(vx, vy, x_1d, y_1d, x_pts, y_pts)

    if seed_points is None:
        rng = np.random.default_rng(42)
        candidates = []
        for _ in range(n_seed * 20):
            x = rng.uniform(minx, maxx)
            y = rng.uniform(miny, maxy)
            pt = Point(x, y)
            if polygon.contains(pt):
                candidates.append((x, y))
        # Subsample by separation
        seed_points = []
        for c in candidates:
            too_close = False
            for s in seed_points:
                if np.hypot(c[0] - s[0], c[1] - s[1]) < separation:
                    too_close = True
                    break
            if not too_close:
                seed_points.append(c)
            if len(seed_points) >= n_seed:
                break

    polylines: List[List[Tuple[float, float]]] = []
    for (x0, y0) in seed_points:
        pt = Point(x0, y0)
        if not polygon.contains(pt):
            continue
        line_fwd = _integrate_streamline(
            x0, y0, get_vel, polygon, step, max_steps, forward=True
        )
        line_bwd = _integrate_streamline(
            x0, y0, get_vel, polygon, step, max_steps, forward=False
        )
        if len(line_bwd) > 1:
            line_bwd = line_bwd[1:][::-1]
        full = line_bwd + line_fwd
        if len(full) >= 2:
            polylines.append(full)
    return polylines


def streamlines_from_scalar(
    phi: np.ndarray,
    x_1d: np.ndarray,
    y_1d: np.ndarray,
    polygon: Polygon,
    use_rotated: bool = True,
    step: float = 0.5,
    separation: float = 1.0,
    max_steps: int = 2000,
    n_seed: int = 30,
    dx: float = 1.0,
    dy: Optional[float] = None,
) -> List[List[Tuple[float, float]]]:
    """
    Build vector field from scalar phi (gradient or rotated gradient) and generate streamlines.
    use_rotated: if True, use field tangent to isocontours (for "following" contours).
    """
    dy = dy if dy is not None else dx
    if use_rotated:
        vx, vy = rotated_gradient_2d(phi, dx, dy)
    else:
        vx, vy = gradient_2d(phi, dx, dy)
    return streamlines_in_polygon(
        polygon,
        vx,
        vy,
        x_1d,
        y_1d,
        step=step,
        separation=separation,
        max_steps=max_steps,
        n_seed=n_seed,
    )
