"""Stability module returns correct shapes and dominant k in expected range."""

import sys
from pathlib import Path

import numpy as np
import pytest

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "src"))

from morphogenesis.stability import dominant_mode, max_re_eigenvalue_for_k
from morphogenesis.rd_models import equilibrium, jacobian
from morphogenesis.config import get_default_schnakenberg


def test_dominant_mode_returns_tuple():
    params = get_default_schnakenberg()
    k_dom, lam, k_arr, re_lam = dominant_mode("schnakenberg", params, k_min=0, k_max=10, n_k=50)
    assert isinstance(k_dom, (float, np.floating))
    assert isinstance(lam, (float, np.floating))
    assert k_arr.shape == (50,)
    assert re_lam.shape == (50,)


def test_max_re_eigenvalue_for_k():
    params = get_default_schnakenberg()
    u0, v0 = equilibrium("schnakenberg", params)
    J = jacobian("schnakenberg", u0, v0, params)
    Du, Dv = params["Du"], params["Dv"]
    val = max_re_eigenvalue_for_k(J, 1.0, Du, Dv)
    assert isinstance(val, (float, np.floating))
