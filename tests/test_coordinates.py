import unittest
import numpy as np
from utils import polar_to_cartesian, cartesian_to_polar


class TestCoordinates(unittest.TestCase):
    """Unit tests for `utils/coordinates.py` module.
    """
    # polar_to_cartesian unit tests
    def test_polar_to_cartesian_1(self):
        """Test `polar_to_cartesian` function with invalid arguments.
        """
        # invalid theta (not an np.ndarray)
        theta = [1]
        radii = np.array([1])

        with self.assertRaises(TypeError):
            polar_to_cartesian(theta, radii)

        # invalid radii (too many values)
        theta = np.array([1])
        radii = np.array([1, 1])

        with self.assertRaises(ValueError):
            polar_to_cartesian(theta, radii)

    def test_polar_to_cartesian_2(self):
        """Test `polar_to_cartesian` function with valid arguments.
        """
        # singleton
        theta = np.array([np.pi / 3])
        radii = np.array([1])

        points = polar_to_cartesian(theta, radii)
        points_correct = np.array([[1 / 2, np.sqrt(3) / 2]])

        np.testing.assert_almost_equal(points, points_correct, decimal=4)

        # vectors
        theta = np.array([np.pi / 3, np.pi / 5])
        radii = np.array([1, 0.5])

        points = polar_to_cartesian(theta, radii)
        points_correct = np.array([[1 / 2, np.sqrt(3) / 2],
                                   [0.40450, 0.29389]])

        np.testing.assert_almost_equal(points, points_correct, decimal=4)

        # negative values
        theta = np.array([-np.pi / 3])
        radii = np.array([-1])

        points = polar_to_cartesian(theta, radii)
        points_correct = np.array([[-1 / 2, np.sqrt(3) / 2]])

        np.testing.assert_almost_equal(points, points_correct, decimal=4)

        # zeros
        theta = np.array([0])
        radii = np.array([0])

        points = polar_to_cartesian(theta, radii)
        points_correct = np.array([[0, 0]])

        np.testing.assert_almost_equal(points, points_correct, decimal=4)

    # cartesian_to_polar unit tests
    def test_cartesian_to_polar_1(self):
        """Test `cartesian_to_polar` function with invalid arguments.
        """
        # invalid points (not an np.ndarray)
        points = [1, 0]

        with self.assertRaises(TypeError):
            cartesian_to_polar(points)

        # invalid points (dimensions incorrect)
        points = np.array([[1, 0, 0],
                           [-0.43, -0.52, 0]])

        with self.assertRaises(ValueError):
            cartesian_to_polar(points)

    def test_cartesian_to_polar_2(self):
        """Test `cartesian_to_polar` function with valid arguments.
        """
        # single point
        points = np.array([[1, 0]])
        print(points.shape)

        theta, radii = cartesian_to_polar(points)

        theta_correct = np.array([0])
        radii_correct = np.array([1])

        np.testing.assert_almost_equal(theta, theta_correct, decimal=4)
        np.testing.assert_almost_equal(radii, radii_correct, decimal=4)

        # multiple points
        points = np.array([[1, 0],
                           [0.43, 0.55]])

        theta, radii = cartesian_to_polar(points)

        theta_correct = np.array([0, 0.9072])
        radii_correct = np.array([1, 0.6981])

        np.testing.assert_almost_equal(theta, theta_correct, decimal=4)
        np.testing.assert_almost_equal(radii, radii_correct, decimal=4)

        # negative values
        points = np.array([[-0.43, 0.55]])

        theta, radii = cartesian_to_polar(points)

        theta_correct = np.array([2.2344])
        radii_correct = np.array([0.6981])

        np.testing.assert_almost_equal(theta, theta_correct, decimal=4)
        np.testing.assert_almost_equal(radii, radii_correct, decimal=4)

        # zero values
        points = np.array([[0, 0]])

        theta, radii = cartesian_to_polar(points)

        theta_correct = np.array([0])
        radii_correct = np.array([0])

        np.testing.assert_almost_equal(theta, theta_correct, decimal=4)
        np.testing.assert_almost_equal(radii, radii_correct, decimal=4)
