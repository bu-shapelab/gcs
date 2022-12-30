from __future__ import annotations

from typing import TYPE_CHECKING

from .verify_parameters import verify_parameters
from .verify_radius import verify_radius
from .verify_base_perimeter import verify_base_perimeter

if TYPE_CHECKING:
    from cls import CLS


def verify_all(shape: CLS, verbose: bool = False) -> bool:
    """TODO
    """
    valid = verify_parameters(shape=shape, verbose=verbose)
    if not valid:
        if verbose:
            print('TODO')
        return valid
    valid = verify_radius(shape=shape, verbose=verbose)
    if not valid:
        if verbose:
            print('TODO')
        return valid
    valid = verify_base_perimeter(shape=shape, verbose=verbose)
    if not valid:
        if verbose:
            print('TODO')
    return valid
