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
    total_points = []
    for i, seg in enumerate(segments):
        points = cubic_bezier(*seg, n=n)
        if i > 0:
            total_points.append(points[1:])
        else:
            total_points.append(points)
    
    return np.vstack(total_points)


def validate_segments(segments: list[Segment], tol: float = 1e-6) -> bool:
    """Check that neighbouring segments are connected.

    For a closed flame contour:
    - the end point of each segment must equal the start point of the next segment;
    - the last segment end point must equal the first segment start point.
    """
    if not segments:
        return False
        
    for i in range(len(segments)):
        current_end = np.array(segments[i][3])
        next_start = np.array(segments[(i + 1) % len(segments)][0])
        
        if not np.allclose(current_end, next_start, atol=tol):
            return False
            
    return True
