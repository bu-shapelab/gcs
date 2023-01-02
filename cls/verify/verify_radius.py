from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cls import CLS

# Minimum radius (mm)
MIN_RADIUS = 0.01


def verify_radius(shape: CLS, verbose: bool = False) -> bool:
    """Verifies the validity of a CLS minimum radius.

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
        `True` if ``shape`` has a valid minimum radius, `False` otherwise.

    Examples
    --------
    TODO

    """
    radius = shape.min_radius
    valid = True
    if radius < MIN_RADIUS:
        if verbose:
            print('TODO')
        valid = False
    return valid
