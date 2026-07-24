from __future__ import annotations

import numpy as np
from scipy.optimize import minimize
from scipy.integrate import simpson

from .summed_cosine import summed_cosine


def arc_length(r0: float, c4: float, c8: float, n_steps: int) -> float:
    """Approximate arc length of a summed cosine polar equation using Simpson's rule.

    Parameters
    ----------
    r0 : float
        Scaling factor.
    c4 : float
        4-lobe parameter.
    c8 : float
        8-lobe parameter.
    n_steps : float
        Number of angular discritization steps.

    Returns
    -------
    length : float
       Approximate arc length.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Arc_length
    .. [2] https://en.wikipedia.org/wiki/Simpson%27s_rule
    .. [3] https://en.wikipedia.org/wiki/Line_element

    """
    theta = np.linspace(start=0, stop=2 * np.pi, num=n_steps)
    r = np.apply_along_axis(func1d=summed_cosine, axis=0, arr=theta, r0=r0, c4=c4, c8=c8)

    d_radius_d_theta = -4 * r0 * (c4 * np.sin(4 * theta) + 2 * c8 * np.sin(8 * theta))

    arc_length_element = np.hypot(d_radius_d_theta, r)

    return simpson(y=arc_length_element, x=theta)


def optimal_scaling_factor(length: float, c4: float, c8: float, n_steps: int) -> float:
    """Finds the optimal summed-cosine scale factor that produces a target arc length.

    Parameters
    ----------
    length : float
        Target arc length.
    c4 : float
        4-lobe parameter.
    c8 : float
        8-lobe parameter.
    n_steps : float
        Number of angular discritization steps.

    Returns
    -------
    r0 : float
        Optimal scaling factor.

    """
    def absolute_error(r0: np.ndarray) -> float:
        """Absolute difference between the target and computed arc lengths.

        Parameters
        ----------
        r0 : (1,) numpy.ndarray
            Candidate scaling factor.

        Returns
        -------
        error : float
            Absolute difference between the target and computed arc lengths.

        """
        curr_length = arc_length(r0=r0.item(), c4=c4, c8=c8, n_steps=n_steps)

        return abs(length - curr_length)

    # Inital scale factor set to 0
    x0 = np.array([0])

    # Minimize the absolute error to get "best" scaling factors
    result = minimize(fun=absolute_error,
                      x0=x0,
                      method='nelder-mead',
                      options={
                          'xatol': 1e-8,
                          'disp': False,
                      })

    return abs(result.x[0])
