from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np
from cls.utils import optimal_scaling_factor, summed_cosine

if TYPE_CHECKING:
    from cls import CLS

# Minimum radius (mm)
MIN_RADIUS = 0.01


def verify_radius(shape: CLS,
                  verbose: bool = False) -> bool:
    """Checks if the ``cls.CLS`` minimum radius is valid.

    This check reduces the risk of print defects by ensuring a ``CLS``
    print paths are well spaced.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    verbose : bool, (default=`False`)
        Set to `True` to receive verify messages.

    Returns
    -------
    valid : bool
       `True` if ``shape`` passes the radius check.

    """
    parameters = shape.parameters

    thetas = np.arange(start=0,
                       stop=2 * np.pi,
                       step=parameters['d_theta'])

    r0_base = optimal_scaling_factor(length=shape.base_perimeter,
                                     c1=parameters['c1_base'],
                                     c2=parameters['c2_base'],
                                     n_steps=thetas.size)

    radii_base = np.apply_along_axis(func1d=summed_cosine,
                                     axis=0,
                                     arr=thetas,
                                     r0=r0_base,
                                     c1=parameters['c1_base'],
                                     c2=parameters['c2_base'])

    if np.min(radii_base) < MIN_RADIUS:
        if verbose:
            print(f'minimum base radius ({np.min(radii_base)}) is less then {MIN_RADIUS}.')
        return False

    r0_top = optimal_scaling_factor(length=shape.top_perimeter,
                                    c1=parameters['c1_top'],
                                    c2=parameters['c2_top'],
                                    n_steps=thetas.size)

    radii_top = np.apply_along_axis(func1d=summed_cosine,
                                    axis=0,
                                    arr=thetas,
                                    r0=r0_top,
                                    c1=parameters['c1_top'],
                                    c2=parameters['c2_top'])

    if np.min(radii_top) < MIN_RADIUS:
        if verbose:
            print(f'minimum top radius ({np.min(radii_top)}) is less then {MIN_RADIUS}.')
        return False

    return True
