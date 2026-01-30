# Experiment description

## Smoke test

- **`experiments/00_smoke_test.py`**: Imports the package, runs a short simulation (few steps), and checks for no NaNs. Used to validate installation.

## 2D patterns

- **`01_gray_scott_2d.py`**: Gray-Scott on a 2D grid; parameters for a stable pattern; saves PNG snapshots and arrays in `data/outputs/patterns/`.
- **`02_schnakenberg_2d.py`**: Schnakenberg; same.
- **`03_brusselator_2d.py`**: Brusselator; same.

## RD → trajectories pipeline

- **`10_rd_to_streamlines.py`**: Loads a u/v snapshot (or generates one), builds φ, derives vector field, generates streamlines inside a polygon (Shapely), exports DXF and SVG to `data/outputs/exports/`.
- **`11_rd_to_serpentine_rooms.py`**: Multi-room domain (e.g. from `data/domains/simple_rooms.geojson`); generates serpentine per room and route graph to collector; exports DXF/SVG with layers per room/collector/routes.
- **`12_export_dxf.py`**: Direct DXF export test (example polylines or output from 10/11) with layers.

## Reproducibility

- Fixed seeds (numpy.random.seed) where applicable.
- Parameters in script header or in `config.py` so they can be varied from a single place.
- Basic logging and output paths in `data/outputs/`.
