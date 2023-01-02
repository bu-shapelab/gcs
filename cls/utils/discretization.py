from __future__ import annotations

import numpy as np
from cls import CLS

from .summed_cosine import summed_cosine, optimal_scaling_factor
from .coordinates import polar_to_cartesian

# Discretized thetas from [0, 2pi]
THETA = np.arange(0, 2 * np.pi, 0.01)


def discretize(shape: CLS, n_steps: int = 100) -> np.ndarray:
    """Discretizes a CLS shape into a tensor of points.

    The height of a ``CLS`` is divided into steps. At each step,
    the polar curve is discretizes to `X` evenly spaced points
    where ``X=np.arange(0, 2 * np.pi, 0.01).size``=629.

    Parameters
    ----------
    shape : cls.CLS
        The CLS shape.
    n_steps : int (default=100)
        The number of steps to discretize the `shape` height.

    Returns
    -------
    points : (629, 3, ``n_steps``) np.ndarray
        The tensor of points. Each step ([0, 1, ..., ``n_steps`` - 1])
        is 1/``n_steps`` of the ``shape`` height. The `i`'th step contains
        an (629, 3) matrix of points.

    Examples
    --------
    TODO

    """
    if n_steps < 1:
        raise ValueError('n_steps needs to be greater than 0.')

    parameters = shape.parameters
    height_per_step = parameters['height'] / (n_steps - 1)

    points = np.empty((THETA.size, 3, n_steps))

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

        r0 = optimal_scaling_factor(length=perimeter, c1=c1, c2=c2)

        theta = THETA + twist_linear + twist_oscillating
        radii = summed_cosine(theta=theta, r0=r0, c1=c1, c2=c2)

        points_2d_polar = np.vstack((theta, radii)).transpose()
        points_2d_cartesian = polar_to_cartesian(points=points_2d_polar)

        points[:, :2, step] = points_2d_cartesian
        points[:, 2, step] = height

    return points
