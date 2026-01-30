# Key equations (inspired by Turing 1952)

Summary of the equations and relations used in the repo. Not literal copy of the paper; an adaptation for numerical implementation.

## Reaction–diffusion PDE

- ∂u/∂t = D_u ∇²u + f(u,v)
- ∂v/∂t = D_v ∇²v + g(u,v)

## Gray-Scott

- f = −uv² + F(1−u),  g = uv² − (F+k)v
- Parameters: F, k, D_u, D_v
- Trivial homogeneous equilibrium: (1, 0). Other equilibria and patterns depend on F, k.

## Schnakenberg

- f = a − u + u²v,  g = b − u²v
- Equilibrium: u₀ = a + b, v₀ = b / (a+b)²
- Jacobian at (u₀,v₀): J_11 = −1 + 2u₀v₀, J_12 = u₀², J_21 = −2u₀v₀, J_22 = −u₀²

## Brusselator

- f = a − (b+1)u + u²v,  g = bu − u²v
- Equilibrium: (u₀, v₀) = (a, b/a)
- Jacobian: J_11 = b−1, J_12 = a², J_21 = −b, J_22 = −a²

## Linear stability (mode k)

- Matrix: M = J − k² D,  D = diag(D_u, D_v)
- Eigenvalues λ of M: if Re(λ) > 0 for some k ≠ 0, homogeneous equilibrium is unstable.
- Dominant mode: k that maximizes Re(λ).

Numerical implementation: `src/morphogenesis/rd_models.py`, `stability.py`.
