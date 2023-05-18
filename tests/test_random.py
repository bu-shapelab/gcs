from __future__ import annotations

import pytest
from cls.random import rand, randn


class TestRandom:
    """Tests for:
        - random/rand.py
        - random/randn.py

    """

    def test_rand(self):
        """Test ``cls.random.rand`` function.

        """
        shape = rand(seed=755,
                     fixed_kwargs={'c1_base': 0.4})

        assert shape.valid is True
        assert shape.parameters['c1_base'] == 0.4
        assert shape.parameters['c2_base'] == 0.7474824863864697

    def test_randn_single(self):
        """Test ``cls.random.randn`` function.

        """
        shapes = randn(num=1,
                       seed=755,
                       fixed_kwargs={'c1_base': 0.4})
        assert len(shapes) == 1
        assert shapes[0].parameters['c1_base'] == 0.4
        assert shapes[0].parameters['c2_base'] == 0.7474824863864697
