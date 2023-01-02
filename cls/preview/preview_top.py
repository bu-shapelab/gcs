from __future__ import annotations

from typing import TYPE_CHECKING

from .preview_step import preview_step

if TYPE_CHECKING:
    from matplotlib.figure import Figure
    from cls import CLS


def preview_top(shape: CLS, show: bool = True) -> Figure:
    """Preview the top shape of a CLS.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    show : bool, (default=True)
        Set to `True` to show the preview.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure of the top shape.

    Examples
    --------
    TODO

    """
    figure = preview_step(shape=shape, step=-1, title='Top Preview', show=show)
    return figure
