from __future__ import annotations

import numpy as np


def summed_cosine(theta: float | np.ndarray, r0: float, c4: float, c8: float) -> float | np.ndarray:
    """Summed cosine polar equation.

    Parameters
    ----------
    theta : {float, (N,) numpy.ndarray}
        Angle(s).
    r0 : float
        Scaling factor.
    c4 : float
        4-lobe parameter.
    c8 : float
        8-lobe parameter.

    Returns
    -------
    r : {float, (N,) numpy.ndarray}
        Radius value(s).

    References
    ----------
    .. [1] Overvelde and Bertoldi, *Relating pore shape to the non-linear response of periodic
        elastomeric structures*, Journal of the Mechanics and Physics of Solids, 2014,
        https://doi.org/10.1016/j.jmps.2013.11.014.

    """
    return r0 * (1 + c4 * np.cos(4 * theta) + c8 * np.cos(8 * theta))
