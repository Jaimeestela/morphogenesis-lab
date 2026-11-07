# Cursor: RD to trajectories

## Objective

Extract trajectories (streamlines and serpentine) from RD patterns or a deterministic planner, within 2D domains (polygons).

## Tasks

1. **streamline.py**: Scalar field φ → grad(φ) or rotated; streamline generation with fixed step and minimum separation; clipping to Shapely polygon; obstacles (holes).
2. **serpentine.py**: Boustrophedon fill per room (pitch, minimum radius, offset); route graph connecting rooms to a collector (corridors).
3. Integrate with u/v snapshot: in 10_rd_to_streamlines use φ = u or v (or combination) and export DXF/SVG.
4. Experiment 11: multi-room domain (GeoJSON), serpentine per room + collector.

## Criteria

- Trajectories do not leave the domain (validity tests).
- Minimum separation between lines respected where specified.
- DXF export with layers per room/collector/routes.
