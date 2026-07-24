from __future__ import annotations

import numpy as np
from pytest import approx

from gcs.geometry.summed_cosine import summed_cosine
from ..constants import ATOL


def test_summed_cosine() -> None:
    """Tests for ``gcs.geometry.summed_cosine``.

    """
    # Scalar angle
    theta = np.pi / 4
    r0 = 2.0
    c4 = 0.25
    c8 = -0.1

    r = summed_cosine(theta=theta, r0=r0, c4=c4, c8=c8)

    expected = r0 * (1 + c4 * np.cos(4 * theta) + c8 * np.cos(8 * theta))

    assert r == approx(expected=expected, abs=ATOL)

    # Array of angles
    theta = np.linspace(start=0.0, stop=2 * np.pi, num=8)
    r0 = 1.5
    c4 = 0.2
    c8 = -0.05

    r = summed_cosine(theta=theta, r0=r0, c4=c4, c8=c8)

    expected = r0 * (1 + c4 * np.cos(4 * theta) + c8 * np.cos(8 * theta))

    np.testing.assert_allclose(actual=r, desired=expected, atol=ATOL)
