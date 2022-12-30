from __future__ import annotations

from cls.random import rand, randn


class TestRandom:
    """TODO
    """

    def test_rand(self):
        """TODO
        """
        shape = rand()
        assert shape.valid is True

    def test_rand_seed(self):
        """TODO
        """
        seed = 100
        shape = rand(seed=seed)
        assert shape.valid is True

    def test_rand_fixed_parameters(self):
        """TODO
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
        """TODO
        """
        n = 1
        shapes = randn(n=n)
        assert len(shapes) == n
        for shape in shapes:
            assert shape.valid is True

    def test_randn_multi(self):
        """TODO
        """
        n = 3
        shapes = randn(n=n)
        assert len(shapes) == n
        for shape in shapes:
            assert shape.valid is True

    def test_randn_none(self):
        """TODO
        """
        n = 0
        shapes = randn(n=n)
        assert len(shapes) == n

    def test_randn_seed(self):
        """TODO
        """
        n = 3
        seed = 100
        shapes = randn(n=n, seed=seed)
        for shape in shapes:
            assert shape.valid is True

    def test_randn_fixed_parameters(self):
        """TODO
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
