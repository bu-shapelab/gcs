from __future__ import annotations

from cls import CLS
from cls.verify import verify_parameters
from ._data import TEST_PARAMETERS


class TestVerify:
    """Tests for:
        - verify/verify_parameters.py

    """

    def test_verify_parameters(self):
        """Test ``cls.verify.verify_parameters`` function.

        """
        shape = CLS(**TEST_PARAMETERS)
        assert verify_parameters(shape=shape) is True
