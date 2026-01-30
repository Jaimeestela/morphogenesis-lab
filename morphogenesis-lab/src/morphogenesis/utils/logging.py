"""Logging setup."""

from __future__ import annotations

import logging
import sys
from typing import Optional


def setup_logging(
    level: int = logging.INFO,
    stream: Optional[object] = None,
) -> None:
    """Configure root logger for morphogenesis."""
    stream = stream or sys.stderr
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=stream,
    )
