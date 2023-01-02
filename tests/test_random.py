from __future__ import annotations

import pytest
from cls.random import rand, randn


class TestRandom:
    """Tests for:
        - random/rand.py
        - random/randn.py
    """

    def test_rand(self):
        """Test cls.random.rand function.
        """
        shape = rand()
        assert shape.valid is True

    def test_rand_seed(self):
        """Test cls.random.rand function.
        - With seed
        """
        seed = 100
        shape = rand(seed=seed)
        assert shape.valid is True

    def test_rand_fixed_parameters(self):
        """Test cls.random.rand function.
        - With fixed parameters
        """
        fixed_parameters = {
            'height': 19,
            'mass': 3.3
        }
        shape = rand(fixed_parameters=fixed_parameters)
        assert shape.valid is True
        parameters = shape.parameters
        assert parameters['height'] == fixed_parameters['height']
        assert parameters['mass'] == fixed_parameters['mass']

    def test_randn_single(self):
        """Test cls.random.randn function.
        - Single CLS
        """
        n = 1
        shapes = randn(n=n)
        assert len(shapes) == n
        for shape in shapes:
            assert shape.valid is True

    def test_randn_multi(self):
        """Test cls.random.randn function.
        - Multiple CLS
        """
        n = 3
        shapes = randn(n=n)
        assert len(shapes) == n
        for shape in shapes:
            assert shape.valid is True

    def test_randn_none(self):
        """Test cls.random.randn function.
        - No CLS
        """
        n = 0
        with pytest.raises(ValueError):
            randn(n=n)

    def test_randn_seed(self):
        """Test cls.random.randn function.
        - With seed
        """
        n = 3
        seed = 100
        shapes = randn(n=n, seed=seed)
        for shape in shapes:
            assert shape.valid is True

    def test_randn_fixed_parameters(self):
        """Test cls.random.randn function.
        - With fixed parameters
        """
        n = 3
        fixed_parameters = {
            'height': 19,
            'mass': 3.3
        }
        shapes = randn(n=n, fixed_parameters=fixed_parameters)
        for shape in shapes:
            assert shape.valid is True
            parameters = shape.parameters
            assert parameters['height'] == fixed_parameters['height']
            assert parameters['mass'] == fixed_parameters['mass']
