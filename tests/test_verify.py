from __future__ import annotations

from cls import CLS
from cls.verify import verify_all, verify_base_perimeter, verify_parameters, verify_radius

VALID_SHAPE = CLS()
INVALID_SHAPE_PARAMETERS = CLS(c1_top=-1)
INVALID_SHAPE_RADIUS = CLS(c2_base=-1)
INVALID_SHAPE_BASE_PERIMETER = CLS(mass=1, perimeter_ratio=3)


class TestVerify:
    """Tests for:
        - verify/verify_all.py
        - verify/verify_base_perimeter.py
        - verify/verify_parameters.py
        - verify/verify_radius.py
    """

    def test_verify_parameters(self):
        """Test cls.verify.verify_parameters function.
        """
        assert verify_parameters(shape=VALID_SHAPE) is True
        assert verify_parameters(shape=INVALID_SHAPE_PARAMETERS) is False

    def test_verify_radius(self):
        """Test cls.verify.verify_radius function.
        """
        assert verify_radius(shape=VALID_SHAPE) is True
        assert verify_radius(shape=INVALID_SHAPE_RADIUS) is False

    def test_verify_base_perimeter(self):
        """Test cls.verify.verify_base_perimeter function.
        """
        assert verify_base_perimeter(shape=VALID_SHAPE) is True
        assert verify_base_perimeter(shape=INVALID_SHAPE_BASE_PERIMETER) is False

    def test_verify_all(self):
        """Test cls.verify.verify_all function.
        """
        assert verify_all(shape=VALID_SHAPE) is True
        assert VALID_SHAPE.valid is True
        assert verify_all(shape=INVALID_SHAPE_PARAMETERS) is False
        assert INVALID_SHAPE_PARAMETERS.valid is False
        assert verify_all(shape=INVALID_SHAPE_RADIUS) is False
        assert INVALID_SHAPE_RADIUS.valid is False
        assert verify_all(shape=INVALID_SHAPE_BASE_PERIMETER) is False
        assert INVALID_SHAPE_BASE_PERIMETER.valid is False
