"""Elementary cubic Bezier curve utilities.

This file is assigned to Person 2.
"""

from __future__ import annotations

from typing import Iterable

import numpy as np

Point = tuple[float, float]


def cubic_bezier(P0: Point, P1: Point, P2: Point, P3: Point, n: int = 100) -> np.ndarray:
    """Return points of a cubic Bezier curve.

    Formula:
        B(t) = (1 - t)^3 * P0
             + 3(1 - t)^2 * t * P1
             + 3(1 - t) * t^2 * P2
             + t^3 * P3,
        where 0 <= t <= 1.

    Args:
        P0: start support point.
        P1: first control point.
        P2: second control point.
        P3: end support point.
        n: number of calculated points.

    Returns:
        NumPy array with shape (n, 2).
    """
    # TODO: Person 2 implements this function.
    raise NotImplementedError("Implement cubic Bezier curve calculation.")


def plot_elementary_curve(curve_points: np.ndarray, control_points: Iterable[Point], save_path: str) -> None:
    """Plot and save an elementary cubic Bezier curve.

    The plot should include:
    - curve itself;
    - support and control points;
    - control polygon.
    """
    # TODO: Person 2 implements this function.
    raise NotImplementedError("Implement elementary curve plotting.")
