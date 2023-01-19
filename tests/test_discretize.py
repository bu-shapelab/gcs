from __future__ import annotations

from pytest import approx
import numpy as np
from cls import CLS, discretize


class TestDiscretize:
    """Tests for:
        - utils/discretize.py

    """

    def test_discretize(self):
        """Test ``cls.discretize`` function.

        """
        shape = CLS()
        n_steps = shape.n_steps

        vertices = discretize(shape=shape)

        theta = np.arange(0, 2 * np.pi, shape.theta_step)

        assert vertices.shape == (theta.size * n_steps, 3)
        np.testing.assert_array_almost_equal(x=vertices, y=shape.vertices)

        parameters = shape.parameters
        height_per_step = parameters['height'] / (n_steps - 1)

        point_a = vertices[0, :]
        point_b = vertices[theta.size, :]

        assert np.linalg.norm(point_b - point_a) == approx(height_per_step)

        unique_vertices = np.unique(ar=vertices, axis=0)

        assert unique_vertices.shape == vertices.shape
