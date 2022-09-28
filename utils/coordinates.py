from __future__ import annotations

import numpy as np


def polar_to_cartesian(theta: np.ndarray, radii: np.ndarray) -> np.ndarray:
    """Converts polar coordinates to cartesian coordinates.

    Args:
        theta: The angles.
        radii: The radii.

    Returns:
        The equivalent 2D points. A points matrix (n x 2) corresponds to n 2-dimension points.
    """
    theta = theta.reshape(-1, 1)
    radii = radii.reshape(-1, 1)

    x = radii * np.cos(theta).reshape(-1, 1)
    y = radii * np.sin(theta).reshape(-1, 1)

    points = np.concatenate((x, y), axis=1)

    return points


def cartesian_to_polar(points: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Converts cartesian coordinates to polar coordinates.

    Args:
        points: The 2D points. A points matrix (n x 2) corresponds to n 2-dimension points.

    Returns:
        The equivalent theta and radii.
    """
    x = points[:, 0]
    y = points[:, 1]

    radii = np.sqrt(np.power(x, 2) + np.power(y, 2))
    theta = np.arctan2(y, x)

    return theta, radii
