from __future__ import annotations

from pytest import approx
from cls import CLS

DEFAULT_SHAPE = CLS()
CUSTOM_SHAPE = CLS(c1_base=0.5,
                   c2_top=-0.25,
                   twist_linear=0.1,
                   twist_amplitude=0.1,
                   twist_period=3,
                   perimeter_ratio=1.5)


class TestCLS:
    """Tests for:
        - cls.py
    """

    def test_parameters(self):
        """Test cls.CLS.parameters property.
        """
        parameters = {
            'c1_base': 0,
            'c2_base': 0,
            'c1_top': 0,
            'c2_top': 0,
            'twist_linear': 0,
            'twist_amplitude': 0,
            'twist_period': 0,
            'perimeter_ratio': 1,
            'height': 19,
            'mass': 2.1,
            'thickness': 0.75,
        }

        assert DEFAULT_SHAPE.parameters == parameters

    def test_base_perimeter(self):
        """Test cls.CLS.base_perimeter property.
        """
        assert DEFAULT_SHAPE.base_perimeter == approx(122.80701754385967)
        assert CUSTOM_SHAPE.base_perimeter == approx(98.24561403508773)

    def test_top_perimeter(self):
        """Test cls.CLS.top_perimeter property.
        """
        assert DEFAULT_SHAPE.top_perimeter == approx(122.80701754385967)
        assert CUSTOM_SHAPE.top_perimeter == approx(147.36842105263162)

    def test_min_radius(self):
        """Test cls.CLS.min_radius property.
        """
        assert DEFAULT_SHAPE.min_radius == approx(19.93625076293947)
        assert CUSTOM_SHAPE.min_radius == approx(4.707543176492682)

    def test_max_radius(self):
        """Test cls.CLS.max_radius property.
        """
        assert DEFAULT_SHAPE.max_radius == approx(19.93625076293947)
        assert CUSTOM_SHAPE.max_radius == approx(17.95458913788471)
