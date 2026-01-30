# MATLAB scripts (validation and prototyping)

## When to use MATLAB

1. **Validate stability and dominant mode** quickly: sweep k and eigenvalues of (J − k² D) without depending on the Python solver.
2. **Check that the Python solver does not invent dynamics**: compare snapshots or temporal evolution with an FD implementation in MATLAB.
3. **Prototype discretization variants**: try schemes (FD, FE) or boundary conditions before porting to Python.

## Files

- **rd_fd_2d.m**: Basic 2D FD simulation (5-point Laplacian, explicit Euler) for a model (e.g. Gray-Scott or Schnakenberg).
- **rd_stability_linear.m**: Computation of eigenvalues of (J − k² D) for a range of k; returns the k that maximizes Re(λ).
- **rd_demo_patterns.m**: Demo script that calls rd_fd_2d and optionally rd_stability_linear, and saves figures.

## How to run

From MATLAB, in the `matlab/` directory:

```matlab
rd_stability_linear   % k sweep and dominant mode
rd_fd_2d             % one FD 2D run
rd_demo_patterns     % full demo
```

## Cross-validation with Python

- Compare the dominant `k` returned by `rd_stability_linear.m` with `morphogenesis.stability.dominant_mode()`.
- Compare a (u,v) snapshot from `rd_fd_2d.m` with that from `experiments/01_gray_scott_2d.py` (same parameters and seed if applicable).
