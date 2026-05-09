"""Main entry point for Bezier coursework.

Run after implementation:
    python -m src.main
"""

from __future__ import annotations

from pathlib import Path

from .bezier import Point
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


def main() -> None:
    """Run all calculations and save images.

    Full implementation will be added by Person 2, Person 3 and Person 4.
    """
    IMAGES_DIR.mkdir(exist_ok=True)
    print("Project structure is ready.")
    print("Selected contour for task 3.2: stylized flame.")
    print("Next steps:")
    print("1. Implement cubic_bezier() in src/bezier.py")
    print("2. Implement composite_bezier() in src/composite_curve.py")
    print("3. Implement scale_points() and plotting in src/scaling.py")
    print("4. Save generated images to images/")


if __name__ == "__main__":
    main()
