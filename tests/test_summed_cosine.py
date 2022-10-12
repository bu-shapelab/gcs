import unittest
import numpy as np
from utils import summed_cosine, summed_cosine_arc_length, summed_cosine_scaling_factor


class TestSummedCosine(unittest.TestCase):
    """Unit tests for `utils/summed_cosine.py` module.
    """
    # summed_cosine unit tests

    def test_summed_cosine_1(self):
        """Test `summed_cosine` function:
           - Invalid theta values (not an np.ndarray)
        """
        theta = [0, 1]
        r0 = 1
        c1 = 0
        c2 = 0

        with self.assertRaises(TypeError):
            summed_cosine(theta, r0, c1, c2)

    def test_summed_cosine_2(self):
        """Test `summed_cosine` function:
           - Invalid theta values (not a vector)
        """
        theta = np.ones((2, 2))
        r0 = 1
        c1 = 0
        c2 = 0

        with self.assertRaises(ValueError):
            summed_cosine(theta, r0, c1, c2)

    def test_summed_cosine_3(self):
        """Test `summed_cosine` function:
           - Valid arguments
        """
        theta = np.array([np.pi / 5, np.pi / 3])
        r0 = 2
        c1 = 0.4
        c2 = 0.2

        radii_actual = summed_cosine(theta, r0, c1, c2)
        radii_desired = np.array([1.4764, 1.4])

        np.testing.assert_almost_equal(actual=radii_actual,
                                       desired=radii_desired,
                                       decimal=4)

    # summed_cosine_arc_length unit tests

    def test_summed_cosine_arc_length_1(self):
        """Test `summed_cosine_arc_length` function:
           - Invalid r0 values (not a number)
        """
        r0 = [1]
        c1 = 0
        c2 = 0
        n_steps = 50

        with self.assertRaises(TypeError):
            summed_cosine_arc_length(r0, c1, c2, n_steps)

    def test_summed_cosine_arc_length_2(self):
        """Test `summed_cosine_arc_length` function:
           - Invalid n_steps values (not a positive number)
        """
        r0 = 1
        c1 = 0
        c2 = 0
        n_steps = 0

        with self.assertRaises(ValueError):
            summed_cosine_arc_length(r0, c1, c2, n_steps)

    def test_summed_cosine_arc_length_3(self):
        """Test `summed_cosine_arc_length` function:
           - Valid arguments
        """
        r0 = 5
        c1 = 0
        c2 = 0
        n_steps = 1000

        integral_actual = summed_cosine_arc_length(r0, c1, c2, n_steps)
        integral_desired = 31.4159

        self.assertAlmostEqual(integral_actual, integral_desired, places=1)

    # summed_cosine_scaling_factor unit tests

    def test_summed_cosine_scaling_factor_1(self):
        """Test `summed_cosine_scaling_factor` function:
           - Invalid perimeter values (not a number)
        """
        perimeter = [1]
        c1 = 0
        c2 = 0

        with self.assertRaises(TypeError):
            summed_cosine_scaling_factor(perimeter, c1, c2)

    def test_summed_cosine_scaling_factor_2(self):
        """Test `summed_cosine_scaling_factor` function:
           - Invalid perimeter values (not a positive number)
        """
        perimeter = 0
        c1 = 0
        c2 = 0

        with self.assertRaises(ValueError):
            summed_cosine_scaling_factor(perimeter, c1, c2)

    def test_summed_cosine_scaling_factor_3(self):
        """Test `summed_cosine_scaling_factor` function:
           - Valid arguments
        """
        perimeter = 10
        c1 = 0
        c2 = 0

        r0_actual = summed_cosine_scaling_factor(perimeter, c1, c2)
        r0_desired = 5 / np.pi

        self.assertAlmostEqual(r0_actual, r0_desired, 1)
