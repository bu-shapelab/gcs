from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np
from matplotlib import pyplot as plt

from ..utils.coordinates import cartesian_to_polar
from ..utils.polar_curves import offset_curve

if TYPE_CHECKING:
    from matplotlib.figure import Figure
    from cls import CLS


def preview_step(shape: CLS, step: int, title: str, show: bool = True) -> Figure:
    """Preview the shape of a CLS at a particular height step.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    step : int
        The height step.
    title : str
        The title of the figure.
    show : bool, (default=True)
        Set to `True` to show the preview.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure of the step shape.

    Raises
    ------
    TypeError
        If ``step`` is not an integer.
        If ``title`` is not a string.
    ValueError
        If ``step`` is negative or ``step>shape.vertices.shape[2]``.

    """
    if not isinstance(step, int):
        raise TypeError('TODO')
    if not isinstance(title, str):
        raise TypeError('TODO')

    vertices = shape.vertices

    if step not in range(vertices.shape[2]):
        raise ValueError('TODO')

    parameters = shape.parameters
    vertices = shape.vertices[:, :2, step]
    vertices_outer = offset_curve(vertices, parameters['thickness'] / 2)
    vertices_inner = offset_curve(vertices, -parameters['thickness'] / 2)

    vertices = cartesian_to_polar(points=vertices)
    vertices_outer = cartesian_to_polar(points=vertices_outer)
    vertices_inner = cartesian_to_polar(points=vertices_inner)

    figure = plt.figure(title)

    plt.subplot(projection='polar')

    theta = vertices[:, 0]
    radii = vertices[:, 1]
    plt.plot(theta, radii, color='C0', label='Center Line')

    theta = vertices_outer[:, 0]
    radii = vertices_outer[:, 1]
    plt.plot(theta, radii, color='C1', label='Walls')

    theta = vertices_inner[:, 0]
    radii = vertices_inner[:, 1]
    plt.plot(theta, radii, color='C1')

    plt.title(title)
    angle = np.deg2rad(67.5)
    plt.legend(loc='lower left', bbox_to_anchor=(.5 + np.cos(angle) / 2, .5 + np.sin(angle) / 2))

    if show:
        plt.show()

    return figure
