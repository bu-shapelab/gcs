from __future__ import annotations

import numpy as np


def polar_to_cartesian(theta: np.ndarray, radii: np.ndarray) -> np.ndarray:
    """Converts polar coordinates to cartesian coordinates.

    Args:
        theta: A vector of angle values.
        radii: A vector of radii values.

    Returns:
        The equivalent 2D points. A points matrix (n x 2) corresponds to n 2-dimension points.

    Raises:
        TypeError
        ValueError
    """
    if not isinstance(theta, np.ndarray):
        raise TypeError("In polar_to_cartesian, theta must be a np.ndarray.")
    if not isinstance(radii, np.ndarray):
        raise TypeError("In polar_to_cartesian, radii must be a np.ndarray.")

    theta = theta.squeeze()
    radii = radii.squeeze()

    if theta.ndim > 1:
        raise ValueError("In polar_to_cartesian, theta must be an vector.")
    if radii.ndim > 1:
        raise ValueError("In polar_to_cartesian, radii must be a vector.")
    if theta.size != radii.size:
        raise ValueError("In polar_to_cartesian, theta and radii must be the same size.")

    x = radii * np.cos(theta)
    y = radii * np.sin(theta)

    points = np.vstack((x, y)).transpose()

    return points


def cartesian_to_polar(points: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Converts cartesian coordinates to polar coordinates.

    Args:
        points: The 2D points. A points matrix (n x 2) corresponds to n 2-dimension points.

    Returns:
        The equivalent theta and radii.

    Raises:
        TypeError
        ValueError
    """
    if not isinstance(points, np.ndarray):
        raise TypeError("In polar_to_cartesian, points must be a np.ndarray.")

    points = points.squeeze()

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("In polar_to_cartesian, points must be an (n x 2) matrix.")

    x = points[:, 0]
    y = points[:, 1]

    radii = np.sqrt(np.power(x, 2) + np.power(y, 2))
    theta = np.arctan2(y, x)

    return theta, radii
