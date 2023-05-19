from __future__ import annotations

from typing import TYPE_CHECKING
from cls.verify import verify_parameters, verify_base_perimeter, verify_radius

if TYPE_CHECKING:
    from cls import CLS


def verify(shape: CLS,
           verbose: bool = False) -> bool:
    """Performs all validity checks on a ``cls.CLS``.

    This check reduces the risk of print defects.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    verbose : bool, (default=`False`)
        Set to `True` to receive verify messages.

    Returns
    -------
    valid : bool
        `True` if ``shape`` is valid.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> valid = cls.verify_base_perimeter(shape=shape)

    """
    valid = True
    if verify_parameters(shape=shape, verbose=verbose) is False:
        valid = False
    elif verify_base_perimeter(shape=shape, verbose=verbose) is False:
        valid = False
    elif verify_radius(shape=shape, verbose=verbose) is False:
        valid = False
    return valid
