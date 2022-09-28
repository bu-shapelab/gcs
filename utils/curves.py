from __future__ import annotations

import numpy as np
from ground.base import get_context
from bentley_ottmann.planar import contour_self_intersects


def offset_curve(points: np.ndarray, amount: float = 0) -> np.ndarray:
    """Offsets the points of a curve in the normal direction.

    Args:
        points: The 2D points. A points matrix (n x 2) corresponds to n 2-dimension points.
        amount: The offset amount. If `offset=0` the curve is unchanged.
                If `offset>0` the curve is expanded. If `offset<0` the curve
                is shrinked.

    Returns:
        The offset 2D points.
    """
    points_offset = np.empty(points.shape)

    for idx in range(points.shape[0] - 1):
        tangent = points[idx - 1, :] - points[idx + 1, :]
        normal = np.array([-tangent[1], tangent[0]])
        normal = normal / np.linalg.norm(normal)
        points_offset[idx, :] = points[idx, :] + amount * normal

    tangent = points[-2, :] - points[0, :]
    normal = np.array([-tangent[1], tangent[0]])
    normal = normal / np.linalg.norm(normal)
    points_offset[-1, :] = points[-1, :] + amount * normal

    return points_offset


def self_intersection(points: np.ndarray) -> bool:
    """Checks if a curve intersects with itself.

    Args:
        points: The 2D points. A points matrix (n x 2) corresponds to n 2-dimension points.

    Returns:
        `True` if the curve intersects with itself, `False` otherwise.
    """
    context = get_context()
    point, contour = context.point_cls, context.contour_cls

    curve = []
    for idx in range(points.shape[0]):
        x = points[idx, 0]
        y = points[idx, 1]
        curve.append(point(x, y))

    return contour_self_intersects(contour(curve))
