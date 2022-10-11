from __future__ import annotations

import numpy as np
from ground.base import get_context
from bentley_ottmann.planar import contour_self_intersects


def offset_curve(points: np.ndarray, amount: float = 0) -> np.ndarray:
    """Offsets the points of a (closed) curve in the normal direction.

    Args:
        points: The 2D points. A points matrix (n x 2) corresponds to n 2-dimension points.
                Note, n > 3 for the points to define a closed curve.
        amount: The offset amount. If `offset=0` the curve is unchanged.
                If `offset>0` the curve is expanded. If `offset<0` the curve
                is shrinked.

    Returns:
        The offset 2D points.

    Raises:
        TypeError
        ValueError
    """
    if not isinstance(points, np.ndarray):
        raise TypeError("In offset_curve, points must be a np.ndarray.")

    points = points.squeeze()

    if points.ndim != 2 or points.shape[1] != 2 or points.shape[0] < 3:
        raise ValueError("In offset_curve, points must be an (n x 2) matrix.")

    if not isinstance(amount, (int, float)):
        raise TypeError("In offset_curve, amount must be a number.")

    points_offset = np.empty(points.shape)

    for idx in range(points.shape[0]):
        point_before = points[idx - 1, :]
        point_after = None

        if idx < points.shape[0] - 1:
            point_after = points[idx + 1, :]
        else:
            point_after = points[0, :]

        tangent = point_before - point_after

        normal = np.array([-tangent[1], tangent[0]])
        normal = normal / np.linalg.norm(normal)

        points_offset[idx, :] = points[idx, :] + amount * normal

    return points_offset


def self_intersection(points: np.ndarray) -> bool:
    """Checks if a curve intersects with itself.

    Args:
        points: The 2D points. A points matrix (n x 2) corresponds to n 2-dimension points.
                Note, n > 3 for the points to define a closed curve.

    Returns:
        `True` if the curve intersects with itself, `False` otherwise.
    """
    if not isinstance(points, np.ndarray):
        raise TypeError("In offset_curve, points must be a np.ndarray.")

    points = points.squeeze()

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("In offset_curve, points must be an (n x 2) matrix.")

    context = get_context()
    point, contour = context.point_cls, context.contour_cls

    curve = []
    for idx in range(points.shape[0]):
        x = points[idx, 0]
        y = points[idx, 1]
        curve.append(point(x, y))

    return contour_self_intersects(contour(curve))
