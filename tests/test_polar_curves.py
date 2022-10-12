import unittest
import numpy as np
from utils import offset_curve, self_intersection


class TestPolarCurves(unittest.TestCase):
    """Unit tests for `utils/polar_curves.py` module.
    """
    # offset_curve unit tests

    def test_offset_curve_1(self):
        """Test `offset_curve` function:
           - Invalid points (not an np.ndarray)
        """
        points = [[0, 0],
                  [1, 0],
                  [1, 1],
                  [0, 1]]
        offset = 0.5

        with self.assertRaises(TypeError):
            offset_curve(points, offset)

    def test_offset_curve_2(self):
        """Test `offset_curve` function:
           - Invalid points (too many dimensions)
        """
        # invalid points (too many values)
        points = np.ones((3, 3))
        offset = 0.5

        with self.assertRaises(ValueError):
            offset_curve(points, offset)

    def test_offset_curve_3(self):
        """Test `offset_curve` function:
           - Invalid points (too few points)
        """
        points = np.ones((2, 2))
        offset = 0.5

        with self.assertRaises(ValueError):
            offset_curve(points, offset)

    def test_offset_curve_4(self):
        """Test `offset_curve` function:
           - Valid arguments
        """
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0, 1]])
        offset = 1

        offset_points_actual = offset_curve(points, offset)
        offset_points_desired = np.array([[-np.sqrt(0.5), -np.sqrt(0.5)],
                                          [1 + np.sqrt(0.5), -np.sqrt(0.5)],
                                          [1 + np.sqrt(0.5), 1 + np.sqrt(0.5)],
                                          [-np.sqrt(0.5), 1 + np.sqrt(0.5)]])

        np.testing.assert_almost_equal(actual=offset_points_actual,
                                       desired=offset_points_desired,
                                       decimal=4)

    def test_offset_curve_5(self):
        """Test `offset_curve` function:
           - Negative offset
        """
        # negative offset
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0, 1]])
        offset = -1

        offset_points_actual = offset_curve(points, offset)
        offset_points_desired = np.array([[np.sqrt(0.5), np.sqrt(0.5)],
                                          [1 - np.sqrt(0.5), np.sqrt(0.5)],
                                          [1 - np.sqrt(0.5), 1 - np.sqrt(0.5)],
                                          [np.sqrt(0.5), 1 - np.sqrt(0.5)]])

        np.testing.assert_almost_equal(actual=offset_points_actual,
                                       desired=offset_points_desired,
                                       decimal=4)

    def test_offset_curve_6(self):
        """Test `offset_curve` function:
           - No offset
        """
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0, 1]])
        offset = 0

        offset_points_actual = offset_curve(points, offset)

        np.testing.assert_almost_equal(actual=offset_points_actual,
                                       desired=points,
                                       decimal=4)

    # self_intersection unit tests

    def test_self_intersection_1(self):
        """Test `self_intersection` function:
           - Invalid points (not an np.ndarray)
        """
        points = [[0, 0],
                  [1, 0],
                  [1, 1],
                  [0, 1]]

        with self.assertRaises(TypeError):
            self_intersection(points)

    def test_self_intersection_2(self):
        """Test `self_intersection` function:
           - Invalid points (too many dimensions)
        """
        points = np.ones((4, 3))

        with self.assertRaises(ValueError):
            self_intersection(points)

    def test_self_intersection_3(self):
        """Test `self_intersection` function:
           - Invalid points (too few points)
        """
        points = np.ones((2, 2))

        with self.assertRaises(ValueError):
            self_intersection(points)

    def test_self_intersection_4(self):
        """Test `self_intersection` function:
           - Valid arguments (no intersection)
        """
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0, 1]])

        result = self_intersection(points)

        self.assertFalse(result)

    def test_self_intersection_5(self):
        """Test `self_intersection` function:
           - Valid arguments (intersection)
        """
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0.5, -0.25]])

        result = self_intersection(points)

        self.assertTrue(result)

    def test_self_intersection_6(self):
        """Test `self_intersection` function:
           - All same point
        """
        points = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])

        result = self_intersection(points)

        self.assertTrue(result)

    def test_self_intersection_7(self):
        """Test `self_intersection` function:
           - All same line segment
        """
        points = np.array([[0, 0],
                           [0, 0],
                           [1, 0]])

        result = self_intersection(points)

        self.assertTrue(result)
