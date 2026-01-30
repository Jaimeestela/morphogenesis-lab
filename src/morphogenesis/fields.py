"""
Scalar and vector fields derived from reaction-diffusion snapshots.
Used for streamlines: phi from u/v, then grad(phi) or rotated field.
"""

from __future__ import annotations

import numpy as np
from typing import Tuple, Optional
from scipy import ndimage


def scalar_from_uv(
    u: np.ndarray,
    v: np.ndarray,
    mode: str = "u",
) -> np.ndarray:
    """
    Build scalar field phi from u, v.
    mode: "u", "v", or "diff" (u - v).
    """
    if mode == "u":
        return u.copy()
    if mode == "v":
        return v.copy()
    if mode == "diff":
        return u - v
    raise ValueError(f"Unknown mode: {mode}")


def gradient_2d(
    phi: np.ndarray,
    dx: float = 1.0,
    dy: float | None = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gradient of phi on a 2D grid (ny, nx). Central differences in interior.
    Returns (grad_x, grad_y) each of shape (ny, nx).
    """
    dy = dy if dy is not None else dx
    grad_x = np.gradient(phi, dx, axis=1)
    grad_y = np.gradient(phi, dy, axis=0)
    return grad_x, grad_y


def rotated_gradient_2d(
    phi: np.ndarray,
    dx: float = 1.0,
    dy: float | None = None,
    clockwise: bool = True,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Rotate gradient by 90° to get field tangent to isocontours.
    (vx, vy) perpendicular to grad(phi). If clockwise: (vy, -vx) in (x,y).
    Returns (vx, vy) for streamlines following isocontours.
    """
    gx, gy = gradient_2d(phi, dx, dy)
    if clockwise:
        vx = gy
        vy = -gx
    else:
        vx = -gy
        vy = gx
    return vx, vy


def vector_field_at_points(
    vx: np.ndarray,
    vy: np.ndarray,
    x_1d: np.ndarray,
    y_1d: np.ndarray,
    x_pts: np.ndarray,
    y_pts: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Interpolate vector field (vx, vy) defined on grid (x_1d, y_1d) at points (x_pts, y_pts).
    Returns (vx_at_pts, vy_at_pts). Uses scipy.ndimage.map_coordinates (order 1).
    """
    ny, nx = vx.shape
    # map_coordinates uses (row, col) = (y index, x index). Coordinates in pixel units.
    ix = (x_pts - x_1d[0]) / (x_1d[-1] - x_1d[0]) * (nx - 1) if nx > 1 else np.zeros_like(x_pts)
    iy = (y_pts - y_1d[0]) / (y_1d[-1] - y_1d[0]) * (ny - 1) if ny > 1 else np.zeros_like(y_pts)
    coords = np.array([iy, ix])
    vx_at = ndimage.map_coordinates(vx, coords, order=1, mode="nearest")
    vy_at = ndimage.map_coordinates(vy, coords, order=1, mode="nearest")
    return vx_at, vy_at


def smooth_scalar(
    phi: np.ndarray,
    sigma: float = 1.0,
) -> np.ndarray:
    """Gaussian smooth phi (e.g. to reduce noise before taking gradient)."""
    return ndimage.gaussian_filter(phi, sigma=sigma, mode="nearest")
