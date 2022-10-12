import unittest
import numpy as np
from utils import polar_to_cartesian, cartesian_to_polar


class TestCoordinates(unittest.TestCase):
    """Unit tests for `utils/coordinates.py` module.
    """
    # polar_to_cartesian unit tests

    def test_polar_to_cartesian_1(self):
        """Test `polar_to_cartesian` function:
           - Invalid points (not an np.ndarray)
        """
        points = [[np.pi / 2, 1]]

        with self.assertRaises(TypeError):
            polar_to_cartesian(points)

    def test_polar_to_cartesian_2(self):
        """Test `polar_to_cartesian` function:
           - Invalid radii (too many values)
        """
        points = np.ones((1, 3))

        with self.assertRaises(ValueError):
            polar_to_cartesian(points)

    def test_polar_to_cartesian_3(self):
        """Test `polar_to_cartesian` function:
            - Single theta and radius
        """
        points = np.array([[np.pi / 2, 1]])

        points_cartesian_actual = polar_to_cartesian(points)
        points_cartesian_desired = np.array([[0, 1]])

        np.testing.assert_almost_equal(actual=points_cartesian_actual,
                                       desired=points_cartesian_desired,
                                       decimal=4)

    def test_polar_to_cartesian_4(self):
        """Test `polar_to_cartesian` function:
            - Vector of theta and radii
        """
        points = np.array([[np.pi / 3, 1],
                           [np.pi / 5, 0.5]])

        points_cartesian_actual = polar_to_cartesian(points)
        points_cartesian_desired = np.array([[1 / 2, np.sqrt(3) / 2],
                                             [0.40450, 0.29389]])

        np.testing.assert_almost_equal(actual=points_cartesian_actual,
                                       desired=points_cartesian_desired,
                                       decimal=4)

    def test_polar_to_cartesian_5(self):
        """Test `polar_to_cartesian` function:
            - Negative values
        """
        points = np.array([[-np.pi / 3, -1]])

        points_cartesian_actual = polar_to_cartesian(points)
        points_cartesian_desired = np.array([[-1 / 2, np.sqrt(3) / 2]])

        np.testing.assert_almost_equal(actual=points_cartesian_actual,
                                       desired=points_cartesian_desired,
                                       decimal=4)

    def test_polar_to_cartesian_6(self):
        """Test `polar_to_cartesian` function:
            - All zeros
        """
        points = np.zeros((1, 2))

        points_cartesian_actual = polar_to_cartesian(points)

        np.testing.assert_almost_equal(actual=points_cartesian_actual,
                                       desired=points,
                                       decimal=4)

    # cartesian_to_polar unit tests

    def test_cartesian_to_polar_1(self):
        """Test `cartesian_to_polar` function:
           - Invalid points (not an np.ndarray)
        """
        points = [[1, 0]]

        with self.assertRaises(TypeError):
            cartesian_to_polar(points)

    def test_cartesian_to_polar_2(self):
        """Test `cartesian_to_polar` function:
           - Invalid points (dimensions incorrect)
        """
        points = np.ones((2, 3))

        with self.assertRaises(ValueError):
            cartesian_to_polar(points)

    def test_cartesian_to_polar_3(self):
        """Test `cartesian_to_polar` function:
           - Single point
        """
        points = np.array([[1, 0]])

        points_polar_actual = cartesian_to_polar(points)
        points_polar_desired = np.array([[0, 1]])

        np.testing.assert_almost_equal(actual=points_polar_actual,
                                       desired=points_polar_desired,
                                       decimal=4)

    def test_cartesian_to_polar_4(self):
        """Test `cartesian_to_polar` function:
           - Multiple points
        """
        points = np.array([[1, 0],
                           [0.43, 0.55]])

        points_polar_actual = cartesian_to_polar(points)
        points_polar_desired = np.array([[0, 1],
                                         [0.9072, 0.6981]])

        np.testing.assert_almost_equal(actual=points_polar_actual,
                                       desired=points_polar_desired,
                                       decimal=4)

    def test_cartesian_to_polar_5(self):
        """Test `cartesian_to_polar` function:
           - Negative values
        """
        points = np.array([[-0.43, 0.55]])

        points_polar_actual = cartesian_to_polar(points)
        points_polar_desired = np.array([[2.2344, 0.6981]])

        np.testing.assert_almost_equal(actual=points_polar_actual,
                                       desired=points_polar_desired,
                                       decimal=4)

    def test_cartesian_to_polar_6(self):
        """Test `cartesian_to_polar` function:
           - All zeros
        """
        points = np.zeros((1, 2))

        points_polar_actual = cartesian_to_polar(points)

        np.testing.assert_almost_equal(actual=points_polar_actual,
                                       desired=points,
                                       decimal=4)
