# Cursor: bootstrap del repo morphogenesis-lab

## Objetivo

Inicializar el repositorio morphogenesis-lab con estructura, dependencias y núcleo Python para reacción–difusión (Turing) y pipeline hacia CAD.

## Tareas

1. Crear estructura de carpetas: `src/morphogenesis/`, `experiments/`, `data/outputs/`, `docs/`, `matlab/`, `tests/`, `notebooks/`.
2. Añadir `environment.yml`, `requirements.txt`, `pyproject.toml` (ruff, black, mypy opcional).
3. Implementar módulos mínimos: `rd_models.py` (Gray-Scott, Schnakenberg, Brusselator), `rd_solvers.py` (FD 5-point, Euler/RK2), `stability.py` (autovalores J − k² D, modo dominante).
4. Añadir experimento smoke test y uno de patrón 2D (p. ej. Gray-Scott) que guarde PNG en `data/outputs/patterns/`.

## Criterios de éxito

- `pip install -e .` y `python experiments/00_smoke_test.py` pasan.
- Un experimento de patrón genera al menos un PNG en `data/outputs/patterns/`.
