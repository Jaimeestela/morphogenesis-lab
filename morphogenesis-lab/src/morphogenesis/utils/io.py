"""I/O for snapshots and arrays."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Tuple

import numpy as np

logger = logging.getLogger(__name__)


def save_snapshot(
    filepath: str | Path,
    u: np.ndarray,
    v: np.ndarray,
) -> None:
    """Save u, v arrays to .npz."""
    np.savez(filepath, u=u, v=v)
    logger.debug("Saved snapshot to %s", filepath)


def load_snapshot(filepath: str | Path) -> Tuple[np.ndarray, np.ndarray]:
    """Load u, v from .npz. Returns (u, v)."""
    data = np.load(filepath)
    return data["u"], data["v"]
