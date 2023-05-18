from __future__ import annotations

import numpy as np


def _polar_to_cartesian(points_polar: np.ndarray) -> np.ndarray:
    """Converts polar points to cartesian points.

    Parameters
    ----------
    points_polar : (N, 2) np.ndarray
        The polar points.
        The columns contain the angles and radii respectively.

    Returns
    -------
    points_cartesian : (N, 2) np.ndarray
        The cartesian points.
        The columns contain the x- and y-values respectively.

    """
    theta = points_polar[:, 0]
    radii = points_polar[:, 1]

    x = radii * np.cos(theta)
    y = radii * np.sin(theta)

    points_cartesian = np.vstack((x, y)).transpose()

    return points_cartesian


def _cartesian_to_polar(points_cartesian: np.ndarray) -> np.ndarray:
    """Converts cartesian points to polar points.

    Parameters
    ----------
    points_cartesian : (N, 2) np.ndarray
        The cartesian points.
        The columns contain the x- and y-values respectively.

    Returns
    -------
    points_polar : (N, 2) np.ndarray
        The polar points.
        The columns contain the angles and radii respectively.

    """
    x = points_cartesian[:, 0]
    y = points_cartesian[:, 1]

    theta = np.arctan2(y, x)
    radii = np.sqrt(np.power(x, 2) + np.power(y, 2))

    points_polar = np.vstack((theta, radii)).transpose()

    return points_polar
