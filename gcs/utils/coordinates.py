from __future__ import annotations

from typing import Tuple
import numpy as np


def pol2cart(radius: np.ndarray,
             theta: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Converts polar points to cartesian points.

    Parameters
    ----------
    radius : (N,) np.ndarray
        The radial values.
    theta : (N,) np.ndarray
        The angular values.

    Returns
    -------
    x : (N,) np.ndarray
        The x-axis values.
    y : (N,) np.ndarray
        The y-axis values.

    """
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    return x, y


def cart2pol(x: np.ndarray,
             y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Converts cartesian points to polar points.

    Parameters
    ----------
    x : (N,) np.ndarray
        The x-axis values.
    y : (N,) np.ndarray
        The y-axis values.

    Returns
    -------
    radius : (N,) np.ndarray
        The radial values.
    theta : (N,) np.ndarray
        The angular values.

    """
    theta = np.arctan2(y, x)
    radius = np.sqrt(np.power(x, 2) + np.power(y, 2))

    return radius, theta
