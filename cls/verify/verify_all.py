from __future__ import annotations

from typing import TYPE_CHECKING

from .verify_parameters import verify_parameters
from .verify_radius import verify_radius
from .verify_base_perimeter import verify_base_perimeter

if TYPE_CHECKING:
    from cls import CLS


def verify_all(shape: CLS, verbose: bool = False) -> bool:
    """Performs all validity checks on a CLS.

    The validity checks are to minimize the risk of printing failures.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    verbose : bool, (default=False)
        Set to `True` to print validity messages.

    Returns
    -------
    valid : bool
        `True` if ``shape`` is valid, `False` otherwise.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> valid = cls.verify_all(shape=shape)

    >>> shape = cls.CLS()
    >>> valid = shape.valid

    """
    valid = verify_parameters(shape=shape, verbose=verbose)
    if not valid:
        return valid
    valid = verify_radius(shape=shape, verbose=verbose)
    if not valid:
        return valid
    valid = verify_base_perimeter(shape=shape, verbose=verbose)
    return valid
