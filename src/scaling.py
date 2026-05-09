"""Scaling and visualization utilities.

This file is assigned to Person 4.
"""

from __future__ import annotations

import numpy as np

from .bezier import Point


def scale_points(points: np.ndarray, center: Point, k: float) -> np.ndarray:
    """Scale points relative to the selected center.

    Formula:
        P' = C + k * (P - C)

    Args:
        points: source curve points with shape (n, 2).
        center: scaling center C = (xc, yc).
        k: scale coefficient.

    Returns:
        Scaled points with shape (n, 2).
    """
    # TODO: Person 4 implements this function.
    raise NotImplementedError("Implement point scaling.")


def plot_scaled_curve(points: np.ndarray, scale: float, save_path: str) -> None:
    """Plot and save one scaled curve version."""
    # TODO: Person 4 implements this function.
    raise NotImplementedError("Implement scaled curve plotting.")
