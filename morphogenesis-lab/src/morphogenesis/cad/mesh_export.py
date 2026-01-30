"""
Export to mesh (STL/optional STEP) for 3D. Optional dependency: trimesh, pyvista.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import List, Sequence, Tuple

logger = logging.getLogger(__name__)

try:
    import trimesh
    _HAS_TRIMESH = True
except ImportError:
    _HAS_TRIMESH = False


def polylines_to_extruded_mesh(
    polylines: List[Sequence[Tuple[float, float]]],
    height: float = 0.1,
) -> "trimesh.Trimesh | None":
    """
    Extrude 2D polylines to thin 3D meshes (e.g. tube cross-section as rectangle).
    Returns a single merged trimesh or None if trimesh not available.
    """
    if not _HAS_TRIMESH:
        return None
    meshes = []
    for pl in polylines:
        if len(pl) < 2:
            continue
        line = [[p[0], p[1], 0.0] for p in pl]
        # Simple extrusion: duplicate at z=height and add side faces
        pts = []
        for p in line:
            pts.append(p)
            pts.append([p[0], p[1], height])
        # Build triangles (simplified: two triangles per segment)
        # trimesh.path.polygon or creation from line is not direct; use a simple box per segment
        pass  # Placeholder: full implementation would create prism per segment
    if not meshes:
        return None
    return trimesh.util.concatenate(meshes)


def export_mesh_stl(
    filepath: str | Path,
    mesh: "trimesh.Trimesh",
) -> None:
    """Export trimesh to STL."""
    if not _HAS_TRIMESH:
        raise ImportError("trimesh is required. pip install trimesh")
    mesh.export(str(filepath))
    logger.info("Saved STL to %s", filepath)
