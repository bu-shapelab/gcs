from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cls import CLS

# Minimum radius (mm)
MIN_RADIUS = 0.01


def verify_radius(shape: CLS, verbose: bool = False) -> bool:
    """TODO
    """
    radius = shape.min_radius
    valid = True
    if radius < MIN_RADIUS:
        if verbose:
            print('TODO')
        valid = False
    return valid
