from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np
from gcs.utils import optimal_scaling_factor, summed_cosine

if TYPE_CHECKING:
    import gcs

# Minimum radius (mm)
MIN_RADIUS = 0.01


def verify_radius(shape: gcs.GCS,
                  verbose: bool = False) -> bool:
    """Checks if the GCS minimum radius is valid.

    This check reduces the risk of print defects by ensuring print
    paths are well spaced.

    Parameters
    ----------
    shape : GCS.gcs
        The GCS.
    verbose : bool, (default=`False`)
        Set to `True` to receive verify messages.

    Returns
    -------
    valid : bool
       `True` if ``shape`` passes the radius check.

    Examples
    --------
    >>> shape = gcs.GCS(...)
    >>> check = gcs.verify.verify_radius(shape=shape)

    >>> shape = gcs.GCS(...)
    >>> check = shape.valid_radius

    """
    parameters = shape.parameters

    thetas = np.arange(start=0,
                       stop=2 * np.pi,
                       step=parameters['d_theta'])

    r0 = optimal_scaling_factor(length=shape.base_perimeter,
                                c4=parameters['c4_base'],
                                c8=parameters['c8_base'],
                                n_steps=thetas.size)

    radii = np.apply_along_axis(func1d=summed_cosine,
                                axis=0,
                                arr=thetas,
                                r0=r0,
                                c4=parameters['c4_base'],
                                c8=parameters['c8_base'])

    min_base_radius = np.min(radii)

    r0 = optimal_scaling_factor(length=shape.top_perimeter,
                                c4=parameters['c4_top'],
                                c8=parameters['c8_top'],
                                n_steps=thetas.size)

    radii = np.apply_along_axis(func1d=summed_cosine,
                                axis=0,
                                arr=thetas,
                                r0=r0,
                                c4=parameters['c4_top'],
                                c8=parameters['c8_top'])

    min_top_radius = np.min(radii)

    min_radius = np.min([min_base_radius, min_top_radius])
    valid = bool(min_radius >= MIN_RADIUS)

    if verbose:
        if not valid:
            print(f'minimum radius ({min_radius}) is less then {MIN_RADIUS}.')

    return valid
