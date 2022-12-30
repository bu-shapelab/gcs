from __future__ import annotations

import pytest
from cls import CLS, triangulate


class TestDiscretize:
    """TODO
    """

    def test_triangulate(self):
        """TODO
        """
        shape = CLS()

        n_steps = 100
        triangulate(shape=shape, n_steps=n_steps)

    def test_triangulate_invalid_n_steps(self):
        """TODO
        """
        shape = CLS()

        n_steps = 0
        with pytest.raises(ValueError):
            triangulate(shape=shape, n_steps=n_steps)
