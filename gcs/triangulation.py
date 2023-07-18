from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np


if TYPE_CHECKING:
    import gcs


def triangulate(shape: gcs.GCS) -> np.ndarray:
    """Triangulates a GCS.

    Parameters
    ----------
    shape : gcs.GCS
        The GCS.

    Returns
    -------
    faces : (N, 3) np.ndarray
        The faces.

    Examples
    --------
    >>> shape = gcs.GCS(...)
    >>> faces = gcs.triangulate(shape=shape)

    >>> shape = gcs.GCS(...)
    >>> faces = gcs.faces

    """
    vertices = shape.vertices

    parameters = shape.parameters
    n_steps = parameters['n_steps']
    n_vertices_per_step = vertices.shape[0] // n_steps

    n_faces = 2 * n_vertices_per_step * (n_steps - 1)

    faces = np.zeros((n_faces, 3), dtype=np.int32)

    for step in range(n_steps - 1):
        offset = step * n_vertices_per_step
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

    return faces
