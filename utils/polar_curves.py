from __future__ import annotations

import numpy as np
from ground.base import get_context
from bentley_ottmann.planar import contour_self_intersects


def offset_curve(points: np.ndarray, offset: float = 0) -> np.ndarray:
    """Offsets the points of a polar curve in the normal direction.

    Args:
        points: An (n x 2) matrix of cartesian points listed in counterclockwise order.
                The x- and y-values are in the first and second columns respectively.
                Note, n > 2 for the points to define a closed curve.
        offset: The offset amount. If `offset=0` the curve is unchanged.
                If `offset>0` the curve is expanded.
                If `offset<0` the curve is shrank.

    Returns:
        The offset points.
    """
    if not isinstance(points, np.ndarray):
        raise TypeError('In offset_curve, points must be a np.ndarray.')

    points = points.squeeze()

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError('In offset_curve, points must be an (n x 2) matrix.')

    if points.shape[0] < 3:
        raise ValueError('In offset_curve, points must be an (n x 2) matrix where n > 2.')

    if not isinstance(offset, (int, float)):
        raise TypeError('In offset_curve, amount must be a number.')

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

        points_offset[idx, :] = points[idx, :] + offset * normal

    return points_offset


def self_intersection(points: np.ndarray) -> bool:
    """Checks if a polar curve intersects with itself.

    Args:
        points: An (n x 2) matrix of cartesian points listed in counterclockwise order.
                The x- and y-values are in the first and second columns respectively.
                Note, n > 2 for the points to define a closed curve.

    Returns:
        `True` if the curve intersects with itself, `False` otherwise.
    """
    if not isinstance(points, np.ndarray):
        raise TypeError('In offset_curve, points must be a np.ndarray.')

    points = points.squeeze()

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError('In offset_curve, points must be an (n x 2) matrix.')

    if points.shape[0] < 3:
        raise ValueError('In offset_curve, points must be an (n x 2) matrix where n > 2.')

    context = get_context()
    point, contour = context.point_cls, context.contour_cls

    curve = []
    for idx in range(points.shape[0]):
        x = points[idx, 0]
        y = points[idx, 1]
        curve.append(point(x, y))

    return contour_self_intersects(contour(curve))
