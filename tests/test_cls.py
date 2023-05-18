from __future__ import annotations

from numpy.testing import assert_almost_equal
from pytest import approx
from cls import CLS, discretize
from ._data import TEST_PARAMETERS

class TestCLS:
    """Tests for:
        - cls.py

    """

    def test_parameters(self):
        """Test ``cls.CLS.parameters`` property.

        """
        shape = CLS(**TEST_PARAMETERS)
        assert shape.parameters == TEST_PARAMETERS

    def test_base_perimeter(self):
        """Test ``cls.CLS.base_perimeter`` property.

        """
        shape = CLS(**TEST_PARAMETERS)
        perimeter = approx(expected=148.14814814814818,
                           abs=None)
        assert shape.base_perimeter == perimeter

    def test_top_perimeter(self):
        """Test ``cls.CLS.top_perimeter`` property.

        """
        shape = CLS(**TEST_PARAMETERS)
        perimeter = approx(expected=296.29629629629636,
                           abs=None)
        assert shape.top_perimeter == perimeter

    def test_vertices(self):
        """Test ``cls.CLS.faces`` property.

        """
        shape = CLS(**TEST_PARAMETERS)
        assert_almost_equal(actual=shape.vertices,
                            desired=discretize(shape=shape))

    def test_faces(self):
        """Test ``cls.CLS.faces`` property.

        """
        pass

    def test_mesh(self):
        """Test ``cls.CLS.faces`` property.

        """
        pass