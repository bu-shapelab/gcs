from __future__ import annotations

from typing import TYPE_CHECKING

from cls.preview import _preview_face

if TYPE_CHECKING:
    from matplotlib.figure import Figure
    from cls import CLS


def preview_base(shape: CLS, show: bool = True) -> Figure:
    """Preview the base shape of a CLS.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    show : bool, (default=True)
        Set to `True` to show the preview.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure of the base shape.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> cls.preview.preview_base(shape=shape, show=True)

    >>> shape = cls.CLS()
    >>> fig = cls.preview.preview_base(shape=shape, show=False)
    >>> from matplotlib import pyplot as plt
    >>> plt.show()

    """
    figure = _preview_face(shape=shape,
                           top=False,
                           title='Base Preview',
                           show=show)

    return figure
