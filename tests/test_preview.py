from __future__ import annotations

from matplotlib.figure import Figure
from cls.random import rand
from cls.preview import preview_base, preview_top, preview_twist

SHAPE = rand()


class TestPreview:
    """TODO
    """

    def test_preview_base(self):
        """TODO
        """
        figure = preview_base(shape=SHAPE, show=False)
        assert isinstance(figure, Figure)

    def test_preview_top(self):
        """TODO
        """
        figure = preview_top(shape=SHAPE, show=False)
        assert isinstance(figure, Figure)

    def test_preview_twist(self):
        """TODO
        """
        figure = preview_twist(shape=SHAPE, show=False)
        assert isinstance(figure, Figure)
