from __future__ import annotations

import numpy as np


def simpsons_rule(y: np.ndarray, a: float, b: float) -> float:
    """TODO Approximate the integral of y = f(x) from a -> b using Simpson's rule.

    For more detail, see the composite Simpson's rule:
    https://en.wikipedia.org/wiki/Simpson%27s_rule#Compoiste_Simpson's_rule.

    Args:
        y: A vector of function values.
           Note, Simpson's rule requires y to be of even length.
        a: The low value in the integration range [a, b].
        b: The high value in the integration range [a, b].

    Returns:
        The approximate integral value.
    """
    if not isinstance(y, np.ndarray):
        raise TypeError('TODO')

    y = y.squeeze()

    if y.ndim > 1:
        raise ValueError('TODO')

    if (y.size - 1) % 2 == 1:
        raise ValueError('TODO')

    if not isinstance(a, (int, float)):
        raise TypeError('TODO')

    if not isinstance(b, (int, float)):
        raise TypeError('TODO')

    if a > b:
        raise ValueError('TODO')

    n_steps = y.size
    h = (b - a) / n_steps
    length = h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])

    return length
