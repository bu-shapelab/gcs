from __future__ import annotations

import numpy as np
from matplotlib import pyplot as plt
from cls import CLS

from .coordinates import cartesian_to_polar
from .polar_curves import offset_curve


def preview_step(shape: CLS, step: int, title: str) -> None:
    """TODO
    """
    parameters = shape.parameters

    vertices = shape.vertices[:, :2, step]
    vertices_outer = offset_curve(vertices, parameters['thickness'] / 2)
    vertices_inner = offset_curve(vertices, -parameters['thickness'] / 2)

    vertices = cartesian_to_polar(points=vertices)
    vertices_outer = cartesian_to_polar(points=vertices_outer)
    vertices_inner = cartesian_to_polar(points=vertices_inner)

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
    plt.legend(loc='lower left',
               bbox_to_anchor=(.5 + np.cos(angle) / 2, .5 + np.sin(angle) / 2))
    plt.show()


def preview_base(shape: CLS) -> None:
    """TODO
    """
    preview_step(shape=shape, step=0, title='Base Preview')


def preview_top(shape: CLS) -> None:
    """TODO
    """
    preview_step(shape=shape, step=-1, title='Top Preview')


def preview_twist(shape: CLS) -> None:
    """TODO
    """
    parameters = shape.parameters

    twist_linear = parameters['twist_linear']
    twist_amplitude = parameters['twist_amplitude']
    twist_period = parameters['twist_period']

    n_steps = 100
    x = np.linspace(0, 1, n_steps)
    y = twist_linear + twist_amplitude * np.sin(np.linspace(0, 2 * np.pi * twist_period, n_steps))

    plt.plot(x, y)
    plt.title('Twist Preview')
    plt.xlabel('Step')
    plt.ylabel('Angular Twist')

    plt.show()
