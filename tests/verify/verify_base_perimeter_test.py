from __future__ import annotations

from gcs import Cylinder
from gcs.verify import verify_base_perimeter


def test_verify_base_perimeter() -> None:
    """Tests for ``gcs.verify.verify_base_perimeter``.

    """
    # Valid base perimeter
    shape = Cylinder(height=25, mass=2, thickness=0.5)

    assert verify_base_perimeter(shape=shape) is True

    # Invalid base perimeter
    shape = Cylinder(height=25, mass=0.1, thickness=0.5)

    assert verify_base_perimeter(shape=shape) is False
