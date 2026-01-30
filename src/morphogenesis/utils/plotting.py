"""Plotting helpers for patterns and paths."""

from __future__ import annotations

from pathlib import Path
from typing import Optional, List, Sequence, Tuple

import numpy as np
import matplotlib.pyplot as plt


def plot_pattern(
    u: np.ndarray,
    v: np.ndarray,
    filepath: Optional[str | Path] = None,
    title: str = "Pattern",
    cmap: str = "viridis",
) -> None:
    """Plot u and v as two subplots; save to filepath if provided."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    im1 = ax1.imshow(u, cmap=cmap, origin="lower")
    ax1.set_title("u")
    plt.colorbar(im1, ax=ax1)
    im2 = ax2.imshow(v, cmap=cmap, origin="lower")
    ax2.set_title("v")
    plt.colorbar(im2, ax=ax2)
    fig.suptitle(title)
    plt.tight_layout()
    if filepath:
        plt.savefig(filepath, dpi=150)
        plt.close()
    else:
        plt.show()


def plot_polylines(
    polylines: List[Sequence[Tuple[float, float]]],
    filepath: Optional[str | Path] = None,
    title: str = "Paths",
) -> None:
    """Plot polylines in xy."""
    fig, ax = plt.subplots(figsize=(8, 8))
    for pl in polylines:
        if len(pl) < 2:
            continue
        xs = [p[0] for p in pl]
        ys = [p[1] for p in pl]
        ax.plot(xs, ys, "b-", linewidth=0.8)
    ax.set_aspect("equal")
    ax.set_title(title)
    if filepath:
        plt.savefig(filepath, dpi=150)
        plt.close()
    else:
        plt.show()
