from __future__ import annotations

import numpy as np
from scipy.optimize import minimize


def summed_cosine_radii(theta: np.ndarray, r0: float = 1, c1: float = 0,
                        c2: float = 0) -> np.ndarray:
    """Calculates the radii of a summed cosine curve at specified angles.

    Args:
        theta: The angles.
        r0: The scaling factor.
        c1: The 4-lobe parameter.
        c2: The 8-lobe parameter.

    Returns:
        The radii of a summed cosine equation.
    """
    return r0 * (1 + c1 * np.cos(4 * theta) + c2 * np.cos(8 * theta))


def find_scaling_factor(perimeter: float, c1: float = 0, c2: float = 0) -> float:
    """Finds the scaling factor r0 for a CLS curve, given a perimeter, c1, and c2.

    Args:
        perimeter: The desired perimeter.
        c1: The 4-lobe parameter.
        c2: The 8-lobe parameter.

    Returns:
        The approximate scaling factor.
    """
    def absolute_error(r0: float) -> float:
        """Absolute error between a target perimeter and the approximate arc length of a CLS curve.

            Args:
                r0: scaling factor.

            Returns:
                Absolute error.
        """
        return abs(perimeter - summed_cosine_arc_length(r0, c1, c2))

    # Inital guess of answer
    x0 = np.array([38])

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


def summed_cosine_segment_lengths(theta: np.ndarray, r0: float = 1, c1: float = 0,
                                  c2: float = 0) -> np.ndarray:
    """Calculates the lengths of line segements approximating a summed cosine curve.

    For more detail, see the arc length in polar coordinates:
    https://en.wikipedia.org/wiki/Arc_length

    Args:
        theta: The angles.
        r0: The scaling factor.
        c1: The 4-lobe parameter.
        c2: The 8-lobe parameter.

    Returns:
        The length of each line segement.
    """
    d_radius_d_theta = -4 * r0 * (c1 * np.sin(4 * theta) + \
                        2 * c2 * np.sin(8 * theta))
    radii = summed_cosine_radii(theta, r0, c1, c2)
    return np.sqrt(d_radius_d_theta ** 2 + radii ** 2)


def summed_cosine_arc_length(r0: float = 1, c1: float = 0, c2: float = 0,
                             n_steps: int = 50) -> float:
    """Approximate arc length of a summed cosine equation using Simpson's rule.

    For more detail, see the composite Simpson's rule:
    https://en.wikipedia.org/wiki/Simpson%27s_rule#Compoiste_Simpson's_rule.

    Args:
        r0: The scaling factor.
        c1: The 4-lobe parameter.
        c2: The 8-lobe parameter.
        n_steps: The number of discretization steps.

    Returns:
        The approximate arc length of a summed cosine equation.
    """
    if n_steps % 2 == 1:
        raise ValueError('"n_steps" must be an even integer.')

    # Simpson's rule parameters
    a = 0
    b = 2 * np.pi
    h = (b - a) / n_steps

    # Approximate arc length integral using Simpson's rule
    x = np.linspace(a, b, n_steps + 1)
    y = summed_cosine_segment_lengths(theta=x, r0=r0, c1=c1, c2=c2)
    length = h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])

    return length
