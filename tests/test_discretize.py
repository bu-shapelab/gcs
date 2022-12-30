from __future__ import annotations

from pytest import raises, approx
import numpy as np
from cls import CLS, discretize
from cls.utils.discretization import THETA


class TestDiscretize:
    """TODO
    """

    def test_discretize(self):
        """TODO
        """
        shape = CLS()

        n_steps = 100
        vertices = discretize(shape=shape, n_steps=n_steps)

        assert vertices.shape == (THETA.size, 3, n_steps)
        np.testing.assert_array_almost_equal(vertices, shape.vertices)

        parameters = shape.parameters
        height_per_step = parameters['height'] / (n_steps - 1)

        pointA = vertices[0, :, 0]
        pointB = vertices[0, :, 1]

        assert np.linalg.norm(pointB - pointA) == approx(height_per_step)

    def test_discretize_invalid_n_steps(self):
        """TODO
        """
        shape = CLS()

        n_steps = 0
        with raises(ValueError):
            discretize(shape=shape, n_steps=n_steps)
