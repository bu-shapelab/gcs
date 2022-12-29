from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cls import CLS

# Minimum base perimeter (mm)
MIN_BASE_PERIMETER = 30


def verify_base_perimeter(shape: CLS, verbose: bool = False) -> bool:
    """TODO
    """
    perimeter = shape.base_perimeter
    valid = True
    if perimeter < MIN_BASE_PERIMETER:
        if verbose:
            print('TODO')
        valid = False
    return valid
