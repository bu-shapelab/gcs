from __future__ import annotations

from pytest import approx
import numpy as np
from cls import CLS, discretize
from ._data import TEST_PARAMETERS

class TestDiscretize:
    """Tests for:
        - utils/discretize.py

    """

    def test_discretize(self):
        """Test ``cls.discretize`` function.

        """
        shape = CLS(**TEST_PARAMETERS)
        vertices = discretize(shape=shape)

        assert vertices is not None

        parameters = shape.parameters
        theta = np.arange(start=0,
                          stop=2 * np.pi,
                          step=parameters['d_theta'])
        height_per_step = parameters['height'] / (parameters['n_steps'] - 1)

        assert vertices.shape == (theta.size * parameters['n_steps'], 3)        

        point_a = vertices[0, :]
        point_b = vertices[theta.size, :]

        # TODO: CHECK
        # assert np.linalg.norm(point_b - point_a) == approx(height_per_step)

        unique_vertices = np.unique(ar=vertices, axis=0)

        assert unique_vertices.shape == vertices.shape
