from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np
from matplotlib import pyplot as plt

if TYPE_CHECKING:
    from matplotlib.figure import Figure
    from cls import CLS


def preview_twist(shape: CLS, show: bool = False) -> Figure:
    """TODO
    """
    parameters = shape.parameters

    twist_linear = parameters['twist_linear']
    twist_amplitude = parameters['twist_amplitude']
    twist_period = parameters['twist_period']

    n_steps = 100
    x = np.linspace(0, 1, n_steps)
    y = twist_linear + twist_amplitude * np.sin(np.linspace(0, 2 * np.pi * twist_period, n_steps))

    title = 'Twist Preview'

    figure = plt.figure(title)

    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('Step')
    plt.ylabel('Angular Twist')

    if show:
        plt.show()

    return figure
