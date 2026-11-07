# Project context

## Objective

This repository (**morphogenesis-lab**) has two main axes:

1. **Numerical validation of the core of Turing (1952)**  
   Reproduce and verify in 2D: reaction–diffusion systems, linearization around homogeneous equilibrium, and pattern formation by instability (dominant mode). No literal text is copied from the paper; it is used as conceptual and mathematical inspiration.

2. **Pipeline to CAD geometry**  
   Convert patterns/fields into useful trajectories: streamlines (pipe/machining-like) and serpentine (underfloor heating) within 2D domains (floor plans), with export to DXF/SVG and preparation for 3D.

## Audience

- Developers and researchers who want to iterate with LLMs (GPT, Cursor) on reproducible experiments.
- Those who need a numerical baseline (Python + optional MATLAB) for stability and solvers, and a clear “pattern → trajectories → CAD” pipeline.

## Stack

- **Python**: numpy, scipy, numba, matplotlib, shapely, scikit-image, networkx; optional trimesh, pyvista.
- **MATLAB**: quick PDE prototyping (FD/FE) and spectral analysis for cross-validation.
- **LLM workflow**: versioned prompts in `docs/prompts/`, guides for Cursor/GPT.

## Conventions

- Environments: conda (recommended) or venv; `environment.yml` and `requirements.txt`.
- Code with docstrings and typing; ruff + black (+ optional mypy).
- Outputs in `data/outputs/`; reproducible experiments as scripts in `experiments/`.
