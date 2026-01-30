# morphogenesis-lab

Laboratory repository for **Turing-style reaction–diffusion** and CAD geometry generation from patterns: numerical validation of the core of Turing (1952), trajectory extraction (streamlines, serpentine), and export to DXF/SVG.

## What this repository is

- **Numerical reproduction and validation** of the central mechanism of Turing (1952): reaction–diffusion systems and pattern formation via **homogeneous equilibrium instability** (linearization + nonlinear simulation), in 2D.
- **Pipeline to CAD**: convert patterns/fields into useful geometry: machining-like paths, pipes, or underfloor heating within 2D domains (floor plans), with a view to 3D (surfaces, slabs).
- **Designed for LLM iteration** (GPT, Cursor): reproducible experiments, metrics, and “paper → prototype” workflow.

The connection with Turing’s paper is conceptual and mathematical: we use the same framework (reaction–diffusion PDE, linearization around equilibrium, diffusion that destabilizes and selects a wavelength). We do not copy literal text; see [docs/01_turing_summary.md](docs/01_turing_summary.md).

---

## What it reproduces from Turing

- **Model**: two species (u, v) with nonlinear reaction and diffusion (coefficients Du, Dv). Equations of the form  
  `∂u/∂t = Du ∇²u + f(u,v)`, `∂v/∂t = Dv ∇²v + g(u,v)`.
- **Homogeneous equilibrium instability**: linearization at (u₀, v₀); for each spatial mode k, the linear operator `J - k² D` is studied. Under certain parameters, diffusion destabilizes the equilibrium and a **dominant mode** appears (k that maximizes Re(λ)).
- **Nonlinear simulation**: temporal integration on a 2D grid (5-point FD) to observe “standing wave” patterns (spots, stripes, etc.).

We implement **Gray-Scott**, **Schnakenberg**, and **Brusselator** as standard models and a **linear stability** module to estimate the dominant mode without simulating.

---

## Installation

### With Conda (recommended)

```bash
cd morphogenesis-lab
conda env create -f environment.yml
conda activate morphogenesis-lab
pip install -e .
```

### With venv

```bash
cd morphogenesis-lab
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

---

## How to run experiments

```bash
# 2D patterns (Gray-Scott, Schnakenberg, Brusselator)
python experiments/01_gray_scott_2d.py
python experiments/02_schnakenberg_2d.py
python experiments/03_brusselator_2d.py

# RD pattern → streamlines → DXF/SVG
python experiments/10_rd_to_streamlines.py

# Serpentine per room + collector (multi-room domain)
python experiments/11_rd_to_serpentine_rooms.py

# Direct DXF export
python experiments/12_export_dxf.py
```

Results are written to `data/outputs/patterns/`, `data/outputs/paths/`, and `data/outputs/exports/`.

---

## Outputs it produces

- **Pattern images**: PNG snapshots of u/v (and optional colormap) in `data/outputs/patterns/`.
- **Arrays**: numpy (`.npy`) or similar for reproduction or post-processing.
- **Trajectories**: polylines (streamlines or serpentine) exported to **DXF** (layers per room/collector/routes) and **SVG** for quick inspection in `data/outputs/exports/`.

---

## Roadmap by milestones

| Milestone | Description |
|-----------|-------------|
| **1** | Reproducible stable 2D patterns (Gray-Scott, Schnakenberg, Brusselator) and validation with linear stability analysis. |
| **2** | Trajectory extraction: scalar field → vector field → streamlines with minimum separation and domain clipping; DXF/SVG export. |
| **3** | Multi-room with collector: domain by rooms (GeoJSON), serpentine per room and route graph to collector. |
| **4** | Jump to 3D: surfaces, slabs, and mesh export (STL/STEP) for future integration in FreeCAD/LignumBIM. |

---

## First 3 commands to get started

```bash
conda activate morphogenesis-lab
python experiments/00_smoke_test.py
python experiments/01_gray_scott_2d.py
```

Then check `data/outputs/patterns/` for pattern PNGs.

---

## What to look at in the outputs

- **`data/outputs/patterns/`**: PNGs of u/v at different times; check for no numerical blow-up (finite values) and stable pattern.
- **`data/outputs/paths/`**: intermediate geometries (point lists) if saved.
- **`data/outputs/exports/`**: DXF and SVG; open in a viewer or CAD to check layers, length, and that lines stay inside the domain.

---

## Next steps for FreeCAD/LignumBIM integration (future)

- Import DXF in FreeCAD as sketch or 2D geometry and extrude/sweep for pipes or slabs.
- Define layer conventions (room, collector, routes) compatible with BIM workflows.
- Export 3D meshes (STL) or STEP from `mesh_export` for structural analysis or fabrication.

---

## Documentation

- [docs/00_context.md](docs/00_context.md) — Project context.
- [docs/01_turing_summary.md](docs/01_turing_summary.md) — Technical summary of Turing’s paper and reusable ideas.
- [docs/02_math_model.md](docs/02_math_model.md) — Mathematical model.
- [docs/03_numerics.md](docs/03_numerics.md) — Discretization and solvers.
- [docs/04_cad_pipeline.md](docs/04_cad_pipeline.md) — Reaction–diffusion → CAD pipeline and evaluation criteria.
- [docs/05_experiments.md](docs/05_experiments.md) — Experiment description.
- [docs/06_results_log.md](docs/06_results_log.md) — Results log.

---

## License

MIT. See [LICENSE](LICENSE).

## Cite

See [CITATION.cff](CITATION.cff). For the original paper: Turing, A. M. (1952). The chemical basis of morphogenesis. *Philosophical Transactions of the Royal Society of London B*, 237(641), 37–72.
