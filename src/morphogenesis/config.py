"""
Configuration and default parameters for morphogenesis-lab.
"""

from pathlib import Path
from typing import Any

# Base paths (relative to repo root when running from repo)
REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"
OUTPUTS_DIR = DATA_DIR / "outputs"
PATTERNS_DIR = OUTPUTS_DIR / "patterns"
PATHS_DIR = OUTPUTS_DIR / "paths"
EXPORTS_DIR = OUTPUTS_DIR / "exports"
DOMAINS_DIR = DATA_DIR / "domains"


def ensure_output_dirs() -> None:
    """Create output directories if they do not exist."""
    for d in (PATTERNS_DIR, PATHS_DIR, EXPORTS_DIR):
        d.mkdir(parents=True, exist_ok=True)


# Default solver
DEFAULT_DX = 1.0
DEFAULT_DT = 0.5
DEFAULT_BC = "neumann"  # "neumann" | "dirichlet"
DEFAULT_INTEGRATOR = "euler"  # "euler" | "rk2"

# Default stability
DEFAULT_K_MIN = 0.0
DEFAULT_K_MAX = 20.0
DEFAULT_K_POINTS = 200


def get_default_grayscott() -> dict[str, Any]:
    """Default Gray-Scott parameters (pattern-forming)."""
    return {
        "F": 0.03,
        "k": 0.062,
        "Du": 0.0002,
        "Dv": 0.0001,
    }


def get_default_schnakenberg() -> dict[str, Any]:
    """Default Schnakenberg parameters."""
    return {
        "a": 0.2,
        "b": 1.0,
        "Du": 0.001,
        "Dv": 0.01,
    }


def get_default_brusselator() -> dict[str, Any]:
    """Default Brusselator parameters."""
    return {
        "a": 1.0,
        "b": 2.5,
        "Du": 0.008,
        "Dv": 0.004,
    }
