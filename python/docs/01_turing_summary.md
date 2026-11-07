# Technical summary of Turing (1952)

This document summarizes the central ideas of **“The chemical basis of morphogenesis”** (Turing, 1952). The repository uses the paper as conceptual and mathematical inspiration; no literal text is copied.

## Summary in 1–2 pages

Turing proposed that spatial patterns in biological systems (e.g. spots, stripes) can arise from **instability of a homogeneous equilibrium** in a reaction–diffusion system with two (or more) morphogens. The key idea: in a reaction-only system, the homogeneous equilibrium can be stable; when **diffusion with different coefficients** for each species is added, the linear operator governing perturbations can become unstable for certain spatial modes. Thus diffusion “destabilizes” the uniform state and selects a **wavelength** (or dominant mode) that gives rise to the pattern.

- **Model**: Reaction–diffusion PDE for two concentrations u, v:
  - ∂u/∂t = D_u ∇²u + f(u,v)
  - ∂v/∂t = D_v ∇²v + g(u,v)
  with f, g nonlinear.

- **Homogeneous equilibrium**: (u₀, v₀) such that f(u₀,v₀)=0, g(u₀,v₀)=0.

- **Linearization**: Perturb (u,v) = (u₀,v₀) + (δu, δv). In Fourier space (mode e^{ik·x}), the growth of the perturbation is governed by the eigenvalues of the matrix **J − k² D**, where J is the Jacobian of (f,g) at (u₀,v₀) and D = diag(D_u, D_v). If for some k ≠ 0 the real part of an eigenvalue is > 0, the homogeneous equilibrium is unstable to that mode.

- **Dominant mode**: The k (or wavelength) that maximizes Re(λ) grows fastest and typically sets the scale of the pattern (“standing waves” in 2D).

- **Nonlinear simulation**: Integrating the PDEs in 2D with suitable boundary conditions yields patterns (spots, stripes, etc.) consistent with linear analysis.

## Reusable ideas in this repo

| Idea | Use in repo |
|------|-------------|
| Reaction–diffusion model (PDE) | Gray-Scott, Schnakenberg, Brusselator in `rd_models.py`; 2D solver in `rd_solvers.py`. |
| Linearization around equilibrium and instability criterion (dominant mode/wavelength) | `stability.py`: numerical computation of eigenvalues of (J − k² D) and search for dominant k. |
| Interpretation of patterns as “standing waves” and 2D generalization | 2D patterns on a regular grid; snapshots and scale analysis. |

## What we do NOT copy and what we adapt

- **We do not copy**: long literal text from the paper; formal proofs; Turing’s exact notation.
- **We adapt to engineering/CAD**: the fields u/v (or functions of them) are used as **scalar fields** to derive trajectories (streamlines, isocontours) and generate geometry (DXF/SVG polylines) for pipes, underfloor heating, etc. The linear stability criterion is used to choose parameters and pattern scale before simulating.

## Reference

Turing, A. M. (1952). The chemical basis of morphogenesis. *Philosophical Transactions of the Royal Society of London B*, 237(641), 37–72. DOI: 10.1098/rstb.1952.0012.
