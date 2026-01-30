"""
Take RD snapshot (u or v), build scalar phi, generate streamlines, export DXF/SVG.
"""

import sys
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "src"))

from morphogenesis.config import ensure_output_dirs, PATTERNS_DIR, PATHS_DIR, EXPORTS_DIR
from morphogenesis.grids import make_xy
from morphogenesis.fields import scalar_from_uv, smooth_scalar
from morphogenesis.paths.streamline import streamlines_from_scalar
from morphogenesis.cad.dxf_export import export_polylines_dxf
from morphogenesis.cad.svg_export import export_polylines_svg
from shapely.geometry import Polygon, box
import numpy as np

ensure_output_dirs()

# Use a small RD snapshot or load from file
NX, NY = 128, 128
DX = 1.0
PHI_MODE = "v"
USE_SNAPSHOT_FILE = False
SNAPSHOT_PATH = PATTERNS_DIR / "gs_final.npz"


def main():
    if USE_SNAPSHOT_FILE and SNAPSHOT_PATH.exists():
        from morphogenesis.utils.io import load_snapshot
        u, v = load_snapshot(SNAPSHOT_PATH)
        nx, ny = v.shape[1], v.shape[0]
        x_1d = np.linspace(0, (nx - 1) * DX, nx)
        y_1d = np.linspace(0, (ny - 1) * DX, ny)
    else:
        # Minimal inline run
        from morphogenesis.rd_solvers import solve_2d
        from morphogenesis.config import get_default_grayscott
        params = get_default_grayscott()
        u, v, _ = solve_2d("grayscott", params, nx=NX, ny=NY, dx=DX, n_steps=2000, seed=42)
        nx, ny = NX, NY
        x_1d, y_1d = make_xy(nx, ny, DX)

    phi = scalar_from_uv(u, v, mode=PHI_MODE)
    phi = smooth_scalar(phi, sigma=2.0)
    domain = box(0, 0, (nx - 1) * DX, (ny - 1) * DX)
    polylines = streamlines_from_scalar(
        phi, x_1d, y_1d, domain,
        use_rotated=True,
        step=0.3,
        separation=1.5,
        n_seed=25,
        dx=DX,
    )
    polylines_by_layer = {"streamlines": polylines}
    export_polylines_dxf(EXPORTS_DIR / "streamlines.dxf", polylines_by_layer)
    export_polylines_svg(EXPORTS_DIR / "streamlines.svg", polylines_by_layer)
    print(f"Exported to {EXPORTS_DIR}/streamlines.dxf and .svg")


if __name__ == "__main__":
    main()
