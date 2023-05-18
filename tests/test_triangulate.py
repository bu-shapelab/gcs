from __future__ import annotations

import numpy as np
from cls import CLS, triangulate
from ._data import TEST_PARAMETERS

class TestTriangulate:
    """Tests for:
        - cls/triangulate.py

    """

    def test_triangulate(self):
        """Test ``cls.triangulate`` function.

        """
        shape = CLS(**TEST_PARAMETERS)
        faces = triangulate(shape=shape)

        assert faces is not None
        assert faces.shape == (124542, 3)
        unique_indices = np.unique(ar=faces)

        assert unique_indices.size == shape.vertices.shape[0]
