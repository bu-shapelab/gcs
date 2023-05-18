from __future__ import annotations

import numpy as np
from ground.base import get_context
from bentley_ottmann.planar import contour_self_intersects


def _offset_curve(points: np.ndarray, offset: float = 0) -> np.ndarray:
    """Offsets a closed polar curve in the normal direction.

    Parameters
    ----------
    points : (N, 2) np.ndarray
        The polar points. Note, `N`>2 to define a closed curve.
        The columns contain the angles and radii respectively.
    offset : float (default=0)
        The offset amount.
        If ``offset=0``, the curve is unchanged.
        If ``offset>0``, the curve is expanded.
        If ``offset<0``, the curve is shrank.

    Returns
    -------
    points_offset : (N, 2) np.ndarray
        The offset points.

    """
    points_offset = np.empty(points.shape)

    for index in range(points.shape[0]):
        point_before = points[index - 1, :]
        point_after = None

        if index < points.shape[0] - 1:
            point_after = points[index + 1, :]
        else:
            point_after = points[0, :]

        tangent = point_before - point_after

        # 90 degree rotation
        normal = np.array([-tangent[1], tangent[0]])
        normal = normal / np.linalg.norm(normal)

        points_offset[index, :] = points[index, :] + offset * normal

    return points_offset


def _self_intersection(points: np.ndarray) -> bool:
    """Checks if a polar curve intersects with itself.

    Parameters
    ----------
    points : (N, 2) np.ndarray
        The polar points.
        The columns contain the angles and radii respectively.

    Returns
    -------
    result : bool
        `True` if the curve intersects itself.

    """
    context = get_context()
    point, contour = context.point_cls, context.contour_cls

    curve = []
    for index in range(points.shape[0]):
        x = points[index, 0]
        y = points[index, 1]
        curve.append(point(x, y))

    result = contour_self_intersects(contour(curve))
    return result
