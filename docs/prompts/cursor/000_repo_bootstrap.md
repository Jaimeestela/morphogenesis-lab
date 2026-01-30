# Cursor: morphogenesis-lab repo bootstrap

## Objective

Initialize the morphogenesis-lab repository with structure, dependencies, and core Python for reaction–diffusion (Turing) and pipeline to CAD.

## Tasks

1. Create folder structure: `src/morphogenesis/`, `experiments/`, `data/outputs/`, `docs/`, `matlab/`, `tests/`, `notebooks/`.
2. Add `environment.yml`, `requirements.txt`, `pyproject.toml` (ruff, black, optional mypy).
3. Implement minimal modules: `rd_models.py` (Gray-Scott, Schnakenberg, Brusselator), `rd_solvers.py` (5-point FD, Euler/RK2), `stability.py` (eigenvalues of J − k² D, dominant mode).
4. Add smoke test experiment and one 2D pattern experiment (e.g. Gray-Scott) that saves PNG in `data/outputs/patterns/`.

## Success criteria

- `pip install -e .` and `python experiments/00_smoke_test.py` pass.
- One pattern experiment produces at least one PNG in `data/outputs/patterns/`.
