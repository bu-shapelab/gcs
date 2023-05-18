from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cls import CLS

# Minimum base perimeter (mm)
MIN_BASE_PERIMETER = 30


def verify_base_perimeter(shape: CLS,
                          verbose: bool = False) -> bool:
    """Checks if the ``cls.CLS`` base perimeter is valid.

    This check reduces the risk of print defects by ensuring ``cls.CLS``
    have a sufficiently large base.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    verbose : bool, (default=`False`)
        Set to `True` to receive verify messages.

    Returns
    -------
    valid : bool
        `True` if ``shape`` has a valid base perimeter.

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
