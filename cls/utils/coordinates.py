from __future__ import annotations

import numpy as np


def polar_to_cartesian(points: np.ndarray) -> np.ndarray:
    """Converts polar points to cartesian points.

    Parameters
    ----------
    points : (N, 2) np.ndarray
        Array of points. The first column contains the angles.
        The second column contains the radii.

    Returns
    -------
    points : (N, 2) np.ndarray
        Array of points. The first column contains the x-values.
        The second column contains the y-values.

    Raises
    ------
    TypeError
        If ``points`` is not an np.ndarray.
    ValueError
        If ``points`` is not a (N, 2) matrix.
    """
    if not isinstance(points, np.ndarray):
        raise TypeError('points needs to be an np.ndarray.')

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError('points needs to be an (N, 2) matrix.')

    theta = points[:, 0]
    radii = points[:, 1]

    x = radii * np.cos(theta)
    y = radii * np.sin(theta)

    points_cartesian = np.empty(points.shape)
    points_cartesian[:, 0] = x
    points_cartesian[:, 1] = y

    return points_cartesian


def cartesian_to_polar(points: np.ndarray) -> np.ndarray:
    """Converts cartesian points to polar points.

    Parameters
    ----------
    points : (N, 2) np.ndarray
        Array of points. The first column contains the x-values.
        The second column contains the y-values.

    Returns
    -------
    points : (N, 2) np.ndarray
        Array of points. The first column contains the angles.
        The second column contains the radii.

    Raises
    ------
    TypeError
        If ``points`` is not an np.ndarray.
    ValueError
        If ``points`` is not a (N, 2) matrix.

    """
    if not isinstance(points, np.ndarray):
        raise TypeError('points needs to be an np.ndarray.')

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError('points needs to be an (N, 2) np.ndarray.')

    x = points[:, 0]
    y = points[:, 1]

    theta = np.arctan2(y, x)
    radii = np.sqrt(np.power(x, 2) + np.power(y, 2))

    points_polar = np.empty(points.shape)
    points_polar[:, 0] = theta
    points_polar[:, 1] = radii

    return points_polar
