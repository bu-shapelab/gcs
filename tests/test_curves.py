import unittest
import numpy as np
from utils import offset_curve, self_intersection


class TestCurves(unittest.TestCase):
    """Unit tests for `utils/curves.py` module.
    """
    # offset_curve unit tests
    def test_offset_curve_1(self):
        """Test `offset_curve` function with invalid arguments.
        """
        # invalid points (not an np.ndarray)
        points = [[0, 0],
                  [1, 0],
                  [1, 1],
                  [0, 1]]
        amount = 0.5

        with self.assertRaises(TypeError):
            offset_curve(points, amount)

        # invalid points (too many values)
        points = np.array([[0, 0, 0],
                           [1, 0, 0],
                           [1, 1, 0],
                           [0, 1, 0]])
        amount = 0.5

        # invalid points (too few values)
        points = np.array([[0, 0, 0],
                           [1, 0, 0]])

        with self.assertRaises(ValueError):
            offset_curve(points, amount)

    def test_offset_curve_2(self):
        """Test `offset_curve` function with valid arguments.
        """

        # positive offset
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

        # negative offset
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0, 1]])
        amount = -1

        offset_points = offset_curve(points, amount)

        offset_points_correct = np.array([[np.sqrt(0.5), np.sqrt(0.5)],
                                          [1 - np.sqrt(0.5), np.sqrt(0.5)],
                                          [1 - np.sqrt(0.5), 1 - np.sqrt(0.5)],
                                          [np.sqrt(0.5), 1 - np.sqrt(0.5)]])

        np.testing.assert_almost_equal(offset_points, offset_points_correct, decimal=4)

        # no offset
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0, 1]])
        amount = 0

        offset_points = offset_curve(points, amount)

        np.testing.assert_almost_equal(offset_points, points, decimal=4)

    # self_intersection unit tests
    def test_self_intersection_1(self):
        """Test `self_intersection` function on invalid arguments.
        """
        # invalid points (not an np.ndarray)
        points = [[0, 0],
                  [1, 0],
                  [1, 1],
                  [0, 1]]

        with self.assertRaises(TypeError):
            self_intersection(points)

        # invalid points (too many arguments)
        points = np.array([[0, 0, 0],
                           [1, 0, 0],
                           [1, 1, 0],
                           [0, 1, 0]])

        with self.assertRaises(ValueError):
            self_intersection(points)

    def test_self_intersection_2(self):
        """Test `self_intersection` function on a curve with valid arguments.
        """
        # no intersection
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0, 1]])

        result = self_intersection(points)

        self.assertFalse(result)

        # intersection
        points = np.array([[0, 0],
                           [1, 0],
                           [1, 1],
                           [0.5, -0.25]])

        result = self_intersection(points)

        self.assertTrue(result)

        # all same point
        points = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])

        result = self_intersection(points)

        self.assertTrue(result)

        # points on a line segment
        points = np.array([[0, 0],
                           [0, 0],
                           [1, 0]])

        result = self_intersection(points)

        self.assertTrue(result)
