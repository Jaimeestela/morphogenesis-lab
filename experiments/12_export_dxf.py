"""
Direct DXF/SVG export test: example polylines with layers (estancia, colector, rutas).
"""

import sys
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "src"))

from morphogenesis.config import ensure_output_dirs, EXPORTS_DIR
from morphogenesis.cad.dxf_export import export_polylines_dxf
from morphogenesis.cad.svg_export import export_polylines_svg

ensure_output_dirs()

# Example: one room with a few lines, collector, and one connection
POLYLINES = {
    "estancia_1": [
        [(0, 0), (3, 0), (3, 2), (0, 2), (0, 0)],
        [(0.5, 0.5), (2.5, 0.5), (2.5, 1.5), (0.5, 1.5)],
    ],
    "colector": [
        [(3.5, -0.2), (3.5, 2.2)],
    ],
    "rutas": [
        [(3, 1), (3.5, 1)],
    ],
}


def main():
    export_polylines_dxf(EXPORTS_DIR / "example_export.dxf", POLYLINES)
    export_polylines_svg(EXPORTS_DIR / "example_export.svg", POLYLINES)
    print(f"Exported to {EXPORTS_DIR}/example_export.dxf and .svg")


if __name__ == "__main__":
    main()
