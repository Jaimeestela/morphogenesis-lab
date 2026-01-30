"""
Multi-room domain: serpentine fill per room + collector. Export DXF/SVG with layers.
Uses simple_rooms.geojson if present, else a minimal 2-room example.
"""

import sys
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "src"))

from morphogenesis.config import ensure_output_dirs, EXPORTS_DIR, DOMAINS_DIR
from morphogenesis.paths.serpentine import serpentine_rooms_with_collector
from morphogenesis.cad.dxf_export import export_polylines_dxf
from morphogenesis.cad.svg_export import export_polylines_svg
from shapely.geometry import Polygon, box

ensure_output_dirs()

# Default: two simple rooms and a collector line
ROOMS = {
    "room_1": box(0, 0, 5, 4),
    "room_2": box(6, 0, 11, 4),
}
COLLECTOR_LINE = [(5.5, -0.5), (5.5, 4.5)]
PITCH = 0.3
OFFSET = 0.15


def load_rooms_geojson(path: Path) -> dict:
    """Load rooms from GeoJSON; return dict room_id -> Polygon."""
    try:
        import json
        with open(path) as f:
            data = json.load(f)
        rooms = {}
        for i, feat in enumerate(data.get("features", [])):
            geom = feat.get("geometry")
            if geom and geom.get("type") == "Polygon":
                from shapely.geometry import shape as geom_shape
                poly = geom_shape(geom)
                if poly.is_valid:
                    rooms[f"room_{i}"] = poly
        return rooms
    except Exception:
        return {}


def main():
    geojson_path = DOMAINS_DIR / "simple_rooms.geojson"
    if geojson_path.exists():
        rooms = load_rooms_geojson(geojson_path)
        if not rooms:
            rooms = ROOMS
    else:
        rooms = ROOMS

    result = serpentine_rooms_with_collector(
        rooms,
        COLLECTOR_LINE,
        pitch=PITCH,
        offset=OFFSET,
    )
    polylines_by_layer = {}
    for rid, plist in result["room_paths"].items():
        polylines_by_layer[rid] = plist
    polylines_by_layer["collector"] = [result["collector"]]
    polylines_by_layer["connections"] = result["connections"]

    export_polylines_dxf(EXPORTS_DIR / "serpentine_rooms.dxf", polylines_by_layer)
    export_polylines_svg(EXPORTS_DIR / "serpentine_rooms.svg", polylines_by_layer)
    print(f"Exported to {EXPORTS_DIR}/serpentine_rooms.dxf and .svg")


if __name__ == "__main__":
    main()
