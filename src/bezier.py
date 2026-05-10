"""Elementary cubic Bezier curve utilities.

This file is assigned to Person 2.
"""

from __future__ import annotations

from typing import Iterable

import numpy as np
import matplotlib.pyplot as plt

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
    t = np.linspace(0.0, 1.0, n)
    p0, p1, p2, p3 = np.array(P0), np.array(P1), np.array(P2), np.array(P3)

    curve = (
        np.outer((1 - t) ** 3, p0)
        + np.outer(3 * (1 - t) ** 2 * t, p1)
        + np.outer(3 * (1 - t) * t ** 2, p2)
        + np.outer(t ** 3, p3)
    )
    return curve  # shape (n, 2)


def bezier_coefficients(P0: Point, P1: Point, P2: Point, P3: Point) -> tuple[np.ndarray, np.ndarray]:
    """Return polynomial coefficients (a, b, c, d) for both axes.

    Coefficient form:
        x(t) = ax*t^3 + bx*t^2 + cx*t + dx
        y(t) = ay*t^3 + by*t^2 + cy*t + dy

    Returns:
        coeff_x: array [ax, bx, cx, dx]
        coeff_y: array [ay, by, cy, dy]
    """
    x0, y0 = P0
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3

    coeff_x = np.array([
        -x0 + 3 * x1 - 3 * x2 + x3,   # ax
         3 * x0 - 6 * x1 + 3 * x2,     # bx
        -3 * x0 + 3 * x1,              # cx
         x0,                           # dx
    ])
    coeff_y = np.array([
        -y0 + 3 * y1 - 3 * y2 + y3,
         3 * y0 - 6 * y1 + 3 * y2,
        -3 * y0 + 3 * y1,
         y0,
    ])
    return coeff_x, coeff_y


def plot_elementary_curve(
    curve_points: np.ndarray,
    control_points: Iterable[Point],
    save_path: str,
) -> None:
    """Plot and save an elementary cubic Bezier curve.

    The plot includes:
    - the curve itself;
    - support and control points;
    - the control polygon.
    """
    ctrl = list(control_points)
    cx = [p[0] for p in ctrl]
    cy = [p[1] for p in ctrl]
    labels = ["P0", "P1", "P2", "P3"]
    label_offsets = [(-0.25, -0.15), (-0.25, 0.10), (0.10, 0.10), (0.10, -0.15)]

    fig, ax = plt.subplots(figsize=(8, 6))

    # Control polygon
    ax.plot(cx, cy, color="gray", linestyle="--", linewidth=1.2, label="Контрольный многоугольник")

    # Bezier curve
    ax.plot(curve_points[:, 0], curve_points[:, 1], color="#1f77b4", linewidth=2.5, label="Кривая Безье")

    # Support points P0, P3
    ax.plot([cx[0], cx[3]], [cy[0], cy[3]], "go", markersize=9, label="Опорные точки (P0, P3)")

    # Control points P1, P2
    ax.plot([cx[1], cx[2]], [cy[1], cy[2]], "r^", markersize=9, label="Управляющие точки (P1, P2)")

    for i, (px, py) in enumerate(zip(cx, cy)):
        dx, dy = label_offsets[i]
        ax.annotate(labels[i], xy=(px, py), xytext=(px + dx, py + dy), fontsize=12, fontweight="bold")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Элементарная кубическая кривая Безье\n(задание 3.1)", fontsize=13)
    ax.legend()
    ax.grid(True, alpha=0.4)
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"Изображение сохранено: {save_path}")
