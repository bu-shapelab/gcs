from __future__ import annotations

import numpy as np
from scipy.optimize import minimize

from .integration import simpsons_rule


def summed_cosine(theta: np.ndarray, r0: float, c1: float, c2: float) -> np.ndarray:
    """Calculates the radii of a summed cosine polar equation.

    The summed cosine equation is inspired by [1].

    Parameters
    ----------
    theta : np.ndarray
        A vector of angles.
    r0 : float
        The scaling factor.
    c1 : float
        The 4-lobe parameter.
    c2 : float
        The 8-lobe parameter.

    Returns
    -------
    theta : np.ndarray
        A vector of radii.

    Raises
    ------
    TypeError
        If ``theta`` is not an np.ndarray.
        If ``r0`` is not a number.
        If ``c1`` is not a number.
        If ``c2`` is not a number.
    ValueError
        If ``theta`` is not a vector.

    References
    ----------
    .. [1] Overvelde and Bertoldi, *Relating pore shape to the non-linear response of periodic
           elastomeric structures*, Journal of the Mechanics and Physics of Solids, 2014

    """
    if not isinstance(theta, np.ndarray):
        raise TypeError('theta needs to be an np.ndarray.')

    theta = theta.squeeze()

    if theta.ndim != 1:
        raise ValueError('theta needs to be a vector.')

    if not isinstance(r0, (int, float)):
        raise TypeError('r0 needs to be a number.')

    if not isinstance(c1, (int, float)):
        raise TypeError('c1 needs to be a number.')

    if not isinstance(c2, (int, float)):
        raise TypeError('c2 needs to be a number.')

    return r0 * (1 + c1 * np.cos(4 * theta) + c2 * np.cos(8 * theta))


def arc_length(r0: float, c1: float, c2: float, n_steps: int = 50) -> float:
    """Approximate arc length of a summed cosine polar equation.

    Parameters
    ----------
    r0 : float
        The scaling factor.
    c1 : float
        The 4-lobe parameter.
    c2 : float
        The 8-lobe parameter.
    n_steps : float (default=50)
        The number of step to discritize the summed cosine equation.

    Returns
    -------
    length : float
        The approximate arc length.

    Raises
    ------
    TypeError
        If ``r0`` is not a number.
        If ``c1`` is not a number.
        If ``c2`` is not a number.
        If ``n_steps`` is not an integer.
    ValueError
        If ``n_steps`` is not positive.

    References
    ----------
    .. [1] Wikipedia page: https://en.wikipedia.org/wiki/Arc_length

    """
    if not isinstance(r0, (int, float)):
        raise TypeError('r0 needs to be a number.')

    if not isinstance(c1, (int, float)):
        raise TypeError('c1 needs to be a number.')

    if not isinstance(c2, (int, float)):
        raise TypeError('c2 needs to be a number.')

    if not isinstance(n_steps, int):
        raise TypeError('n_steps needs to be an integer.')

    if n_steps < 1:
        raise ValueError('n_steps needs to be positive.')

    theta = np.linspace(0, 2 * np.pi, n_steps + 1)
    radii = summed_cosine(theta, r0, c1, c2)

    d_radius_d_theta = -4 * r0 * \
        (c1 * np.sin(4 * theta) + 2 * c2 * np.sin(8 * theta))

    arc_length_function = np.sqrt(d_radius_d_theta ** 2 + radii ** 2)

    # approximate integral from 0 -> 2pi of arc_length_function using Simpson's rule
    integral = simpsons_rule(arc_length_function, 0, 2 * np.pi)

    return integral


def optimal_scaling_factor(length: float, c1: float, c2: float) -> float:
    """Approximate arc length of a summed cosine polar equation.

    Parameters
    ----------
    perimeter : float
        The desired arc length for the summed cosine curve.
    c1 : float
        The 4-lobe parameter.
    c2 : float
        The 8-lobe parameter.

    Returns
    -------
    r0 : float
        The optimized scaling factor.

    Raises
    ------
    TypeError
        If ``length`` is not a number.
        If ``c1`` is not a number.
        If ``c2`` is not a number.
    ValueError
        If ``length`` is not positive.

    """
    if not isinstance(length, (int, float)):
        raise TypeError('length needs to be a number.')

    if length <= 0:
        raise ValueError('length needs to be positive.')

    if not isinstance(c1, (int, float)):
        raise TypeError('c1 needs to be a number.')

    if not isinstance(c2, (int, float)):
        raise TypeError('c2 needs to be a number.')

    def absolute_error(r0: np.ndarray) -> float:
        """TODO
        """
        # when passed in by minimizer, r0 is a singleton
        r0 = r0.item()
        return abs(length - arc_length(r0, c1, c2))

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
