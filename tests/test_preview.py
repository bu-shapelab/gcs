from __future__ import annotations

from matplotlib.figure import Figure
from cls.random import rand
from cls.preview import preview_base, preview_top, preview_twist

SHAPE = rand()


class TestPreview:
    """Tests for:
        - preview/preview_base.py
        - preview/preview_top.py
        - preview/preview_twist.py

    """

    def test_preview_base(self):
        """Test ``cls.preview.preview_base`` function.

        """
        figure = preview_base(shape=SHAPE, show=False)
        assert isinstance(figure, Figure)

    def test_preview_top(self):
        """Test ``cls.preview.preview_top`` function.

        """
        figure = preview_top(shape=SHAPE, show=False)
        assert isinstance(figure, Figure)

    def test_preview_twist(self):
        """Test ``cls.preview.preview_twist`` function.

        """
        figure = preview_twist(shape=SHAPE, show=False)
        assert isinstance(figure, Figure)
