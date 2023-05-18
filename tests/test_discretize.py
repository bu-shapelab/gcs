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
        assert vertices.shape == (62900, 3)

        # TODO: CHECK
        # point_a = vertices[0, :]
        # point_b = vertices[239, :]
        # assert np.linalg.norm(point_b - point_a) == approx(height_per_step)

        unique_vertices = np.unique(ar=vertices, axis=0)

        assert unique_vertices.shape == vertices.shape
