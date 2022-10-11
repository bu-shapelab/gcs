import unittest
import numpy as np
from utils import polar_to_cartesian, cartesian_to_polar


class TestCoordinates(unittest.TestCase):
    """Unit tests for `utils/coordinates.py` module.
    """
    # polar_to_cartesian unit tests
    def test_polar_to_cartesian_invalid_type(self):
        """Test `polar_to_cartesian` function on invalid argument types.
        """
        theta = np.array([1])
        radii = 1

        with self.assertRaises(TypeError):
            polar_to_cartesian(theta, radii)

    def test_polar_to_cartesian_invalid_values(self):
        """Test `polar_to_cartesian` function on invalid argument values.
        """
        theta = np.array([1])
        radii = np.array([[1, 2],
                          [3, 4]])

        with self.assertRaises(ValueError):
            polar_to_cartesian(theta, radii)

    def test_polar_to_cartesian(self):
        """Test `polar_to_cartesian` function.
        """
        theta = np.array([np.pi / 3, np.pi / 5])
        radii = np.array([1, -0.5])

        points = polar_to_cartesian(theta, radii)
        points_correct = np.array([[1 / 2, np.sqrt(3) / 2],
                                   [-0.40450, -0.29389]])

        np.testing.assert_almost_equal(points, points_correct, decimal=4)

    # cartesian_to_polar unit tests
    def test_cartesian_to_polar_invalid_type(self):
        """Test `cartesian_to_polar` function on invalid argument types.
        """
        points = [1, 0]

        with self.assertRaises(TypeError):
            cartesian_to_polar(points)

    def test_cartesian_to_polar_invalid_values(self):
        """Test `cartesian_to_polar` function on invalid argument values.
        """
        points = np.array([[1, 0, 0],
                           [-0.43, -0.52, 0]])

        with self.assertRaises(ValueError):
            cartesian_to_polar(points)

    def test_cartesian_to_polar(self):
        """Test `cartesian_to_polar` function.
        """
        points = np.array([[1, 0],
                           [-0.43, -0.55]])

        theta, radii = cartesian_to_polar(points)

        theta_correct = np.array([0, -2.2344])
        radii_correct = np.array([1, 0.6981])

        np.testing.assert_almost_equal(theta, theta_correct, decimal=4)
        np.testing.assert_almost_equal(radii, radii_correct, decimal=4)
