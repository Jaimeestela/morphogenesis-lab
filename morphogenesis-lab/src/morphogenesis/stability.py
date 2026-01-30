"""
Linear stability analysis: eigenvalues of (J - k^2 D) and dominant mode k.
Connects to Turing's argument: diffusion can destabilize a homogeneous equilibrium.
"""

from __future__ import annotations

import numpy as np
from typing import Tuple, Dict, Any, Optional

from morphogenesis.rd_models import equilibrium, jacobian


def stability_matrix(
    J: np.ndarray,
    k_sq: float,
    Du: float,
    Dv: float,
) -> np.ndarray:
    """
    M = J - k^2 * D, with D = diag(Du, Dv).
    Eigenvalues of M determine linear growth rate for mode k (k^2 = k_sq).
    """
    D = np.array([[Du, 0], [0, Dv]])
    return J - k_sq * D


def max_re_eigenvalue_for_k(
    J: np.ndarray,
    k_sq: float,
    Du: float,
    Dv: float,
) -> float:
    """Maximum real part of eigenvalues of (J - k^2 D)."""
    M = stability_matrix(J, k_sq, Du, Dv)
    w = np.linalg.eigvals(M)
    return float(np.max(w.real))


def dominant_mode(
    model: str,
    params: Dict[str, Any],
    k_min: float = 0.0,
    k_max: float = 20.0,
    n_k: int = 200,
) -> Tuple[float, float, np.ndarray, np.ndarray]:
    """
    Compute the dominant mode k (maximizing Re(lambda)) for the linearized RD system.
    Returns: (k_dominant, lambda_dominant_real, k_arr, re_lambda_arr).
    Uses equilibrium (u0,v0) and Jacobian J from the model.
    """
    u0, v0 = equilibrium(model, params)
    J = jacobian(model, u0, v0, params)
    Du = params["Du"]
    Dv = params["Dv"]

    k_arr = np.linspace(k_min, k_max, n_k)
    k_sq_arr = k_arr ** 2
    re_lambda_arr = np.array(
        [max_re_eigenvalue_for_k(J, k_sq, Du, Dv) for k_sq in k_sq_arr]
    )

    idx = np.argmax(re_lambda_arr)
    k_dominant = float(k_arr[idx])
    lambda_dominant = float(re_lambda_arr[idx])

    return k_dominant, lambda_dominant, k_arr, re_lambda_arr
