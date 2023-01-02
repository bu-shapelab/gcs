from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cls import CLS

# Minimum base perimeter (mm)
MIN_BASE_PERIMETER = 30


def verify_base_perimeter(shape: CLS, verbose: bool = False) -> bool:
    """Verifies the validity of a CLS base perimeter.

    This validity check is to minimize the risk of printing failures.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    verbose : bool, (default=False)
        Set to `True` to print validity messages.

    Returns
    -------
    valid : bool
        `True` if ``shape`` has a valid base perimeter, `False` otherwise.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> valid = cls.verify_base_perimeter(shape=shape)

    """
    perimeter = shape.base_perimeter
    valid = True
    if perimeter < MIN_BASE_PERIMETER:
        if verbose:
            print(f'base perimeter ({perimeter}) is less then {MIN_BASE_PERIMETER}.')
        valid = False
    return valid
