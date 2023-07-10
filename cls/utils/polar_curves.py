from __future__ import annotations

from typing import Tuple
import numpy as np
from ground.base import get_context
from bentley_ottmann.planar import contour_self_intersects


def offset_curve(radius: np.ndarray,
                 theta: np.ndarray,
                 offset: float = 0) -> Tuple[np.ndarray, np.ndarray]:
    """Offsets a closed polar curve in the normal direction.

    Parameters
    ----------
    radius : (N,) np.ndarray
        The radial values. Note, `N`>2 to define a closed curve.
    theta : (N,) np.ndarray
        The angular values. Note, `N`>2 to define a closed curve.
    offset : float (default=0)
        The offset amount:
        If ``offset=0``, the curve is unchanged.
        If ``offset>0``, the curve is expanded.
        If ``offset<0``, the curve is shrank.

    Returns
    -------
    radius_offset : (N,) np.ndarray
        The offset radial values.
    theta_offset : (N,) np.ndarray
        The offset angular values.

    """
    radius_offset = np.empty_like(radius)
    theta_offset = np.empty_like(radius)

    for index in range(radius.shape[0]):
        index_before = index - 1
        index_after = index + 1

        if index == radius.shape[0] - 1:
            index_after = 0

        point_before = np.array([
            radius[index_before],
            theta[index_before]
        ])

        point = np.array([
            radius[index],
            theta[index]
        ])

        point_after = np.array([
            radius[index_after],
            theta[index_after]
        ])

        tangent = point_before - point_after

        # 90 degree rotation
        normal = np.array([-tangent[1], tangent[0]])
        normal = normal / np.linalg.norm(normal)

        point = point + offset * normal

        radius_offset[index] = point[0]
        theta_offset[index] = point[1]

    return radius_offset, theta_offset


def self_intersection(x: np.ndarray,
                      y: np.ndarray) -> bool:
    """Checks if a polar curve intersects with itself.

    Parameters
    ----------
    x : (N,) np.ndarray
        The x-axis values.
    y : (N,) np.ndarray
        The y-axis values.

    Returns
    -------
    result : bool
        `True` if the curve intersects itself.

    """
    context = get_context()
    point, contour = context.point_cls, context.contour_cls

    curve = []
    for index in range(x.shape[0]):
        curve.append(point(x[index], y[index]))

    result = contour_self_intersects(contour(curve))

    return result
