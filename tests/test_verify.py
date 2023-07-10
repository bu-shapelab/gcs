from __future__ import annotations

from gcs import GCS
from gcs.verify import verify_base_perimeter, verify_radius, verify
from ._data import TEST_1_PARAMETERS, TEST_2_PARAMETERS

TEST_1_SHAPE = GCS(**TEST_1_PARAMETERS)
TEST_2_SHAPE = GCS(**TEST_2_PARAMETERS)


class TestVerify:
    """Tests for:
        - verify/verify_base_perimeter.py
        - verify/verify_radius.py
        - verify/verify.py

    """

    def test_verify_base_perimeter(self):
        """Test ``gcs.verify.verify_base_perimeter`` function.

        """
        assert verify_base_perimeter(shape=TEST_1_SHAPE) is True
        assert verify_base_perimeter(shape=TEST_2_SHAPE) is True

    def test_verify_radius(self):
        """Test ``gcs.verify.verify_radius`` function.

        """
        assert verify_radius(shape=TEST_1_SHAPE) is True
        assert verify_radius(shape=TEST_2_SHAPE) is True

    def test_verify(self):
        """Test ``gcs.verify.verify`` function.

        """
        assert verify(shape=TEST_1_SHAPE) is True
        assert verify(shape=TEST_2_SHAPE) is True
