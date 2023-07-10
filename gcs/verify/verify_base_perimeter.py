from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gcs import GCS

# Minimum base perimeter (mm)
MIN_BASE_PERIMETER = 30


def verify_base_perimeter(shape: GCS,
                          verbose: bool = False) -> bool:
    """Checks if the ``GCS`` base perimeter is valid.

    This check reduces the risk of print defects by ensuring a ``GCS``
    has a sufficiently large base for adhesion.

    Parameters
    ----------
    shape : GCS.gcs
        The GCS.
    verbose : bool, (default=`False`)
        Set to `True` to receive verify messages.

    Returns
    -------
    valid : bool
        `True` if ``shape`` passes the base perimeter check.

    Examples
    --------
    >>> shape = gcs.GCS(...)
    >>> check = gcs.verify.verify_base_perimeter(shape=shape)

    >>> shape = gcs.GCS(...)
    >>> check = shape.valid_base_perimeter

    """
    perimeter = shape.base_perimeter
    valid = True
    if perimeter < MIN_BASE_PERIMETER:
        if verbose:
            print(f'base perimeter ({perimeter}) is less then {MIN_BASE_PERIMETER}.')
        valid = False
    return valid