from __future__ import annotations

import numpy as np


def pol2cart(r: np.ndarray, theta: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Converts polar points to cartesian points.

    Parameters
    ----------
    r : (N,) numpy.ndarray
        Radial values.
    theta : (N,) numpy.ndarray
        Angular values.

    Returns
    -------
    x : (N,) numpy.ndarray
        x-axis values.
    y : (N,) numpy.ndarray
        y-axis values.

    """
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x, y


def cart2pol(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Converts cartesian points to polar points.

    Parameters
    ----------
    x : (N,) numpy.ndarray
        x-axis values.
    y : (N,) numpy.ndarray
        y-axis values.

    Returns
    -------
    r : (N,) numpy.ndarray
        Radial values.
    theta : (N,) numpy.ndarray
        Angular values.

    """
    theta = np.arctan2(y, x)
    r = np.hypot(x, y)

    return r, theta
