from __future__ import annotations

import numpy as np


def simpsons_rule(y: np.ndarray, a: float, b: float) -> float:
    """Calculates the integral of ``y = f(x)`` from ``a`` to ``b``
    using Simpson's rule.

    Parameters
    ----------
    y : np.ndarray
        A vector of function values. Simpson's rule requires ``y`` to be of even length.
    a : float
        The low value in the integration range [``a``, ``b``].
    b : float
        The high value in the integration range [``a``, ``b``].

    Returns
    -------
    integral : float
        The integral value.

    Raises
    ------
    TypeError
        If ``y`` is not an np.ndarray.
        If ``a`` is not a number.
        If ``b`` is not a number.
    ValueError
        If ``y`` is not a vector of even length.
        If ``a``>``b``.

    References
    ----------
    .. [1] Wikipedia page: https://en.wikipedia.org/wiki/Simpson%27s_rule

    """
    if not isinstance(y, np.ndarray):
        raise TypeError('y needs to be an np.ndarray.')

    y = y.squeeze()

    if y.ndim > 1:
        raise ValueError('y needs to be a vector.')

    if (y.size - 1) % 2 == 1:
        raise ValueError('y needs to be a vector of even length.')

    if not isinstance(a, (int, float)):
        raise TypeError('a needs to be a number.')

    if not isinstance(b, (int, float)):
        raise TypeError('b needs to be a number.')

    if a > b:
        raise ValueError('a needs to be less than (or equal to) b.')

    n_steps = y.size
    h = (b - a) / n_steps
    integral = h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])

    return integral
