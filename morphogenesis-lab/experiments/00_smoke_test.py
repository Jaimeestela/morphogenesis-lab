"""
Smoke test: import package, run a few RD steps, check no NaNs.
"""

import sys
from pathlib import Path

# Ensure src is on path
repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "src"))

from morphogenesis.config import ensure_output_dirs
from morphogenesis.rd_solvers import solve_2d
from morphogenesis.config import get_default_grayscott

ensure_output_dirs()

def main():
    params = get_default_grayscott()
    u, v, snaps = solve_2d(
        "grayscott",
        params,
        nx=64,
        ny=64,
        dx=1.0,
        dt=0.5,
        n_steps=50,
        seed=42,
    )
    assert u is not None and v is not None
    assert u.shape == (64, 64) and v.shape == (64, 64)
    import numpy as np
    assert not np.any(~np.isfinite(u))
    assert not np.any(~np.isfinite(v))
    print("Smoke test OK: no NaNs, shape correct.")

if __name__ == "__main__":
    main()
