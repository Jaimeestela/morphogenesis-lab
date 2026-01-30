"""Sanity: solver produces finite values and reasonable shapes."""

import sys
from pathlib import Path

import numpy as np
import pytest

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "src"))

from morphogenesis.rd_solvers import solve_2d
from morphogenesis.config import get_default_grayscott, get_default_schnakenberg


def test_grayscott_no_nans():
    params = get_default_grayscott()
    u, v, _ = solve_2d("grayscott", params, nx=32, ny=32, n_steps=100, seed=42)
    assert np.all(np.isfinite(u))
    assert np.all(np.isfinite(v))
    assert u.shape == (32, 32)
    assert v.shape == (32, 32)


def test_schnakenberg_no_nans():
    params = get_default_schnakenberg()
    u, v, _ = solve_2d("schnakenberg", params, nx=32, ny=32, n_steps=100, seed=42)
    assert np.all(np.isfinite(u))
    assert np.all(np.isfinite(v))
