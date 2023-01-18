from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np
from cls._utils import _summed_cosine, _optimal_scaling_factor
from cls._utils import _polar_to_cartesian

if TYPE_CHECKING:
    from cls import CLS

# Discretized thetas from [0, 2pi]
THETA = np.arange(0, 2 * np.pi, 0.01)


def discretize(shape: CLS) -> np.ndarray:
    """Discretizes a CLS shape into points.

    The height of a ``CLS`` is divided into steps. At each step,
    the polar curve is discretized to `X` evenly spaced points
    where ``X=np.arange(0, 2 * np.pi, 0.01).size=629``.

    Parameters
    ----------
    shape : cls.CLS
        The CLS shape.
    n_steps : int (default=100)
        The number of steps to discretize the ``shape`` height.

    Returns
    -------
    points : (``629 x n_steps``, 3, ) np.ndarray
        The matrix of points.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> vertices = cls.discretize(shape=shape)

    >>> shape = cls.CLS()
    >>> vertices = shape.vertices

    """
    n_steps = shape.n_steps

    if n_steps < 1:
        raise ValueError('n_steps needs to be greater than 0.')

    parameters = shape.parameters
    height_per_step = parameters['height'] / (n_steps - 1)

    points = np.empty((THETA.size * n_steps, 3))

    c1s = np.linspace(parameters['c1_base'], parameters['c1_top'], n_steps)
    c2s = np.linspace(parameters['c2_base'], parameters['c2_top'], n_steps)
    perimeters = np.linspace(shape.base_perimeter,
                             shape.top_perimeter, n_steps)
    twists_linear = np.linspace(0, parameters['twist_linear'], n_steps)
    twists_oscillating = parameters['twist_amplitude'] * np.sin(
        np.linspace(0, 2 * np.pi * parameters['twist_period'], n_steps))

    for step in range(n_steps):
        c1 = c1s[step]
        c2 = c2s[step]
        perimeter = perimeters[step]
        twist_linear = twists_linear[step]
        twist_oscillating = twists_oscillating[step]
        height = height_per_step * step

        r0 = _optimal_scaling_factor(length=perimeter, c1=c1, c2=c2)

        theta = THETA + twist_linear + twist_oscillating
        radii = _summed_cosine(theta=theta, r0=r0, c1=c1, c2=c2)

        points_2d_polar = np.vstack((theta, radii)).transpose()
        points_2d_cartesian = _polar_to_cartesian(points=points_2d_polar)

        idx_start = step * THETA.size
        idx_end = (step + 1) * THETA.size

        points[idx_start:idx_end, :2] = points_2d_cartesian
        points[idx_start:idx_end, 2] = height

    return points
