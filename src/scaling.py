"""Scaling and visualization utilities.

This file is assigned to Person 4.
"""

from __future__ import annotations

import numpy as np

from .bezier import Point


import matplotlib.pyplot as plt

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
    c = np.array(center)
    return c + k * (points - c)


def plot_scaled_curve(points: np.ndarray, scale: float, save_path: str) -> None:
    """Plot and save one scaled curve version."""
    plt.figure(figsize=(8, 8))
    plt.plot(points[:, 0], points[:, 1], 'r-', label=f'Масштаб {scale}')
    plt.title(f'Стилизованное пламя (масштаб {scale})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.savefig(save_path)
    plt.close()
