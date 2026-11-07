"""
2D reaction-diffusion solver: 5-point Laplacian, Euler/RK2, Neumann/Dirichlet BC.
"""

from __future__ import annotations

import logging
import numpy as np
from typing import Tuple, Dict, Any, Optional

from morphogenesis.grids import laplacian_5point, laplacian_5point_dirichlet
from morphogenesis.rd_models import reaction

logger = logging.getLogger(__name__)


def step_euler(
    u: np.ndarray,
    v: np.ndarray,
    model: str,
    params: Dict[str, Any],
    dx: float,
    dy: float,
    dt: float,
    bc: str = "neumann",
    u_bc: float = 0.0,
    v_bc: float = 0.0,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    One explicit Euler step: u_new = u + dt*(Du*Lap(u) + f), same for v.
    bc: "neumann" or "dirichlet". For dirichlet, u_bc, v_bc are boundary values.
    """
    Du = params["Du"]
    Dv = params["Dv"]
    if bc == "dirichlet":
        lap_u = laplacian_5point_dirichlet(u, dx, dy, u_bc)
        lap_v = laplacian_5point_dirichlet(v, dx, dy, v_bc)
    else:
        lap_u = laplacian_5point(u, dx, dy)
        lap_v = laplacian_5point(v, dx, dy)
    f, g = reaction(model, u, v, params)
    u_new = u + dt * (Du * lap_u + f)
    v_new = v + dt * (Dv * lap_v + g)
    return u_new, v_new


def step_rk2(
    u: np.ndarray,
    v: np.ndarray,
    model: str,
    params: Dict[str, Any],
    dx: float,
    dy: float,
    dt: float,
    bc: str = "neumann",
    u_bc: float = 0.0,
    v_bc: float = 0.0,
) -> Tuple[np.ndarray, np.ndarray]:
    """RK2 (midpoint): k1 = rhs(u,v), u_mid = u + dt/2*k1, k2 = rhs(u_mid), u_new = u + dt*k2."""
    u_mid, v_mid = step_euler(u, v, model, params, dx, dy, dt * 0.5, bc, u_bc, v_bc)
    u_step, v_step = step_euler(u_mid, v_mid, model, params, dx, dy, dt, bc, u_bc, v_bc)
    u_new = u + (u_step - u_mid)
    v_new = v + (v_step - v_mid)
    return u_new, v_new


def initial_condition(
    ny: int,
    nx: int,
    u0: float,
    v0: float,
    noise_amplitude: float = 0.01,
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """Perturbation around homogeneous equilibrium (u0, v0) with reproducible noise."""
    rng = np.random.default_rng(seed)
    u = u0 + noise_amplitude * (rng.random((ny, nx)) - 0.5)
    v = v0 + noise_amplitude * (rng.random((ny, nx)) - 0.5)
    return u, v


def solve_2d(
    model: str,
    params: Dict[str, Any],
    nx: int,
    ny: int,
    dx: float = 1.0,
    dy: float | None = None,
    dt: float = 0.5,
    n_steps: int = 1000,
    bc: str = "neumann",
    integrator: str = "euler",
    seed: Optional[int] = None,
    noise_amplitude: float = 0.01,
    u_bc: float = 0.0,
    v_bc: float = 0.0,
    snapshot_every: Optional[int] = None,
) -> Tuple[np.ndarray, np.ndarray, list]:
    """
    Run 2D RD simulation. Returns (u_final, v_final, list of (step, u, v) snapshots if snapshot_every set).
    """
    from morphogenesis.rd_models import equilibrium

    dy = dy if dy is not None else dx
    u0, v0 = equilibrium(model, params)
    u, v = initial_condition(ny, nx, u0, v0, noise_amplitude, seed)
    step_fn = step_rk2 if integrator == "rk2" else step_euler
    snapshots: list = []

    for step in range(n_steps):
        u, v = step_fn(u, v, model, params, dx, dy, dt, bc, u_bc, v_bc)
        if np.any(~np.isfinite(u)) or np.any(~np.isfinite(v)):
            logger.warning("Non-finite values at step %d", step)
            break
        if snapshot_every and (step + 1) % snapshot_every == 0:
            snapshots.append((step + 1, u.copy(), v.copy()))

    return u, v, snapshots
