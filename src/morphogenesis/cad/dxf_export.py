"""
Export polylines to DXF (R12 or ACAD2000) with layers per room/collector/routes.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import List, Dict, Sequence, Tuple

logger = logging.getLogger(__name__)

try:
    import ezdxf
    from ezdxf.document import Drawing
    _HAS_EZDXF = True
except ImportError:
    _HAS_EZDXF = False


def export_polylines_dxf(
    filepath: str | Path,
    polylines_by_layer: Dict[str, List[Sequence[Tuple[float, float]]]],
    dxf_version: str = "ACAD2000",
) -> None:
    """
    Export polylines to DXF. polylines_by_layer: layer_name -> list of polylines (each = list of (x,y)).
    Layers: e.g. "room_1", "room_2", "collector", "routes".
    """
    if not _HAS_EZDXF:
        raise ImportError("ezdxf is required for DXF export. pip install ezdxf")

    doc = ezdxf.new(dxf_version)
    msp = doc.modelspace()

    for layer_name, polylines in polylines_by_layer.items():
        if layer_name not in doc.layers:
            doc.layers.add(layer_name)
        for pl in polylines:
            if len(pl) < 2:
                continue
            points = [(float(p[0]), float(p[1]), 0.0) for p in pl]
            msp.add_lwpolyline(
                points,
                dxfattribs={"layer": layer_name},
            )
    doc.saveas(str(filepath))
    logger.info("Saved DXF to %s", filepath)
