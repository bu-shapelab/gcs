from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..shape import GCS

# Minimum base perimeter (mm)
MIN_BASE_PERIMETER = 30


def verify_base_perimeter(shape: GCS) -> bool:
    """Checks whether a GCS has a sufficiently large base perimeter.

    This check reduces the risk of print defects by ensuring
    a sufficiently large base for adhesion.

    Parameters
    ----------
    shape : gcs.GCS
        GCS shape.

    Returns
    -------
    valid : bool
        `True` if ``shape`` passes the base perimeter check.

    Examples
    --------
    >>> shape = gcs.Cylinder(height=25, mass=2, thickness=0.5)
    >>> gcs.verify.verify_base_perimeter(shape=shape)
    True

    """
    return shape.base_perimeter >= MIN_BASE_PERIMETER
