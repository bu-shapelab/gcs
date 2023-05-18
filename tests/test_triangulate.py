from __future__ import annotations

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
        triangulate(shape=shape)
