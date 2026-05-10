"""Main entry point for Bezier coursework.

Run after implementation:
    python -m src.main
"""

from __future__ import annotations

from pathlib import Path

from .bezier import Point, cubic_bezier, bezier_coefficients, plot_elementary_curve
from .composite_curve import Segment

PROJECT_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = PROJECT_ROOT / "images"

# Example for task 3.1: elementary cubic Bezier curve.
ELEMENTARY_CONTROL_POINTS: tuple[Point, Point, Point, Point] = (
    (0, 0),
    (1, 3),
    (3, 3),
    (4, 0),
)

# Selected contour for task 3.2: stylized flame.
# The contour consists of four cubic Bezier segments.
FLAME_SEGMENTS: list[Segment] = [
    # Segment 1: lower left part of the flame.
    ((0.0, 0.0), (-2.0, -0.2), (-2.8, 2.5), (-1.2, 4.5)),

    # Segment 2: left upper part leading to the top point.
    ((-1.2, 4.5), (-1.0, 5.8), (-0.5, 7.0), (0.0, 8.0)),

    # Segment 3: top point and right upper part.
    ((0.0, 8.0), (0.8, 6.8), (2.0, 5.5), (1.4, 3.8)),

    # Segment 4: lower right part and closing the contour.
    ((1.4, 3.8), (2.8, 2.0), (2.2, 0.2), (0.0, 0.0)),
]

# Approximate scaling center for the flame contour.
SCALE_CENTER: Point = (0.0, 4.0)
SCALES = [0.5, 1, 1.5, 2]


def run_task_31() -> None:
    """Task 3.1 — elementary cubic Bezier curve (Person 2)."""
    P0, P1, P2, P3 = ELEMENTARY_CONTROL_POINTS

    print("=== Задание 3.1: элементарная кубическая кривая Безье ===")
    print(f"Контрольные точки: P0={P0}, P1={P1}, P2={P2}, P3={P3}")

    coeff_x, coeff_y = bezier_coefficients(P0, P1, P2, P3)
    print("\nКоэффициентная форма:")
    print(f"  x(t) = {coeff_x[0]:.4f}*t^3 + {coeff_x[1]:.4f}*t^2 + {coeff_x[2]:.4f}*t + {coeff_x[3]:.4f}")
    print(f"  y(t) = {coeff_y[0]:.4f}*t^3 + {coeff_y[1]:.4f}*t^2 + {coeff_y[2]:.4f}*t + {coeff_y[3]:.4f}")

    curve = cubic_bezier(P0, P1, P2, P3, n=200)

    save_path = str(IMAGES_DIR / "elementary_curve.png")
    plot_elementary_curve(curve, [P0, P1, P2, P3], save_path)
    print("Задание 3.1 выполнено.\n")


def main() -> None:
    """Run all calculations and save images."""
    IMAGES_DIR.mkdir(exist_ok=True)

    run_task_31()

    # Tasks 3.2: composite curve and scaling — implemented by Person 3 and Person 4.
    print("Задания 3.2 (составная кривая и масштабирование) ожидают реализации от Человека 3 и Человека 4.")


if __name__ == "__main__":
    main()
