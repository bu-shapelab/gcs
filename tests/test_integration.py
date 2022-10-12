import unittest
import numpy as np
from utils import simpsons_rule


class TestIntegration(unittest.TestCase):
    """Unit tests for `utils/integration.py` module.
    """
    # simpsons_rule unit tests

    def test_simpsons_rule_1(self):
        """Test `simpsons_rule` function:
           - Invalid y values (not an np.ndarray)
        """
        y = [[0, 0]]
        a = 0
        b = 1

        with self.assertRaises(TypeError):
            simpsons_rule(y, a, b)

    def test_simpsons_rule_2(self):
        """Test `simpsons_rule` function:
           - Invalid y values (not a vector)
        """
        y = np.ones((2, 2))
        a = 0
        b = 1

        with self.assertRaises(ValueError):
            simpsons_rule(y, a, b)

    def test_simpsons_rule_3(self):
        """Test `simpsons_rule` function:
           - Invalid range
        """
        n_steps = 1000

        a = 3
        b = 1

        x = np.linspace(a, b, n_steps + 1)
        y = -1.25 * x ** 2 + 8.5 * x - 2.25

        with self.assertRaises(ValueError):
            simpsons_rule(y, a, b)

    def test_simpsons_rule_4(self):
        """Test `simpsons_rule` function:
           - Odd number of steps
        """
        n_steps = 1001

        a = 1
        b = 3

        x = np.linspace(a, b, n_steps + 1)
        y = -1.25 * x ** 2 + 8.5 * x - 2.25

        with self.assertRaises(ValueError):
            simpsons_rule(y, a, b)

    def test_simpsons_rule_5(self):
        """Test `simpsons_rule` function:
           - Valid arguments
        """
        n_steps = 1000

        a = 1
        b = 3

        x = np.linspace(a, b, n_steps + 1)
        y = -1.25 * x ** 2 + 8.5 * x - 2.25

        integral_actual = simpsons_rule(y, a, b)
        integral_desired = 18.6667

        self.assertAlmostEqual(integral_actual, integral_desired, places=1)
