"""
Gray-Scott 2D: generate stable pattern, save snapshots PNG and arrays.
Parameters: F=0.03, k=0.062 (pattern-forming). Seed 42 for reproducibility.
"""

import sys
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "src"))

from morphogenesis.config import ensure_output_dirs, PATTERNS_DIR, get_default_grayscott
from morphogenesis.rd_solvers import solve_2d
from morphogenesis.utils.plotting import plot_pattern
from morphogenesis.utils.io import save_snapshot
import numpy as np

ensure_output_dirs()

# Parameters (pattern-forming spots)
PARAMS = get_default_grayscott()
NX, NY = 256, 256
DX = 1.0
DT = 0.5
N_STEPS = 10000
SEED = 42
SNAPSHOT_EVERY = 2500


def main():
    u, v, snapshots = solve_2d(
        "grayscott",
        PARAMS,
        nx=NX,
        ny=NY,
        dx=DX,
        dt=DT,
        n_steps=N_STEPS,
        seed=SEED,
        snapshot_every=SNAPSHOT_EVERY,
    )
    # Final snapshot
    out_u = PATTERNS_DIR / "gs_u_final.png"
    out_v = PATTERNS_DIR / "gs_v_final.png"
    plot_pattern(u, v, filepath=PATTERNS_DIR / "gs_final.png", title="Gray-Scott final")
    save_snapshot(PATTERNS_DIR / "gs_final.npz", u, v)
    # Intermediate snapshots
    for step, u_s, v_s in snapshots:
        plot_pattern(
            u_s, v_s,
            filepath=PATTERNS_DIR / f"gs_snapshot_{step:06d}.png",
            title=f"Gray-Scott step {step}",
        )
    print(f"Saved patterns to {PATTERNS_DIR}")


if __name__ == "__main__":
    main()
