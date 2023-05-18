from __future__ import annotations

from typing import TYPE_CHECKING, Union
import numpy as np
from cls.verify import verify_parameters

if TYPE_CHECKING:
    from cls import CLS


def triangulate(shape: CLS,
                verbose: bool = False) -> Union[np.ndarray, None]:
    """Triangulates a ``cls.CLS``.

    Parameters
    ----------
    shape : cls.CLS
        The CLS.
    verbose : bool, (default=`False`)
        Set to `True` to receive triangulation messages.

    Returns
    -------
    faces : (n_faces, 3) np.ndarray
        The faces.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> triangles = cls.triangulate(shape=shape)

    >>> shape = cls.CLS()
    >>> triangles = shape.mesh

    """
    if verify_parameters(shape=shape, verbose=verbose) is False:
        return None

    vertices = shape.vertices

    parameters = shape.parameters
    n_steps = parameters['n_steps']
    n_vertices_per_step = vertices.shape[0] // n_steps

    n_faces = 2 * n_vertices_per_step * (n_steps - 1)

    # faces = np.zeros((n_faces, 3), dtype=np.int32)
    faces = np.zeros((n_faces, 3), dtype=np.int32)

    # TODO: Add offset to for loop argument
    offset = 0
    for _ in range(n_steps - 1):
        for vertex_index in range(n_vertices_per_step):
            # bottom right vertex index
            index_br = offset + vertex_index

            # bottom left vertex index
            index_bl = index_br - 1
            if vertex_index == 0:
                index_bl += n_vertices_per_step

            # top right vertex index
            index_tr = index_br + n_vertices_per_step

            # top left vertex index
            index_tl = index_tr - 1
            if vertex_index == 0:
                index_tl += n_vertices_per_step

            # lower triangle
            lower_triangle = np.array([index_br, index_tl, index_bl])
            lower_triangle_index = offset + vertex_index
            faces[lower_triangle_index, :] = lower_triangle

            # upper triangle
            upper_triangle = np.array([index_br, index_tr, index_tl])
            upper_triangle_index = lower_triangle_index + \
                n_vertices_per_step * (n_steps - 1)
            faces[upper_triangle_index, :] = upper_triangle

        offset += n_vertices_per_step

    return faces
