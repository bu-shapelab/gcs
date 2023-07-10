from __future__ import annotations

from typing import TYPE_CHECKING
from gcs.verify import verify_base_perimeter, verify_radius

if TYPE_CHECKING:
    from gcs import GCS


def verify(shape: GCS,
           verbose: bool = False) -> bool:
    """Performs all checks on a ``GCS``.

    The checks reduces the risk of print defects.

    Parameters
    ----------
    shape : GCS.gcs
        The GCS.
    verbose : bool, (default=`False`)
        Set to `True` to receive verify messages.

    Returns
    -------
    valid : bool
        `True` if ``shape`` passes all checks.

    Examples
    --------
    >>> shape = gcs.GCS(...)
    >>> check = gcs.verify.verify(shape=shape)

    >>> shape = gcs.GCS(...)
    >>> check = shape.valid

    """
    valid = verify_base_perimeter(shape=shape,
                                  verbose=verbose)
    if not valid:
        return valid

    valid = verify_radius(shape=shape,
                          verbose=verbose)

    return valid
