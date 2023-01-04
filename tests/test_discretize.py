from __future__ import annotations

from pytest import raises, approx
import numpy as np
from cls import CLS, discretize
from cls.discretization import THETA


class TestDiscretize:
    """Tests for:
        - utils/discretize.py

    """

    def test_discretize(self):
        """Test ``cls.discretize`` function.

        """
        shape = CLS()

        n_steps = 100
        vertices = discretize(shape=shape, n_steps=n_steps)

        assert vertices.shape == (THETA.size, 3, n_steps)
        np.testing.assert_array_almost_equal(vertices, shape.vertices)

        parameters = shape.parameters
        height_per_step = parameters['height'] / (n_steps - 1)

        point_a = vertices[0, :, 0]
        point_b = vertices[0, :, 1]

        assert np.linalg.norm(point_b - point_a) == approx(height_per_step)

    def test_discretize_invalid_n_steps(self):
        """Test ``cls.discretize`` function.
        - Invalid n_steps argument

        """
        shape = CLS()

        n_steps = 0
        with raises(ValueError):
            discretize(shape=shape, n_steps=n_steps)
