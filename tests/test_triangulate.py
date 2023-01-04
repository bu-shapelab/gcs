from __future__ import annotations

from cls import CLS, triangulate


class TestTriangulate:
    """Tests for:
        - cls/triangulate.py

    """

    def test_triangulate(self):
        """Test ``cls.triangulate`` function.

        """
        shape = CLS()

        triangulate(shape=shape)
