from __future__ import annotations

from typing import TYPE_CHECKING

from .verify_base_perimeter import verify_base_perimeter
from .verify_radius import verify_radius

if TYPE_CHECKING:
    from ..shape import GCS


def verify(shape: GCS) -> bool:
    """Runs all verification checks for a GCS.

    The checks reduces the risk of print defects.

    Parameters
    ----------
    shape : gcs.GCS
        GCS shape.

    Returns
    -------
    valid : bool
        `True` if ``shape`` passes all verification checks.

    Examples
    --------
    >>> shape = gcs.Cylinder(height=25, mass=2, thickness=0.5)
    >>> gcs.verify.verify(shape=shape)
    True

    """
    return verify_base_perimeter(shape=shape) and verify_radius(shape=shape)
