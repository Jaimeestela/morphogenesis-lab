"""
Reaction-diffusion models: Gray-Scott, Schnakenberg, Brusselator.
Each model provides reaction terms f(u,v), g(u,v) and homogeneous equilibrium (u0,v0) when applicable.
"""

from __future__ import annotations

import numpy as np
from typing import Tuple, Dict, Any


# ---------------------------------------------------------------------------
# Gray-Scott
# ---------------------------------------------------------------------------


def grayscott_reaction(
    u: np.ndarray,
    v: np.ndarray,
    F: float,
    k: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gray-Scott: f = -u*v^2 + F*(1-u), g = u*v^2 - (F+k)*v.
    Parameters: F (feed), k (kill).
    """
    f = -u * v * v + F * (1.0 - u)
    g = u * v * v - (F + k) * v
    return f, g


def grayscott_equilibrium(F: float, k: float) -> Tuple[float, float]:
    """Trivial homogeneous equilibrium: (1, 0). Other equilibria exist for pattern formation."""
    return 1.0, 0.0


def grayscott_jacobian(u0: float, v0: float, F: float, k: float) -> np.ndarray:
    """Jacobian J of (f,g) at (u0,v0). J = [[df/du, df/dv], [dg/du, dg/dv]]."""
    J = np.array(
        [
            [-v0 * v0 - F, -2 * u0 * v0],
            [v0 * v0, 2 * u0 * v0 - (F + k)],
        ]
    )
    return J


# ---------------------------------------------------------------------------
# Schnakenberg
# ---------------------------------------------------------------------------


def schnakenberg_reaction(
    u: np.ndarray,
    v: np.ndarray,
    a: float,
    b: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Schnakenberg: f = a - u + u^2*v, g = b - u^2*v.
    Parameters: a, b.
    """
    f = a - u + u * u * v
    g = b - u * u * v
    return f, g


def schnakenberg_equilibrium(a: float, b: float) -> Tuple[float, float]:
    """Homogeneous equilibrium: u0 = a+b, v0 = b/(a+b)^2."""
    u0 = a + b
    v0 = b / (u0 * u0)
    return u0, v0


def schnakenberg_jacobian(u0: float, v0: float, a: float, b: float) -> np.ndarray:
    """Jacobian at (u0,v0). df/du = -1+2*u0*v0, df/dv = u0^2, dg/du = -2*u0*v0, dg/dv = -u0^2."""
    J = np.array(
        [
            [-1.0 + 2 * u0 * v0, u0 * u0],
            [-2 * u0 * v0, -u0 * u0],
        ]
    )
    return J


# ---------------------------------------------------------------------------
# Brusselator
# ---------------------------------------------------------------------------


def brusselator_reaction(
    u: np.ndarray,
    v: np.ndarray,
    a: float,
    b: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Brusselator: f = a - (b+1)*u + u^2*v, g = b*u - u^2*v.
    Parameters: a, b.
    """
    f = a - (b + 1.0) * u + u * u * v
    g = b * u - u * u * v
    return f, g


def brusselator_equilibrium(a: float, b: float) -> Tuple[float, float]:
    """Homogeneous equilibrium: (u0, v0) = (a, b/a)."""
    return a, b / a


def brusselator_jacobian(u0: float, v0: float, a: float, b: float) -> np.ndarray:
    """Jacobian at (u0,v0)."""
    J = np.array(
        [
            [b - 1.0 + 2 * u0 * v0, u0 * u0],
            [-b - 2 * u0 * v0, -u0 * u0],
        ]
    )
    return J


# ---------------------------------------------------------------------------
# Generic reaction interface
# ---------------------------------------------------------------------------


def reaction(
    model: str,
    u: np.ndarray,
    v: np.ndarray,
    params: Dict[str, Any],
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Dispatch reaction terms for a given model name.
    params must contain model-specific keys (F, k for Gray-Scott; a, b for Schnakenberg/Brusselator).
    """
    if model == "grayscott":
        return grayscott_reaction(u, v, params["F"], params["k"])
    if model == "schnakenberg":
        return schnakenberg_reaction(u, v, params["a"], params["b"])
    if model == "brusselator":
        return brusselator_reaction(u, v, params["a"], params["b"])
    raise ValueError(f"Unknown model: {model}")


def equilibrium(model: str, params: Dict[str, Any]) -> Tuple[float, float]:
    """Homogeneous equilibrium (u0, v0) for the given model and params."""
    if model == "grayscott":
        return grayscott_equilibrium(params["F"], params["k"])
    if model == "schnakenberg":
        return schnakenberg_equilibrium(params["a"], params["b"])
    if model == "brusselator":
        return brusselator_equilibrium(params["a"], params["b"])
    raise ValueError(f"Unknown model: {model}")


def jacobian(
    model: str,
    u0: float,
    v0: float,
    params: Dict[str, Any],
) -> np.ndarray:
    """Jacobian J of (f,g) at (u0,v0) for the given model."""
    if model == "grayscott":
        return grayscott_jacobian(u0, v0, params["F"], params["k"])
    if model == "schnakenberg":
        return schnakenberg_jacobian(u0, v0, params["a"], params["b"])
    if model == "brusselator":
        return brusselator_jacobian(u0, v0, params["a"], params["b"])
    raise ValueError(f"Unknown model: {model}")
