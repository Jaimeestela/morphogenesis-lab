# Pipeline to CAD

## Main idea

**Reaction–diffusion → scalar field → vector field → streamlines → CAD curves**

1. **Reaction–diffusion**: A model (Gray-Scott, Schnakenberg, Brusselator) is simulated in 2D and fields u(x,y), v(x,y) are obtained at a snapshot.
2. **Scalar field**: φ is defined from u/v (e.g. φ = u, φ = v, or φ = u−v, etc.) on the grid.
3. **Vector field**: **∇φ** (gradient) or a rotated field (e.g. perpendicular to follow isocontours) is computed on the grid; interpolated if needed at arbitrary points.
4. **Streamlines**: Flow lines of the vector field are integrated with fixed step and minimum separation between lines; **clipping** to the domain (Shapely polygon) and obstacles (holes) are respected.
5. **CAD curves**: The resulting polylines are exported to **DXF** (layers per room/collector/routes) and **SVG** for inspection.

This yields “pipe-like” or machining trajectories that follow the pattern structure.

## Alternative: deterministic planner (serpentine)

**Serpentine / boustrophedon per room → connections to collector**

- For each room (polygon): fill with a serpentine pattern (back and forth) with pitch and minimum radius of curvature set.
- Rooms are connected to each other and to a **collector** via a route graph (corridors). This gives a “circuit” per room plus a connection tree to the collector.
- This baseline is **deterministic** and does not depend on the RD pattern; it is used to compare quality (length, coverage, crossings) with the streamline-based approach.

## Evaluation criteria

To compare and validate trajectories (streamlines vs serpentine, or different seeds/parameters):

| Criterion | Description |
|-----------|-------------|
| **Total length** | Sum of lengths of all polylines (per room and collector). |
| **Coverage uniformity** | Distribution of distances from domain points to nearest polyline (histogram, std). |
| **Minimum radii** | Minimum radius of curvature at bends; must respect a threshold (e.g. for pipes). |
| **Crossings** | Number of intersections between segments (avoid when possible). |
| **Distance to borders** | Minimum distance of the trajectory to the domain boundary; must be ≥ margin. |
| **Number of loops** | Count of connected components or closed loops; relevant for underfloor heating circuits. |

These criteria are implemented or referenced in `src/morphogenesis/metrics.py` and in the export experiments (DXF/SVG).
