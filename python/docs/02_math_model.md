# Mathematical model

## Reaction–diffusion PDE (2 species)

In spatial domain Ω (2D) and time t:

- ∂u/∂t = D_u ∇²u + f(u, v)
- ∂v/∂t = D_v ∇²v + g(u, v)

with:
- u, v: concentrations (scalar fields).
- D_u, D_v: diffusion coefficients (constants).
- f, g: reaction terms (nonlinear).

## Homogeneous equilibrium

Point (u₀, v₀) such that f(u₀, v₀) = 0 and g(u₀, v₀) = 0. In Turing’s paper, the stability of this equilibrium is analyzed by linearizing and studying spatial modes.

## Linearization and modes

Perturbation (δu, δv) = (U, V) e^{i k·x + λ t}. Substituting into the linearized PDEs yields the eigenvalue problem:

- (J − k² D) (U, V)^T = λ (U, V)^T

with J = Jacobian of (f,g) at (u₀,v₀) and D = diag(D_u, D_v). If there exists k ≠ 0 with Re(λ) > 0, the homogeneous equilibrium is unstable; the k that maximizes Re(λ) is the dominant mode.

## Implemented models

- **Gray-Scott**: f = −uv² + F(1−u), g = uv² − (F+k)v. Parameters F, k.
- **Schnakenberg**: f = a − u + u²v, g = b − u²v. Homogeneous equilibrium (u₀,v₀) in terms of a, b.
- **Brusselator**: f = a − (b+1)u + u²v, g = bu − u²v. Equilibrium (a, b/a); parameters a, b.

Details of equilibria and Jacobians in `src/morphogenesis/rd_models.py` and in the notes `papers/notes/turing_key_equations.md`.
