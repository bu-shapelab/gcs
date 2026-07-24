from __future__ import annotations

import numpy as np

from gcs.geometry.coordinates import cart2pol, pol2cart
from ..constants import ATOL


def test_pol2cart() -> None:
    """Tests for ``gcs.geometry.pol2cart``.

    """
    # Axes-aligned points
    r = np.array([1.0, 2.0, 3.0])
    theta = np.array([0.0, np.pi / 2, np.pi])

    x, y = pol2cart(r=r, theta=theta)

    np.testing.assert_allclose(actual=x, desired=np.array([1.0, 0.0, -3.0]), atol=ATOL)
    np.testing.assert_allclose(actual=y, desired=np.array([0.0, 2.0, 0.0]), atol=ATOL)

    # Round-trip points
    r = np.linspace(start=0.1, stop=2.0, num=10)
    theta = np.linspace(start=-np.pi / 2, stop=np.pi / 2, num=10)

    x, y = pol2cart(r=r, theta=theta)

    np.testing.assert_allclose(actual=x, desired=r * np.cos(theta), atol=ATOL)
    np.testing.assert_allclose(actual=y, desired=r * np.sin(theta), atol=ATOL)


def test_cart2pol() -> None:
    """Tests for ``gcs.geometry.cart2pol``.

    """
    # Axes-aligned points
    x = np.array([1.0, 0.0, -3.0])
    y = np.array([0.0, 2.0, 0.0])

    r, theta = cart2pol(x=x, y=y)

    np.testing.assert_allclose(actual=r, desired=np.array([1.0, 2.0, 3.0]), atol=ATOL)
    np.testing.assert_allclose(actual=theta, desired=np.array([0.0, np.pi / 2, np.pi]), atol=ATOL)

    # Round-trip points
    r = np.linspace(start=0.1, stop=2.0, num=10)
    theta = np.linspace(start=-np.pi / 2, stop=np.pi / 2, num=10)

    x, y = pol2cart(r=r, theta=theta)
    recovered_r, recovered_theta = cart2pol(x=x, y=y)

    np.testing.assert_allclose(actual=recovered_r, desired=r, atol=ATOL)
    np.testing.assert_allclose(actual=recovered_theta, desired=theta, atol=ATOL)
