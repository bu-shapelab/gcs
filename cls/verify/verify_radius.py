from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np
from cls._utils import _cartesian_to_polar

if TYPE_CHECKING:
    from cls import CLS

# Minimum radius (mm)
MIN_RADIUS = 0.01


def verify_radius(shape: CLS,
                  verbose: bool = False) -> bool:
    """Checks if the ``cls.CLS`` minimum radius is valid.

    This check reduces the risk of print defects by ensuring ``cls.CLS``
    have sufficiently large radii.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    verbose : bool, (default=`False`)
        Set to `True` to receive verify messages.

    Returns
    -------
    valid : bool
       `True` if ``shape`` has a valid radii.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> valid = cls.verify_radius(shape=shape)

    """
    vertices = shape.vertices
    vertices_2d_cartesian = vertices[:, :2]
    vertices_2d_polar = _cartesian_to_polar(points_cartesian=vertices_2d_cartesian)
    radii = vertices_2d_polar[:, 1]
    min_radius = np.amin(radii)

    valid = True
    if min_radius < MIN_RADIUS:
        if verbose:
            print(f'minimum radius ({min_radius}) is less then {MIN_RADIUS}.')
        valid = False
    return valid
