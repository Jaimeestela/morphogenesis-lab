"""
Regular 2D grids for reaction-diffusion and field operations.
"""

from __future__ import annotations

import numpy as np
from typing import Tuple


def make_xy(
    nx: int,
    ny: int,
    dx: float = 1.0,
    dy: float | None = None,
    origin: Tuple[float, float] = (0.0, 0.0),
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Build 1D coordinate arrays and optionally 2D meshes for a regular grid.

    Returns:
        x_1d, y_1d: 1D arrays of cell-centered coordinates.
        If origin is (ox, oy): x = ox + (0.5 + i)*dx for i in 0..nx-1.
    """
    dy = dy if dy is not None else dx
    ox, oy = origin
    x_1d = ox + (np.arange(nx) + 0.5) * dx
    y_1d = oy + (np.arange(ny) + 0.5) * dy
    return x_1d, y_1d


def meshgrid_2d(
    nx: int,
    ny: int,
    dx: float = 1.0,
    dy: float | None = None,
    origin: Tuple[float, float] = (0.0, 0.0),
) -> Tuple[np.ndarray, np.ndarray]:
    """Return (X, Y) 2D arrays of shape (ny, nx) for the grid."""
    x_1d, y_1d = make_xy(nx, ny, dx, dy, origin)
    X, Y = np.meshgrid(x_1d, y_1d, indexing="xy")
    return X, Y


def laplacian_5point(
    u: np.ndarray,
    dx: float = 1.0,
    dy: float | None = None,
) -> np.ndarray:
    """
    Five-point Laplacian on a 2D array (ny, nx).
    Interior: (u[i+1,j] + u[i-1,j] + u[i,j+1] + u[i,j-1] - 4*u[i,j]) / h^2.
    Assumes Neumann (zero normal derivative) at boundaries: ghost cell = interior.
    """
    dy = dy if dy is not None else dx
    out = np.empty_like(u)
    ny, nx = u.shape
    # Interior
    out[1 : ny - 1, 1 : nx - 1] = (
        u[2:, 1 : nx - 1]
        + u[: ny - 2, 1 : nx - 1]
        + u[1 : ny - 1, 2:]
        + u[1 : ny - 1, : nx - 2]
        - 4.0 * u[1 : ny - 1, 1 : nx - 1]
    ) / (dx * dy)
    # Neumann BC: extend interior gradient to boundary (same as interior Laplacian at edge)
    out[0, :] = out[1, :]
    out[ny - 1, :] = out[ny - 2, :]
    out[:, 0] = out[:, 1]
    out[:, nx - 1] = out[:, nx - 2]
    return out


def laplacian_5point_dirichlet(
    u: np.ndarray,
    dx: float = 1.0,
    dy: float | None = None,
    u_bc: float = 0.0,
) -> np.ndarray:
    """
    Five-point Laplacian with Dirichlet BC: boundary values fixed to u_bc.
    """
    dy = dy if dy is not None else dx
    out = np.empty_like(u)
    ny, nx = u.shape
    out[1 : ny - 1, 1 : nx - 1] = (
        u[2:, 1 : nx - 1]
        + u[: ny - 2, 1 : nx - 1]
        + u[1 : ny - 1, 2:]
        + u[1 : ny - 1, : nx - 2]
        - 4.0 * u[1 : ny - 1, 1 : nx - 1]
    ) / (dx * dy)
    # Dirichlet: use boundary value in stencil (ghost = u_bc)
    out[0, :] = (u[1, :] + u_bc + u[0, 1:] + u[0, : nx - 1] - 4 * u[0, :]) / (dx * dy)
    out[ny - 1, :] = (
        u_bc + u[ny - 2, :] + u[ny - 1, 1:] + u[ny - 1, : nx - 1] - 4 * u[ny - 1, :]
    ) / (dx * dy)
    out[:, 0] = (u[1:, 0] + u[: ny - 1, 0] + u[:, 1] + u_bc - 4 * u[:, 0]) / (dx * dy)
    out[:, nx - 1] = (
        u[1:, nx - 1] + u[: ny - 1, nx - 1] + u_bc + u[:, nx - 2] - 4 * u[:, nx - 1]
    ) / (dx * dy)
    return out
