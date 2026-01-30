"""
Medial axis / skeleton from binary mask or polygon (optional path strategy).
"""

from __future__ import annotations

from typing import List, Tuple
import numpy as np
from shapely.geometry import Polygon

# Optional: scikit-image medial_axis
try:
    from skimage.morphology import medial_axis
    _HAS_SKIMAGE = True
except ImportError:
    _HAS_SKIMAGE = False


def medial_axis_polyline(
    polygon: Polygon,
    resolution: float = 0.1,
) -> List[Tuple[float, float]]:
    """
    Approximate medial axis as a polyline (simplified: use centroid path or skeleton).
    If skimage available, rasterize polygon and compute medial_axis; else return centroid.
    """
    if _HAS_SKIMAGE:
        minx, miny, maxx, maxy = polygon.bounds
        nx = max(10, int((maxx - minx) / resolution))
        ny = max(10, int((maxy - miny) / resolution))
        xx = np.linspace(minx, maxx, nx)
        yy = np.linspace(miny, maxy, ny)
        X, Y = np.meshgrid(xx, yy)
        mask = np.zeros((ny, nx))
        for i in range(ny):
            for j in range(nx):
                mask[i, j] = polygon.contains(Point(xx[j], yy[i]))
        skel = medial_axis(mask)
        ys, xs = np.where(skel)
        if len(xs) == 0:
            c = polygon.centroid
            return [(c.x, c.y)]
        # Order points along skeleton (simplified: sort by x then y)
        pts = [(float(xx[x]), float(yy[y])) for x, y in zip(xs, ys)]
        return pts
    else:
        c = polygon.centroid
        return [(c.x, c.y)]
