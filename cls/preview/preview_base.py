from __future__ import annotations

from typing import TYPE_CHECKING

from .preview_step import preview_step

if TYPE_CHECKING:
    from matplotlib.figure import Figure
    from cls import CLS


def preview_base(shape: CLS, show: bool = True) -> Figure:
    """TODO
    """
    figure = preview_step(shape=shape, step=0, title='Top Preview', show=show)
    return figure
