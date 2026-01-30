"""
Brusselator 2D: generate pattern, save snapshots PNG and arrays.
"""

import sys
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "src"))

from morphogenesis.config import ensure_output_dirs, PATTERNS_DIR, get_default_brusselator
from morphogenesis.rd_solvers import solve_2d
from morphogenesis.utils.plotting import plot_pattern
from morphogenesis.utils.io import save_snapshot

ensure_output_dirs()

PARAMS = get_default_brusselator()
NX, NY = 256, 256
DX = 1.0
DT = 0.2
N_STEPS = 8000
SEED = 42
SNAPSHOT_EVERY = 2000


def main():
    u, v, snapshots = solve_2d(
        "brusselator",
        PARAMS,
        nx=NX,
        ny=NY,
        dx=DX,
        dt=DT,
        n_steps=N_STEPS,
        seed=SEED,
        snapshot_every=SNAPSHOT_EVERY,
    )
    plot_pattern(u, v, filepath=PATTERNS_DIR / "brusselator_final.png", title="Brusselator final")
    save_snapshot(PATTERNS_DIR / "brusselator_final.npz", u, v)
    for step, u_s, v_s in snapshots:
        plot_pattern(
            u_s, v_s,
            filepath=PATTERNS_DIR / f"brusselator_snapshot_{step:06d}.png",
            title=f"Brusselator step {step}",
        )
    print(f"Saved patterns to {PATTERNS_DIR}")


if __name__ == "__main__":
    main()
