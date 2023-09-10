from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np
from gcs.utils import summed_cosine, optimal_scaling_factor
from gcs.utils import pol2cart

if TYPE_CHECKING:
    import gcs


def discretize(shape: gcs.GCS) -> np.ndarray:
    """Discretizes a GCS.

    Parameters
    ----------
    shape : gcs.GCS
        The GCS.

    Returns
    -------
    vertices : (N, 3) np.ndarray
        The vertices.

    Examples
    --------
    >>> shape = gcs.GCS(...)
    >>> vertices = gcs.discretize(shape=shape)

    >>> shape = gcs.GCS(...)
    >>> vertices = shape.vertices

    """
    parameters = shape.parameters

    thetas = np.arange(start=0,
                       stop=2 * np.pi,
                       step=parameters['d_theta'])
    height_per_step = parameters['height'] / (parameters['n_steps'] - 1)

    c4s = np.linspace(start=parameters['c4_base'],
                      stop=parameters['c4_top'],
                      num=parameters['n_steps'])
    c8s = np.linspace(start=parameters['c8_base'],
                      stop=parameters['c8_top'],
                      num=parameters['n_steps'])
    perimeters = np.linspace(start=shape.base_perimeter,
                             stop=shape.top_perimeter,
                             num=parameters['n_steps'])
    twists_linear = np.linspace(start=0,
                                stop=parameters['twist_linear'],
                                num=parameters['n_steps'])
    twists_oscillating = parameters['twist_amplitude'] * np.sin(
        np.linspace(0, 2 * np.pi * parameters['twist_cycles'], parameters['n_steps']))

    vertices = np.empty((thetas.size * parameters['n_steps'], 3), dtype=np.float16)

    for step in range(parameters['n_steps']):
        c4 = c4s[step]
        c8 = c8s[step]
        perimeter = perimeters[step]
        twist_linear = twists_linear[step]
        twist_oscillating = twists_oscillating[step]
        height = height_per_step * step

        r0 = optimal_scaling_factor(length=perimeter,
                                    c4=c4,
                                    c8=c8,
                                    n_steps=thetas.size)

        step_thetas = thetas + twist_linear + twist_oscillating
        radii = np.apply_along_axis(func1d=summed_cosine,
                                    axis=0,
                                    arr=step_thetas,
                                    r0=r0,
                                    c4=c4,
                                    c8=c8)

        x, y = pol2cart(radius=radii, theta=thetas)

        index_start = step * thetas.size
        index_end = (step + 1) * thetas.size

        vertices[index_start:index_end, 0] = x
        vertices[index_start:index_end, 1] = y
        vertices[index_start:index_end, 2] = height

    return vertices
