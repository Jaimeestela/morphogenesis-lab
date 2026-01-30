"""Paths stay inside domain and respect minimum separation (where applicable)."""

import sys
from pathlib import Path

import numpy as np
import pytest
from shapely.geometry import Polygon, box, Point

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "src"))

from morphogenesis.paths.streamline import streamlines_in_polygon
from morphogenesis.paths.serpentine import serpentine_fill_room
from morphogenesis.grids import make_xy
from morphogenesis.fields import gradient_2d


def test_serpentine_stays_inside():
    poly = box(0, 0, 5, 4)
    plist = serpentine_fill_room(poly, pitch=0.5, offset=0.2)
    for pl in plist:
        for p in pl:
            assert poly.contains(Point(p)) or poly.boundary.contains(Point(p))


def test_streamlines_inside_domain():
    # Simple constant gradient -> streamlines straight; domain rectangle
    nx, ny = 20, 20
    x_1d = np.linspace(0, 19, nx)
    y_1d = np.linspace(0, 19, ny)
    vx = np.ones((ny, nx))
    vy = np.zeros((ny, nx))
    domain = box(1, 1, 18, 18)
    plist = streamlines_in_polygon(domain, vx, vy, x_1d, y_1d, step=0.5, separation=2, n_seed=5)
    for pl in plist:
        for p in pl:
            assert domain.contains(Point(p)) or domain.boundary.contains(Point(p)), f"Point {p} outside"
