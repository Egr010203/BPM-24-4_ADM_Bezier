"""Main entry point for Bezier coursework.

Run after implementation:
    python -m src.main
"""

from __future__ import annotations

from pathlib import Path

from .bezier import Point, cubic_bezier, bezier_coefficients, plot_elementary_curve
from .composite_curve import Segment, composite_bezier, validate_segments
from .scaling import scale_points, plot_scaled_curve, plot_scaled_versions

PROJECT_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = PROJECT_ROOT / "images"

# Example for task 3.1: elementary cubic Bezier curve.
ELEMENTARY_CONTROL_POINTS: tuple[Point, Point, Point, Point] = (
    (0, 0),
    (1, 3),
    (3, 3),
    (4, 0),
)

# Selected contour for task 3.2: stylized flame with multiple tongues.
# The contour consists of six cubic Bezier segments to form three flames.
FLAME_SEGMENTS: list[Segment] = [
    # Segment 1: base to left tongue tip
    ((0.0, 0.0), (-2.0, 1.0), (-2.5, 3.0), (-1.5, 4.0)),

    # Segment 2: left tongue tip down to the left valley
    ((-1.5, 4.0), (-1.0, 3.0), (-0.8, 3.0), (-0.5, 3.5)),

    # Segment 3: left valley up to the main central tongue tip
    ((-0.5, 3.5), (-0.5, 5.0), (-0.2, 7.0), (0.2, 8.0)),

    # Segment 4: main central tongue tip down to the right valley
    ((0.2, 8.0), (0.5, 6.0), (0.8, 4.0), (1.0, 3.5)),

    # Segment 5: right valley up to the right tongue tip
    ((1.0, 3.5), (1.5, 3.5), (2.0, 4.5), (2.2, 5.0)),

    # Segment 6: right tongue tip down to the base, closing the contour
    ((2.2, 5.0), (2.5, 3.0), (1.5, 0.5), (0.0, 0.0)),
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


def run_task_32() -> None:
    """Task 3.2 — composite flame curve and scaling (Persons 3 & 4)."""
    print("=== Задание 3.2: составная кривая (пламя) и масштабирование ===")

    if not validate_segments(FLAME_SEGMENTS):
        print("Ошибка: Сегменты составной кривой не связаны корректно.")
        return

    # 1. Построение базовой составной кривой (масштаб 1)
    points_base = composite_bezier(FLAME_SEGMENTS, n=150)

    # 2. Масштабирование и визуализация (все масштабы + сравнительный график)
    plot_scaled_versions(points_base, SCALES, IMAGES_DIR, center=SCALE_CENTER)

    print("Задание 3.2 выполнено.\n")


def main() -> None:
    """Run all calculations and save images."""
    IMAGES_DIR.mkdir(exist_ok=True)

    run_task_31()
    run_task_32()


if __name__ == "__main__":
    main()
