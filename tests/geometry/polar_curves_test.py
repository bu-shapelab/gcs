from __future__ import annotations

import numpy as np
from pytest import approx

from gcs.geometry.polar_curves import arc_length, optimal_scaling_factor
from ..constants import ATOL


def test_arc_length() -> None:
    """Tests for ``gcs.geometry.arc_length``.

    """
    # Circle perimeter
    r0 = 2.5
    expected_perimeter = 2 * np.pi * r0

    length = arc_length(r0=r0, c4=0.0, c8=0.0, n_steps=100)

    assert length == approx(expected=expected_perimeter, abs=ATOL)


def test_optimal_scaling_factor() -> None:
    """Tests for ``gcs.geometry.optimal_scaling_factor``.

    """
    # Circle radius recovery
    expected_r0 = 3.0
    target_length = 2 * np.pi * expected_r0

    r0 = optimal_scaling_factor(length=target_length, c4=0.0, c8=0.0, n_steps=100)

    assert r0 == approx(expected=expected_r0, abs=ATOL)

    # Lobed profile radius recovery
    expected_r0 = 1.75
    c4 = 0.2
    c8 = -0.05
    n_steps = 100
    target_length = arc_length(r0=expected_r0, c4=c4, c8=c8, n_steps=n_steps)

    r0 = optimal_scaling_factor(length=target_length, c4=c4, c8=c8, n_steps=n_steps)

    assert r0 == approx(expected=expected_r0, abs=ATOL)
