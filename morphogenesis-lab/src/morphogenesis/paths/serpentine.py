"""
Serpentine (boustrophedon) fill per room and connection to a collector.
Deterministic baseline for underfloor heating / pipe routing.
"""

from __future__ import annotations

import logging
from typing import List, Tuple, Dict, Any, Optional
from shapely.geometry import Polygon, Point, LineString
import numpy as np

logger = logging.getLogger(__name__)


def _clip_to_polygon(
    pts: List[Tuple[float, float]],
    polygon: Polygon,
) -> List[Tuple[float, float]]:
    """Clip polyline to polygon: keep only segments inside, with boundary clips."""
    if not pts:
        return []
    inside = [polygon.contains(Point(p)) for p in pts]
    result = []
    for i, p in enumerate(pts):
        if inside[i]:
            result.append(p)
        else:
            if i > 0 and inside[i - 1]:
                line = LineString([pts[i - 1], p])
                inter = polygon.boundary.intersection(line)
                if not inter.is_empty and inter.geom_type == "Point":
                    result.append((inter.x, inter.y))
            elif i < len(pts) - 1 and inside[i + 1]:
                line = LineString([p, pts[i + 1]])
                inter = polygon.boundary.intersection(line)
                if not inter.is_empty and inter.geom_type == "Point":
                    result.append((inter.x, inter.y))
    return result


def serpentine_fill_room(
    polygon: Polygon,
    pitch: float = 0.3,
    min_radius: float = 0.1,
    offset: float = 0.15,
    origin: str = "miny",
) -> List[List[Tuple[float, float]]]:
    """
    Fill a single room (polygon) with serpentine / boustrophedon paths.
    - pitch: distance between parallel runs.
    - min_radius: minimum bend radius (simplified: we use sharp corners; can round later).
    - offset: margin from boundary.
    - origin: "miny" = start from bottom (min y), "minx", "maxy", "maxx".
    Returns list of polylines (each run of the serpentine as a list of points).
    """
    minx, miny, maxx, maxy = polygon.bounds
    # Shrink by offset
    minx += offset
    miny += offset
    maxx -= offset
    maxy -= offset
    if minx >= maxx or miny >= maxy:
        return []

    if origin == "miny":
        y_start = miny
        y_end = maxy
        x_min, x_max = minx, maxx
        horizontal = True
    elif origin == "maxy":
        y_start = maxy
        y_end = miny
        x_min, x_max = minx, maxx
        horizontal = True
    elif origin == "minx":
        x_start = minx
        x_end = maxx
        y_min, y_max = miny, maxy
        horizontal = False
    else:
        x_start = maxx
        x_end = minx
        y_min, y_max = miny, maxy
        horizontal = False

    polylines: List[List[Tuple[float, float]]] = []
    if horizontal:
        y = y_start
        direction = 1
        while y <= y_end if y_end >= y_start else y >= y_end:
            if direction == 1:
                pts = [(x_min, y), (x_max, y)]
            else:
                pts = [(x_max, y), (x_min, y)]
            clipped = _clip_to_polygon(pts, polygon)
            if len(clipped) >= 2:
                polylines.append(clipped)
            y += pitch if y_end >= y_start else -pitch
            direction *= -1
    else:
        x = x_start
        direction = 1
        while (x <= x_end if x_end >= x_start else x >= x_end):
            if direction == 1:
                pts = [(x, y_min), (x, y_max)]
            else:
                pts = [(x, y_max), (x, y_min)]
            clipped = _clip_to_polygon(pts, polygon)
            if len(clipped) >= 2:
                polylines.append(clipped)
            x += pitch if x_end >= x_start else -pitch
            direction *= -1

    return polylines


def _nearest_point_on_boundary(polygon: Polygon, pt: Tuple[float, float]) -> Tuple[float, float]:
    """Nearest point on polygon boundary to pt."""
    p = Point(pt)
    d = polygon.boundary.project(p)
    proj = polygon.boundary.interpolate(d)
    return (proj.x, proj.y)


def serpentine_rooms_with_collector(
    rooms: Dict[str, Polygon],
    collector_line: List[Tuple[float, float]],
    pitch: float = 0.3,
    offset: float = 0.15,
    corridor_graph: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    """
    Generate serpentine fill per room and connect each room to the collector.
    - rooms: dict room_id -> Polygon.
    - collector_line: polyline representing the collector (e.g. manifold).
    - corridor_graph: optional dict room_id -> list of adjacent room_ids for routing.
    Returns dict with keys: "room_paths" (room_id -> list of polylines), "collector" (polyline),
    "connections" (list of polylines from room connection point to collector).
    """
    room_paths: Dict[str, List[List[Tuple[float, float]]]] = {}
    for rid, poly in rooms.items():
        room_paths[rid] = serpentine_fill_room(poly, pitch=pitch, offset=offset)

    # Connection: from centroid or nearest boundary point of each room to nearest point on collector
    collector_linestring = LineString(collector_line)
    connections: List[List[Tuple[float, float]]] = []
    for rid, poly in rooms.items():
        centroid = poly.centroid
        cx, cy = centroid.x, centroid.y
        pt = Point(cx, cy)
        d = collector_linestring.project(pt)
        conn_pt = collector_linestring.interpolate(d)
        room_conn = _nearest_point_on_boundary(poly, (cx, cy))
        connections.append([room_conn, (conn_pt.x, conn_pt.y)])

    return {
        "room_paths": room_paths,
        "collector": collector_line,
        "connections": connections,
    }
