import unittest
import numpy as np
from utils import offset_curve, self_intersection


class TestCurves(unittest.TestCase):
    """Unit tests for `utils/curves.py` module.
    """
    # offset_curve unit tests

    def test_offset_curve_invalid_type(self):
        """Test `offset_curve` function on invalid argument types.
        """
        points = [[0, 0],
                  [1, 0],
                  [1, 1],
                  [0, 1]]
        amount = 0.5

        with self.assertRaises(TypeError):
            offset_curve(points, amount)

    def test_offset_curve_invalid_values(self):
        """Test `offset_curve` function on invalid argument values.
        """
        points = np.array([[0, 0, 0],
                           [1, 0, 0],
                           [1, 1, 0],
                           [0, 1, 0]])
        amount = 0.5

        with self.assertRaises(ValueError):
            offset_curve(points, amount)

    def test_offset_curve_with_offset(self):
        """Test `offset_curve` function with an offset.
        """
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0, 1]])
        amount = 1

        offset_points = offset_curve(points, amount)

        offset_points_correct = np.array([[-np.sqrt(0.5), -np.sqrt(0.5)],
                                          [1 + np.sqrt(0.5), -np.sqrt(0.5)],
                                          [1 + np.sqrt(0.5), 1 + np.sqrt(0.5)],
                                          [-np.sqrt(0.5), 1 + np.sqrt(0.5)]])

        np.testing.assert_almost_equal(offset_points, offset_points_correct, decimal=4)

    def test_offset_curve_without_offset(self):
        """Test `offset_curve` function without an offset.
        """
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0, 1]])
        amount = 0

        offset_points = offset_curve(points, amount)

        np.testing.assert_almost_equal(offset_points, points, decimal=4)

    # self_intersection unit tests
    def test_self_intersection_invalid_type(self):
        """Test `self_intersection` function on invalid argument types.
        """
        points = [[0, 0],
                  [1, 0],
                  [1, 1],
                  [0, 1]]

        with self.assertRaises(TypeError):
            self_intersection(points)

    def test_self_intersection_invalid_values(self):
        """Test `self_intersection` function on invalid argument values.
        """
        points = np.array([[0, 0, 0],
                           [1, 0, 0],
                           [1, 1, 0],
                           [0, 1, 0]])

        with self.assertRaises(ValueError):
            self_intersection(points)

    def test_self_intersection_no_intersect(self):
        """Test `self_intersection` function on a curve with no intersections.
        """
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0, 1]])

        result = self_intersection(points)

        self.assertFalse(result)

    def test_self_intersection_intersect(self):
        """Test `self_intersection` function on a curve with intersections.
        """
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0.5, -0.25]])

        result = self_intersection(points)

        self.assertTrue(result)
