from __future__ import annotations

import numpy as np
from gcs import GCS, triangulate
from ._data import TEST_CYLINDER_PARAMETERS


class TestTriangulate:
    """Tests for:
        - gcs/triangulate.py

    """

    def test_triangulate(self):
        """Test ``gcs.triangulate`` function.

        """
        shape = GCS(**TEST_CYLINDER_PARAMETERS)
        faces = triangulate(shape=shape)

        assert faces is not None

        parameters = shape.parameters
        n_vertices_per_step = shape.vertices.shape[0] // parameters['n_steps']
        n_faces = 2 * n_vertices_per_step * (parameters['n_steps'] - 1)

        assert faces.shape == (n_faces, 3)
        assert shape.vertices.shape[0] == np.unique(ar=faces).size

        np.testing.assert_equal(actual=faces[0],
                                desired=[0, 1257, 628])
        np.testing.assert_equal(actual=faces[1],
                                desired=[1, 629, 0])
        np.testing.assert_equal(actual=faces[2],
                                desired=[2, 630, 1])
