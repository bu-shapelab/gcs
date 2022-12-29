from __future__ import annotations

import numpy as np
from scipy.optimize import minimize
from .integration import simpsons_rule


def summed_cosine(theta: np.ndarray, r0: float, c1: float, c2: float) -> np.ndarray:
    """TODO Calculates the radii of a summed cosine polar equation.

    Args:
        theta: A vector of angles.
        r0: The scaling factor.
        c1: The 4-lobe parameter.
        c2: The 8-lobe parameter.

    Returns:
        A vector of radii.
    """
    if not isinstance(theta, np.ndarray):
        raise TypeError('TODO')

    theta = theta.squeeze()

    if theta.ndim != 1:
        raise ValueError('TODO')

    if not isinstance(r0, (int, float)):
        raise TypeError('TODO')

    if not isinstance(c1, (int, float)):
        raise TypeError('TODO')

    if not isinstance(c2, (int, float)):
        raise TypeError('TODO')

    return r0 * (1 + c1 * np.cos(4 * theta) + c2 * np.cos(8 * theta))


def arc_length(r0: float, c1: float, c2: float, n_steps: int = 50) -> float:
    """TODO Approximate arc length of a summed cosine polar equation.

    Args:
        r0: The scaling factor.
        c1: The 4-lobe parameter.
        c2: The 8-lobe parameter.
        n_steps: Number of step to discritize the summed cosine equation.

    Returns:
        The approximate arc length.
    """
    if not isinstance(r0, (int, float)):
        raise TypeError('TODO')

    if not isinstance(c1, (int, float)):
        raise TypeError('TODO')

    if not isinstance(c2, (int, float)):
        raise TypeError('TODO')

    if not isinstance(n_steps, int):
        raise TypeError('TODO')

    if n_steps < 1:
        raise ValueError('TODO')

    theta = np.linspace(0, 2 * np.pi, n_steps + 1)
    radii = summed_cosine(theta, r0, c1, c2)

    d_radius_d_theta = -4 * r0 * \
        (c1 * np.sin(4 * theta) + 2 * c2 * np.sin(8 * theta))

    arc_length_function = np.sqrt(d_radius_d_theta ** 2 + radii ** 2)

    # approximate integral from 0 -> 2pi of arc_length_function using Simpson's rule
    integral = simpsons_rule(arc_length_function, 0, 2 * np.pi)

    return integral


def optimal_scaling_factor(perimeter: float, c1: float, c2: float) -> float:
    """TODO
    """
    if not isinstance(perimeter, (int, float)):
        raise TypeError('TODO')

    if perimeter <= 0:
        raise ValueError('TODO')

    if not isinstance(c1, (int, float)):
        raise TypeError('TODO')

    if not isinstance(c2, (int, float)):
        raise TypeError('TODO')

    def absolute_error(r0: np.ndarray) -> float:
        """TODO
        """
        # when passed in by minimizer, r0 is a singleton
        r0 = r0.item()
        return abs(perimeter - arc_length(r0, c1, c2))

    # Inital guess of answer
    x0 = np.array([0])

    # Optimization method and options
    method = 'nelder-mead'
    options = {
        'xatol': 1e-8,
        'disp': False,
    }

    # Minimize the absolute error to get "best" scaling factors
    result = minimize(fun=absolute_error,
                      x0=x0,
                      method=method,
                      options=options)

    r0 = abs(result.x[0])

    return r0
