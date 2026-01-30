# Cursor: núcleo Turing (reacción–difusión)

## Objetivo

Implementar y validar el núcleo numérico del paper de Turing: modelos RD, solver 2D y análisis de estabilidad lineal.

## Tareas

1. **rd_models.py**: Gray-Scott, Schnakenberg, Brusselator con `reaction(u, v, params)` y equilibrio homogéneo (u0, v0) cuando aplique.
2. **rd_solvers.py**: Laplaciano 5-point, Neumann/Dirichlet, Euler explícito + opción RK2, semilla reproducible.
3. **stability.py**: Dado (u0, v0) y parámetros, Jacobiano J; para un rango de k, autovalores de (J − k² D); devolver k que maximiza Re(λ).
4. Experimentos 01–03: cada modelo genera snapshots PNG y arrays; documentar parámetros en cabecera del script.

## Criterios

- Solver no produce NaNs en runs típicos (tests de sanidad).
- stability devuelve un k numérico (no simbólico) y forma coherente con la teoría (modo dominante).
