from __future__ import annotations

import numpy as np
from scipy.optimize import minimize
from scipy.integrate import simpson


def summed_cosine(theta: float,
                  r0: float,
                  c4: float,
                  c8: float) -> float:
    """Summed cosine polar equation.

    Parameters
    ----------
    theta : float
        The angle.
    r0 : float
        The scaling factor.
    c4 : float
        The 4-lobe parameter.
    c8 : float
        The 8-lobe parameter.

    Returns
    -------
    radius : float
        The radius.

    References
    ----------
    .. [1] Overvelde and Bertoldi, *Relating pore shape to the non-linear response of periodic
        elastomeric structures*, Journal of the Mechanics and Physics of Solids, 2014,
        https://doi.org/10.1016/j.jmps.2013.11.014.

    """
    radius = r0 * (1 + c4 * np.cos(4 * theta) + c8 * np.cos(8 * theta))
    return radius


def arc_length(r0: float,
               c4: float,
               c8: float,
               n_steps: int) -> float:
    """Approximate arc length of a summed cosine polar equation using Simpson's rule.

    Parameters
    ----------
    r0 : float
        The scaling factor.
    c4 : float
        The 4-lobe parameter.
    c8 : float
        The 8-lobe parameter.
    n_steps : float
        The number of angular discritization steps.

    Returns
    -------
    length : float
        The approximate arc length.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Arc_length
    .. [2] https://en.wikipedia.org/wiki/Simpson%27s_rule
    .. [3] https://en.wikipedia.org/wiki/Line_element

    """
    theta = np.linspace(0, 2 * np.pi, n_steps)
    radius = np.apply_along_axis(summed_cosine,
                                 axis=0,
                                 arr=theta,
                                 r0=r0,
                                 c4=c4,
                                 c8=c8)

    d_radius_d_theta = -4 * r0 * \
        (c4 * np.sin(4 * theta) + 2 * c8 * np.sin(8 * theta))

    arc_length_element = np.sqrt(d_radius_d_theta ** 2 + radius ** 2)

    integral = simpson(y=arc_length_element,
                       x=theta)

    return integral


def optimal_scaling_factor(length: float,
                           c4: float,
                           c8: float,
                           n_steps: int) -> float:
    """Find the optimal scaling factor (r0) given an arc length, c4, and c8.

    Parameters
    ----------
    length : float
        The arc length.
    c4 : float
        The 4-lobe parameter.
    c8 : float
        The 8-lobe parameter.
    n_steps : float
        The number of angular discritization steps.

    Returns
    -------
    r0 : float
        The optimal scaling factor.

    """
    def absolute_error(r0: np.ndarray) -> float:
        """Absolute error between the current arc length and
        target arc length given a choice of scaling factor (r0).

        """
        # when passed in by minimizer, r0 is a singleton
        r0 = r0.item()
        curr_length = arc_length(r0=r0,
                                 c4=c4,
                                 c8=c8,
                                 n_steps=n_steps)
        error = abs(length - curr_length)
        return error

    # Inital guess of answer
    x0 = np.array([0])

    # Minimize the absolute error to get "best" scaling factors
    result = minimize(fun=absolute_error,
                      x0=x0,
                      method='nelder-mead',
                      options={
                          'xatol': 1e-8,
                          'disp': False,
                      })

    r0 = abs(result.x[0])

    return r0
