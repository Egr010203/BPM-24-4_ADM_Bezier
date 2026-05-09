"""Composite Bezier curve utilities.

This file is assigned to Person 3.
"""

from __future__ import annotations

import numpy as np

from .bezier import Point, cubic_bezier

Segment = tuple[Point, Point, Point, Point]


def composite_bezier(segments: list[Segment], n: int = 100) -> np.ndarray:
    """Return points of a composite cubic Bezier curve.

    Args:
        segments: list of cubic Bezier segments. Each segment contains four points.
        n: number of points per segment.

    Returns:
        NumPy array with points of the full composite curve.
    """
    # TODO: Person 3 implements this function using cubic_bezier().
    raise NotImplementedError("Implement composite Bezier curve calculation.")


def validate_segments(segments: list[Segment]) -> bool:
    """Check that neighbouring segments are connected.

    For a closed flame contour:
    - the end point of each segment must equal the start point of the next segment;
    - the last segment end point must equal the first segment start point.
    """
    # TODO: Person 3 may implement validation.
    raise NotImplementedError("Implement segment validation.")
