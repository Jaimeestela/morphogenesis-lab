# Discretization and solvers

## Grid

- 2D rectangular domain discretized on a regular grid (nx × ny).
- Spacing Δx, Δy (constants).

## Laplacian

- Five-point finite differences:  
  ∇²φ ≈ (φ_{i+1,j} + φ_{i-1,j} + φ_{i,j+1} + φ_{i,j-1} − 4φ_{i,j}) / h²  
  with h = Δx = Δy for a square grid.

## Boundary conditions

- **Neumann (reflecting)**: zero normal derivative; implemented with ghost cells or by updating edges so that flux is zero.
- **Dirichlet**: fixed values on the boundary (e.g. homogeneous equilibrium).

## Temporal integration

- **Explicit Euler**: u^{n+1} = u^n + Δt (D_u L[u^n] + f(u^n,v^n)), same for v. Stability: Δt limited by CFL (diffusion).
- **RK2 (optional)**: intermediate step and averaging for better temporal accuracy.

## Initial seed

- Homogeneous equilibrium + reproducible random perturbation (fixed seed) to break symmetry and trigger instability.

## Output

- Fields u, v at each step (or at intervals); snapshots saved as arrays and/or images (PNG).

Implementation: `src/morphogenesis/rd_solvers.py` and `grids.py`.
