from __future__ import annotations

from gcs import Cylinder
from gcs.verify import verify


def test_verify() -> None:
    """Tests for ``gcs.verify.verify``.

    """
    # Valid shape
    shape = Cylinder(height=25, mass=2, thickness=0.5)

    assert verify(shape=shape)

    # Invalid base perimeter
    shape = Cylinder(height=25, mass=0.1, thickness=0.5)

    assert not verify(shape=shape)

    # Invalid radius
    shape = Cylinder(height=250, mass=0.001, thickness=0.5)

    assert not verify(shape=shape)
