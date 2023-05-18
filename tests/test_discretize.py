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

        point_a = vertices[0, :]
        point_b = vertices[629, :]

        assert np.linalg.norm(point_b - point_a) == approx(expected=0.3333,
                                                           abs=0.0001)
        assert point_b[2] - point_a[2] == approx(expected=0.1515,
                                                 abs=0.0001)

        unique_vertices = np.unique(ar=vertices, axis=0)

        assert unique_vertices.shape == vertices.shape
