# Cursor: Turing core (reaction–diffusion)

## Objective

Implement and validate the numerical core of Turing’s paper: RD models, 2D solver, and linear stability analysis.

## Tasks

1. **rd_models.py**: Gray-Scott, Schnakenberg, Brusselator with `reaction(u, v, params)` and homogeneous equilibrium (u0, v0) when applicable.
2. **rd_solvers.py**: 5-point Laplacian, Neumann/Dirichlet, explicit Euler + RK2 option, reproducible seed.
3. **stability.py**: Given (u0, v0) and parameters, Jacobian J; for a range of k, eigenvalues of (J − k² D); return k that maximizes Re(λ).
4. Experiments 01–03: each model produces PNG snapshots and arrays; document parameters in script header.

## Criteria

- Solver does not produce NaNs in typical runs (sanity tests).
- stability returns a numerical k (not symbolic) and form consistent with theory (dominant mode).
