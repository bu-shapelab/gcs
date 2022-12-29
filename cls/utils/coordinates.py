from __future__ import annotations

import numpy as np


def polar_to_cartesian(points: np.ndarray) -> np.ndarray:
    """TODO Converts polar coordinates to cartesian coordinates.

    Args:
        points: A (n x 2) matrix of polar points.
                The angles and radii are in the first and second columns respectively.

    Returns:
        The equivalent 2D cartesian points.
        The x- and y-values are in the first and second columns respectively.
    """
    if not isinstance(points, np.ndarray):
        raise TypeError('TODO')

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError('TODO')

    theta = points[:, 0]
    radii = points[:, 1]

    x = radii * np.cos(theta)
    y = radii * np.sin(theta)

    points_cartesian = np.empty(points.shape)
    points_cartesian[:, 0] = x
    points_cartesian[:, 1] = y

    return points_cartesian


def cartesian_to_polar(points: np.ndarray) -> np.ndarray:
    """TODO Converts cartesian coordinates to polar coordinates.

    Args:
        points: A (n x 2) matrix of cartesian points.
                The x- and y-values are in the first and second columns respectively.

    Returns:
        The equivalent 2D polar points.
        The angles and radii are in the first and second columns respectively.
    """
    if not isinstance(points, np.ndarray):
        raise TypeError('TODO')

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError('TODO')

    x = points[:, 0]
    y = points[:, 1]

    theta = np.arctan2(y, x)
    radii = np.sqrt(np.power(x, 2) + np.power(y, 2))

    points_polar = np.empty(points.shape)
    points_polar[:, 0] = theta
    points_polar[:, 1] = radii

    return points_polar
