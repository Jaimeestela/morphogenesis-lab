"""
Export polylines to SVG for quick inspection.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import List, Dict, Sequence, Tuple

logger = logging.getLogger(__name__)

try:
    import svgwrite
    _HAS_SVGWRITE = True
except ImportError:
    _HAS_SVGWRITE = False


def _bounds(polylines_by_layer: Dict[str, List[Sequence[Tuple[float, float]]]]) -> Tuple[float, float, float, float]:
    minx = miny = float("inf")
    maxx = maxy = float("-inf")
    for polylines in polylines_by_layer.values():
        for pl in polylines:
            for p in pl:
                minx = min(minx, p[0])
                miny = min(miny, p[1])
                maxx = max(maxx, p[0])
                maxy = max(maxy, p[1])
    if minx == float("inf"):
        minx = miny = 0
        maxx = maxy = 100
    return minx, miny, maxx, maxy


def export_polylines_svg(
    filepath: str | Path,
    polylines_by_layer: Dict[str, List[Sequence[Tuple[float, float]]]],
    stroke_width: float = 0.5,
    margin: float = 10.0,
) -> None:
    """
    Export polylines to SVG. Each layer is a group. ViewBox from bounds + margin.
    """
    if not _HAS_SVGWRITE:
        raise ImportError("svgwrite is required for SVG export. pip install svgwrite")

    minx, miny, maxx, maxy = _bounds(polylines_by_layer)
    w = maxx - minx + 2 * margin
    h = maxy - miny + 2 * margin
    ox, oy = minx - margin, miny - margin

    dwg = svgwrite.Drawing(str(filepath), size=(f"{w}px", f"{h}px"), viewBox=f"0 0 {w} {h}")

    for layer_name, polylines in polylines_by_layer.items():
        g = dwg.g(id=layer_name)
        for pl in polylines:
            if len(pl) < 2:
                continue
            pts = [(p[0] - ox, p[1] - oy) for p in pl]
            path = dwg.polyline(
                pts,
                fill="none",
                stroke="black",
                stroke_width=stroke_width,
            )
            g.add(path)
        dwg.add(g)
    dwg.save()
    logger.info("Saved SVG to %s", filepath)
