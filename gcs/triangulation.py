from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np
import mapbox_earcut as earcut


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
    triangulate_faces = shape.parameters['triangulate_faces']

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

    if triangulate_faces:
        base_vertices = vertices[:n_vertices_per_step:, :2]
        top_vertices = vertices[-n_vertices_per_step:, :2]

        # from mapbox_earcut:
        # An array of end-indices for each ring (1st ring is outer contour of the polygon).
        rings = np.array([n_vertices_per_step])

        triangles_indices_base = earcut.triangulate_float32(base_vertices, rings)
        triangles_indices_top = earcut.triangulate_float32(top_vertices, rings)

        # offset top indices to correct indices
        triangles_indices_top = triangles_indices_top + (vertices.shape[0] - n_vertices_per_step)

        faces_base = triangles_indices_base.reshape(-1, 3)
        faces_top = triangles_indices_top.reshape(-1, 3)

        # Flip order of base vertices for outward facing normals
        faces_base = np.fliplr(m=faces_base)

        faces = np.vstack((faces, faces_base, faces_top))

    return faces
