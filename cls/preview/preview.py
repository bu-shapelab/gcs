from __future__ import annotations

from typing import TYPE_CHECKING

import plotly.graph_objects as go

if TYPE_CHECKING:
    from cls import CLS
    from plotly.graph_objects import Figure


def preview(shape: CLS, show: bool = True) -> Figure:
    """Preview the 3D render of a CLS.

    Note, the preview will open in the default browser.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    show : bool, (default=True)
        Set to `True` to show the preview.
    
    Returns
    -------
    figure : plotly.go.Figure
        The figure of the shape.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> cls.preview.preview(shape=shape)

    >>> shape = cls.CLS()
    >>> fig = cls.preview.preview_top(shape=shape, show=False)
    >>> from matplotlib import pyplot as plt
    >>> plt.show()

    """
    vertices = shape.vertices
    faces = shape.faces

    x = vertices[:, 0].tolist()
    y = vertices[:, 1].tolist()
    z = vertices[:, 2].tolist()

    i = faces[:, 0].tolist()
    j = faces[:, 1].tolist()
    k = faces[:, 2].tolist()

    data = go.Mesh3d(
        x=x,
        y=y,
        z=z,
        i=i,
        j=j,
        k=k,
    )
    
    layout = {
        'xaxis': {
            'visible': False
        },
        'yaxis': {
            'visible': False
        },
        'zaxis': {
            'visible': False
        },
        'hovermode': False,
        'dragmode': 'turntable',
    }

    config = {
        'staticPlot': False,
        'displayModeBar': False,
        'responsive': True,
        'doubleClickDelay': 1000,
        'scrollZoom': False,
    }

    figure = go.Figure(data=[data])
    figure.update_layout(scene=layout)

    if show:
        figure.show(config=config)
    
    return figure
