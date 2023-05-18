from __future__ import annotations

from typing import TYPE_CHECKING, Union
import numpy as np
from cls.verify import verify_parameters
from cls._utils import _summed_cosine, _optimal_scaling_factor
from cls._utils import _polar_to_cartesian

if TYPE_CHECKING:
    from cls import CLS


def discretize(shape: CLS,
               verbose: bool = False) -> Union[np.ndarray, None]:
    """Discretizes a ``cls.CLS``.

    Parameters
    ----------
    shape : cls.CLS
        The CLS.
    verbose : bool, (default=`False`)
        Set to `True` to receive discretization messages.

    Returns
    -------
    vertices : (n_vertices, 3) np.ndarray
        The vertices.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> vertices = cls.discretize(shape=shape)

    >>> shape = cls.CLS()
    >>> vertices = shape.vertices

    """
    if verify_parameters(shape=shape, verbose=verbose) is False:
        return None

    parameters = shape.parameters

    thetas = np.arange(start=0,
                       stop=2 * np.pi,
                       step=parameters['d_theta'])
    height_per_step = parameters['height'] / (parameters['n_steps'] - 1)

    c1s = np.linspace(start=parameters['c1_base'],
                      stop=parameters['c1_top'],
                      num=parameters['n_steps'])
    c2s = np.linspace(start=parameters['c2_base'],
                      stop=parameters['c2_top'],
                      num=parameters['n_steps'])
    perimeters = np.linspace(start=shape.base_perimeter,
                             stop=shape.top_perimeter,
                             num=parameters['n_steps'])
    twists_linear = np.linspace(start=0,
                                stop=parameters['twist_linear'],
                                num=parameters['n_steps'])
    twists_oscillating = parameters['twist_amplitude'] * np.sin(
        np.linspace(0, 2 * np.pi * parameters['twist_period'], parameters['n_steps']))

    vertices = np.empty((thetas.size * parameters['n_steps'], 3), dtype=np.float16)

    for step in range(parameters['n_steps']):
        c1 = c1s[step]
        c2 = c2s[step]
        perimeter = perimeters[step]
        twist_linear = twists_linear[step]
        twist_oscillating = twists_oscillating[step]
        height = height_per_step * step

        r0 = _optimal_scaling_factor(
            length=perimeter, c1=c1, c2=c2, n_steps=parameters['n_steps'])

        step_thetas = thetas + twist_linear + twist_oscillating
        radii = np.apply_along_axis(func1d=_summed_cosine,
                                    axis=0,
                                    arr=step_thetas,
                                    r0=r0,
                                    c1=c1,
                                    c2=c2)

        points_2d_polar = np.vstack((thetas, radii)).transpose()
        points_2d_cartesian = _polar_to_cartesian(points_polar=points_2d_polar)

        index_start = step * thetas.size
        index_end = (step + 1) * thetas.size

        vertices[index_start:index_end, :2] = points_2d_cartesian
        vertices[index_start:index_end, 2] = height

    return vertices
