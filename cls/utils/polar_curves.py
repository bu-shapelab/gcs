from __future__ import annotations

import numpy as np
from ground.base import get_context
from bentley_ottmann.planar import contour_self_intersects


def offset_curve(points: np.ndarray, offset: float = 0) -> np.ndarray:
    """Offsets a closed polar curve in the normal direction.

    Parameters
    ----------
    points : (N, 2) np.ndarray
        Array of points. The first column contains the angles.
        The second column contains the radii. `N`>2 to define a closed curve.
    offset : float (default=0)
        The offset amount. If ``offset``=0, the curve is unchanged. If ``offset``>0,
        the curve is expanded. If ``offset``<0, the curve is shrank.

    Returns
    -------
    points : (N, 2) np.ndarray
        Array of offset points. The first column contains the angles.
        The second column contains the radii.

    Raises
    ------
    TypeError
        If ``points`` is not an np.ndarray.
        If ``offset`` is not a number.
    ValueError
        If ``points`` is not a (N, 2) matrix.

    """
    if not isinstance(points, np.ndarray):
        raise TypeError('TODO')

    points = points.squeeze()

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError('TODO')

    if points.shape[0] < 3:
        raise ValueError('TODO')

    if not isinstance(offset, (int, float)):
        raise TypeError('TODO')

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

    Parameters
    ----------
    points : (N, 2) np.ndarray
        Array of points. The first column contains the angles.
        The second column contains the radii.

    Returns
    -------
    intersect : bool
        `True` if the curve intersects itself, `False` otherwise.

    Raises
    ------
    TypeError
        If ``points`` is not an np.ndarray.
    ValueError
        If ``points`` is not a (N, 2) matrix.

    """
    if not isinstance(points, np.ndarray):
        raise TypeError('TODO')

    points = points.squeeze()

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError('TODO')

    if points.shape[0] < 3:
        raise ValueError('TODO')

    context = get_context()
    point, contour = context.point_cls, context.contour_cls

    curve = []
    for idx in range(points.shape[0]):
        x = points[idx, 0]
        y = points[idx, 1]
        curve.append(point(x, y))

    return contour_self_intersects(contour(curve))
