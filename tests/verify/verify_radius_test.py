from __future__ import annotations

import numpy as np
from pytest import approx

from gcs import Cylinder, GCS
from gcs.verify.verify_radius import min_radius, verify_radius
from ..constants import ATOL


def test_min_radius() -> None:
    """Tests for ``gcs.verify.verify_radius.min_radius``.

    """
    # Circle radius
    thetas = np.arange(start=0, stop=2 * np.pi, step=0.01)
    expected_min_r = 2.0
    perimeter = 2 * np.pi * expected_min_r

    min_r = min_radius(thetas=thetas, perimeter=perimeter, c4=0.0, c8=0.0)

    assert min_r == approx(expected=expected_min_r, abs=ATOL)


def test_verify_radius() -> None:
    """Tests for ``gcs.verify.verify_radius``.

    """
    # Valid radius
    shape = Cylinder(height=25, mass=2, thickness=0.5)

    assert verify_radius(shape=shape)

    # Invalid radius
    shape = Cylinder(height=250, mass=0.001, thickness=0.5)

    assert not verify_radius(shape=shape)
