from __future__ import annotations

from cls import CLS
from cls.verify import verify_parameters, verify_base_perimeter, verify_radius
from ._data import TEST_PARAMETERS


class TestVerify:
    """Tests for:
        - verify/verify_parameters.py
        - verify/verify_base_perimeter.py
        - verify/verify_radius.py

    """

    def test_verify_parameters(self):
        """Test ``cls.verify.verify_parameters`` function.

        """
        shape = CLS(**TEST_PARAMETERS)
        assert verify_parameters(shape=shape) is True

    def test_verify_base_perimeter(self):
        """Test ``cls.verify.verify_base_perimeter`` function.

        """
        shape = CLS(**TEST_PARAMETERS)
        assert verify_base_perimeter(shape=shape) is True

    def test_verify_radius(self):
        """Test ``cls.verify.verify_radius`` function.

        """
        shape = CLS(**TEST_PARAMETERS)
        assert verify_radius(shape=shape) is True
