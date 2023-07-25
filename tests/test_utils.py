from __future__ import annotations

import numpy as np
from gcs.utils import pol2cart, cart2pol, offset_radius, self_intersection


class TestUtils:
    """Tests for:
        - coordinates.py
        - polar_curves.py

    """

    def test_coordinates(self):
        """Test ``gcs.utils.pol2cart`` and ``gcs.utils.cart2pol`` functions.

        """
        radius = np.linspace(start=0,
                             stop=1,
                             num=10)
        theta = np.linspace(start=0,
                            stop=1,
                            num=10)

        x, y = pol2cart(radius=radius,
                        theta=theta)

        np.testing.assert_almost_equal(actual=x,
                                       desired=radius * np.cos(theta))
        np.testing.assert_almost_equal(actual=y,
                                       desired=radius * np.sin(theta))

        radius2, theta2 = cart2pol(x=x,
                                   y=y)

        np.testing.assert_almost_equal(actual=radius2,
                                       desired=radius)
        np.testing.assert_almost_equal(actual=theta2,
                                       desired=theta)

    def test_offset_curve(self):
        """Test ``gcs.utils.offset_curve`` function.

        """
        # circle
        theta = np.linspace(0, 2 * np.pi, 100)
        radius = np.ones_like(theta)

        radius_offset = offset_radius(radius=radius,
                                      theta=theta,
                                      offset=0)

        np.testing.assert_almost_equal(actual=radius_offset,
                                       desired=radius)

        radius_offset = offset_radius(radius=radius,
                                      theta=theta,
                                      offset=1)

        np.testing.assert_almost_equal(actual=radius_offset,
                                       desired=2 * radius)

        radius_offset = offset_radius(radius=radius,
                                      theta=theta,
                                      offset=-0.5)

        np.testing.assert_almost_equal(actual=radius_offset,
                                       desired=0.5 * radius)

    def test_self_intersection(self):
        """Test ``gcs.utils.self_intersection`` function.

        """
        t = np.linspace(0, 2 * np.pi, 100)

        # circle
        x = np.cos(t)
        y = np.sin(t)
        intersect = self_intersection(x=x,
                                      y=y)

        assert intersect is False

        # figure 8
        x = np.sin(t)
        y = np.sin(t) * np.cos(t)
        intersect = self_intersection(x=x,
                                      y=y)

        assert intersect is True
