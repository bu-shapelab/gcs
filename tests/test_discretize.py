from __future__ import annotations

from pytest import approx
import numpy as np
from gcs import GCS, discretize
from ._data import TEST_CYLINDER_PARAMETERS


class TestDiscretize:
    """Tests for:
        - utils/discretize.py

    """

    def test_discretize(self):
        """Test ``gcs.discretize`` function.

        """
        shape = GCS(**TEST_CYLINDER_PARAMETERS)
        parameters = shape.parameters
        vertices = discretize(shape=shape)

        assert vertices is not None

        thetas = np.arange(start=0,
                           stop=2 * np.pi,
                           step=parameters['d_theta'])

        assert vertices.shape == (thetas.size * parameters['n_steps'], 3)
        assert vertices.shape == np.unique(ar=vertices, axis=0).shape

        point_a = vertices[0, :]
        point_b = vertices[thetas.size, :]
        height_per_step = parameters['height'] / (parameters['n_steps'] - 1)

        assert np.linalg.norm(point_b - point_a) == approx(expected=height_per_step,
                                                           abs=0.0001)
