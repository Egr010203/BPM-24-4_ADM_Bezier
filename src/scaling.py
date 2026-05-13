"""Scaling and visualization utilities.

This file is assigned to Person 4.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from .bezier import Point


# ---------------------------------------------------------------------------
# Core scaling
# ---------------------------------------------------------------------------

def scale_points(points: np.ndarray, center: Point, k: float) -> np.ndarray:
    """Scale points relative to the selected center.

    Formula:
        P' = C + k * (P - C)

    In coordinate form:
        x' = xc + k * (x - xc)
        y' = yc + k * (y - yc)

    Args:
        points: source curve points with shape (n, 2).
        center: scaling center C = (xc, yc).
        k: scale coefficient.

    Returns:
        Scaled points with shape (n, 2).
    """
    c = np.array(center)
    return c + k * (points - c)


# ---------------------------------------------------------------------------
# Single-scale plot
# ---------------------------------------------------------------------------

def plot_scaled_curve(
    points: np.ndarray,
    scale: float,
    save_path: str,
    *,
    center: Point | None = None,
    figure_number: int | None = None,
) -> None:
    """Plot and save one scaled version of the composite curve.

    Args:
        points:        Curve points (n, 2) already scaled.
        scale:         Scale coefficient k used (for title / label).
        save_path:     File path to save the PNG image.
        center:        Optional scaling center to mark on the plot.
        figure_number: Optional figure number for the caption (e.g. 2 → «Рисунок 2»).
    """
    fig, ax = plt.subplots(figsize=(7, 8))

    ax.plot(points[:, 0], points[:, 1], color="#d62728", linewidth=2.2,
            label=f"Составная кривая Безье (k = {scale})")
    ax.fill(points[:, 0], points[:, 1], alpha=0.12, color="#d62728")

    if center is not None:
        ax.plot(*center, marker="x", markersize=10, color="#2ca02c",
                markeredgewidth=2, label=f"Центр масштабирования ({center[0]}, {center[1]})")

    # Descriptive title
    scale_desc = {0.5: "уменьшение в 2 раза", 1.0: "исходный размер",
                  1.5: "увеличение в 1.5 раза", 2.0: "увеличение в 2 раза"}
    desc = scale_desc.get(float(scale), f"k = {scale}")

    caption = ""
    if figure_number is not None:
        caption = f"Рисунок {figure_number} — "
    caption += f"Составная кривая Безье, масштаб k = {scale}"

    ax.set_title(f"Составная кривая Безье\nМасштаб k = {scale}  ({desc})", fontsize=13)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.35)
    ax.set_aspect("equal")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    # Caption below the figure
    fig.text(0.5, 0.01, caption, ha="center", fontsize=10, style="italic")

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  Сохранено: {save_path}")


# ---------------------------------------------------------------------------
# Multi-scale batch function (main deliverable for Person 4)
# ---------------------------------------------------------------------------

def plot_scaled_versions(
    curve_points: np.ndarray,
    scales: list[float],
    images_dir: str | Path,
    center: Point = (0.0, 4.0),
) -> None:
    """Build and save images of the composite curve at different scales.

    For each k in *scales* the function:
    1. Scales *curve_points* relative to *center* using :func:`scale_points`.
    2. Saves an individual PNG: ``flame_scale_<k>.png``.

    Additionally saves a combined comparison plot: ``flame_all_scales.png``.

    Figure numbering follows the report captions:
        Рисунок 2 — k = 1
        Рисунок 3 — k = 0.5
        Рисунок 4 — k = 2
        (k = 1.5 gets the next available number)

    Args:
        curve_points: Base composite curve points (n, 2) at scale k = 1.
        scales:       List of scale coefficients, e.g. [0.5, 1, 1.5, 2].
        images_dir:   Directory where PNG files will be saved.
        center:       Scaling center C = (xc, yc).
    """
    images_dir = Path(images_dir)
    images_dir.mkdir(parents=True, exist_ok=True)

    # Figure numbers from the task description
    figure_numbers: dict[float, int] = {1.0: 2, 0.5: 3, 2.0: 4, 1.5: 5}

    print("\n--- Масштабирование составной кривой ---")
    print(f"Центр масштабирования: C = {center}")

    for k in scales:
        scaled = scale_points(curve_points, center, k)
        fname = f"flame_scale_{k}.png"
        fpath = str(images_dir / fname)
        fig_num = figure_numbers.get(float(k))
        plot_scaled_curve(scaled, k, fpath, center=center, figure_number=fig_num)

    # -----------------------------------------------------------------------
    # Combined comparison plot
    # -----------------------------------------------------------------------
    colors = {0.5: "#1f77b4", 1.0: "#2ca02c", 1.5: "#ff7f0e", 2.0: "#d62728"}
    linestyles = {0.5: "--", 1.0: "-", 1.5: "-.", 2.0: ":"}

    fig, ax = plt.subplots(figsize=(9, 10))

    for k in sorted(scales):
        scaled = scale_points(curve_points, center, k)
        color = colors.get(float(k), None)
        ls = linestyles.get(float(k), "-")
        ax.plot(scaled[:, 0], scaled[:, 1],
                color=color, linestyle=ls, linewidth=2.0,
                label=f"k = {k}")

    # Mark scaling center
    ax.plot(*center, marker="x", markersize=12, color="black",
            markeredgewidth=2.5, label=f"Центр масштабирования {center}", zorder=5)

    ax.set_title("Составная кривая Безье при разных масштабах", fontsize=14)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.35)
    ax.set_aspect("equal")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    caption = "Рисунок 5 — Составная кривая Безье при k ∈ {0.5, 1, 1.5, 2}"
    fig.text(0.5, 0.01, caption, ha="center", fontsize=10, style="italic")

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    combined_path = str(images_dir / "flame_all_scales.png")
    plt.savefig(combined_path, dpi=150)
    plt.close()
    print(f"  Сохранено (сравнение): {combined_path}")

    # -----------------------------------------------------------------------
    # Brief analysis printout
    # -----------------------------------------------------------------------
    print("\n--- Краткий анализ масштабирования ---")
    print("  Форма кривой сохраняется при любом k: масштабирование является")
    print("  аффинным преобразованием подобия, которое не искажает углы и")
    print("  пропорции. Меняется только размер контура относительно центра C.")
    for k in scales:
        scaled = scale_points(curve_points, center, k)
        x_span = scaled[:, 0].max() - scaled[:, 0].min()
        y_span = scaled[:, 1].max() - scaled[:, 1].min()
        print(f"  k = {k:3}: ширина ≈ {x_span:.2f}, высота ≈ {y_span:.2f}")
