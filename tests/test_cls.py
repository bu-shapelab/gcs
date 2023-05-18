from __future__ import annotations

from numpy.testing import assert_almost_equal
from pytest import approx
from cls import CLS, discretize, triangulate
from cls.verify import verify_parameters, verify_base_perimeter, verify_radius
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

    def test_valid_parameters(self):
        """Test ``cls.CLS.valid_parameters`` property.

        """
        shape = CLS(**TEST_PARAMETERS)
        assert shape.valid_parameters == verify_parameters(shape=shape)

    def test_valid_base_perimeter(self):
        """Test ``cls.CLS.valid_base_perimeter`` property.

        """
        shape = CLS(**TEST_PARAMETERS)
        assert shape.valid_base_perimeter == verify_base_perimeter(shape=shape)

    def test_valid_radius(self):
        """Test ``cls.CLS.valid_radius`` property.

        """
        shape = CLS(**TEST_PARAMETERS)
        assert shape.valid_radius == verify_radius(shape=shape)

    def test_valid(self):
        """Test ``cls.CLS.valid_radius`` property.

        """
        shape = CLS(**TEST_PARAMETERS)
        assert shape.valid is True

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
        shape = CLS(**TEST_PARAMETERS)
        assert_almost_equal(actual=shape.faces,
                            desired=triangulate(shape=shape))

    def test_mesh(self):
        """Test ``cls.CLS.faces`` property.

        """
        pass