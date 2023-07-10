from __future__ import annotations

from typing import TYPE_CHECKING
from cls.verify import verify_base_perimeter, verify_radius

if TYPE_CHECKING:
    from cls import CLS


def verify(shape: CLS,
           verbose: bool = False) -> bool:
    """Performs all checks on a ``CLS``.

    The checks reduces the risk of print defects.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    verbose : bool, (default=`False`)
        Set to `True` to receive verify messages.

    Returns
    -------
    valid : bool
        `True` if ``shape`` passes all checks.

    """
    valid = verify_base_perimeter(shape=shape,
                                  verbose=verbose)
    if not valid:
        return valid

    valid = verify_radius(shape=shape,
                          verbose=verbose)

    return valid
