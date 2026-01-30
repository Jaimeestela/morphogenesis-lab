# Contexto del proyecto

## Objetivo

Este repositorio (**morphogenesis-lab**) tiene dos ejes:

1. **Validación numérica del núcleo del paper de Turing (1952)**  
   Reproducir y verificar en 2D: sistemas reacción–difusión, linealización en torno al equilibrio homogéneo, y formación de patrón por inestabilidad (modo dominante). No se copia texto literal del paper; se usa como inspiración conceptual y matemática.

2. **Pipeline hacia geometría CAD**  
   Convertir patrones/campos en trayectorias útiles: streamlines (tipo tuberías/mecanizado) y serpentine (suelo radiante) dentro de dominios 2D (plantas), con export a DXF/SVG y preparación para 3D.

## Público

- Desarrolladores e investigadores que quieran iterar con LLMs (GPT, Cursor) en experimentos reproducibles.
- Quienes necesiten un baseline numérico (Python + MATLAB opcional) para estabilidad y solvers, y un pipeline claro “patrón → trayectorias → CAD”.

## Stack

- **Python**: numpy, scipy, numba, matplotlib, shapely, scikit-image, networkx; opcional trimesh, pyvista.
- **MATLAB**: prototipado rápido de PDE (FD/FE) y análisis espectral para validación cruzada.
- **LLM workflow**: prompts versionados en `docs/prompts/`, guías para Cursor/GPT.

## Convenciones

- Entornos: conda (recomendado) o venv; `environment.yml` y `requirements.txt`.
- Código con docstrings y typing; ruff + black (+ mypy opcional).
- Outputs en `data/outputs/`; experimentos reproducibles como scripts en `experiments/`.
