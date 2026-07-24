from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from ..geometry.polar_curves import optimal_scaling_factor
from ..geometry.summed_cosine import summed_cosine

if TYPE_CHECKING:
    from ..shape import GCS

# Minimum radius (mm)
MIN_RADIUS = 0.01


def min_radius(thetas: np.ndarray, perimeter: float, c4: float, c8: float) -> float:
    """Computes the minimum radius of a summed cosine polar equation.

    Parameters
    ----------
    thetas : (N,) numpy.ndarray
        Angles.
    perimeter : float
        Target perimeter.
    c4 : float
        4-lobe parameter.
    c8 : float
        8-lobe parameter.
        
    Returns
    -------
    r : float
        Minimum radius.

    """
    r0 = optimal_scaling_factor(length=perimeter, c4=c4, c8=c8, n_steps=thetas.size)

    rs = summed_cosine(theta=thetas, r0=r0, c4=c4, c8=c8)

    return np.min(rs)


def verify_radius(shape: GCS) -> bool:
    """Checks whether the minimum radius stays above a printable threshold.

    This check reduces the risk of print defects by ensuring print
    paths are well spaced.

    Parameters
    ----------
    shape : gcs.GCS
        GCS shape.

    Returns
    -------
    valid : bool
       `True` if ``shape`` passes the radius check.

    Examples
    --------
    >>> shape = gcs.Cylinder(height=25, mass=2, thickness=0.5)
    >>> gcs.verify.verify_radius(shape=shape)
    True

    """
    parameters = shape.parameters

    thetas = np.arange(start=0, stop=2 * np.pi, step=parameters['theta_step'])

    min_base_r = min_radius(thetas=thetas,
                            perimeter=shape.base_perimeter,
                            c4=parameters['c4_base'],
                            c8=parameters['c8_base'])

    min_top_r = min_radius(thetas=thetas,
                           perimeter=shape.top_perimeter,
                           c4=parameters['c4_top'],
                           c8=parameters['c8_top'])

    min_r = np.min([min_base_r, min_top_r])

    return min_r >= MIN_RADIUS
