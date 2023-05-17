from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np

if TYPE_CHECKING:
    from cls import CLS


def triangulate(shape: CLS) -> np.ndarray:
    """Triangulates a CLS.

    Parameters
    ----------
    shape : cls.CLS
        The CLS.

    Returns
    -------
        triangles : (n_triangles, 3) np.ndarray
            The triangles.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> triangles = cls.triangulate(shape=shape)

    >>> shape = cls.CLS()
    >>> triangles = shape.mesh

    """
    vertices = shape.vertices

    n_steps = shape.n_steps
    n_vertices_per_step = vertices.shape[0] // shape.n_steps

    n_facets = 2 * n_vertices_per_step * (n_steps - 1)

    triangulation = np.zeros((n_facets, 3))

    # add side triangles
    offset = 0
    for _ in range(n_steps - 1):
        for vertex_idx in range(n_vertices_per_step):
            # bottom right vertex idx
            idx_br = offset + vertex_idx
            
            # bottom left vertex idx
            idx_bl = idx_br - 1
            if vertex_idx == 0:
                idx_bl += n_vertices_per_step

            # top right vertex idx
            idx_tr = idx_br + n_vertices_per_step

            # top left vertex idx
            idx_tl = idx_tr - 1
            if vertex_idx == 0:
                idx_tl += n_vertices_per_step

            # lower triangle
            lower_trianlge_idx = offset + vertex_idx
            triangulation[lower_trianlge_idx, :] = np.array([idx_br, idx_tl, idx_bl])

            # upper triangle
            upper_trianlge_idx = lower_trianlge_idx + n_vertices_per_step * (n_steps - 1)
            triangulation[upper_trianlge_idx, :] = np.array([idx_br, idx_tr, idx_tl])

        offset += n_vertices_per_step

    triangulation = triangulation.astype(int)

    return triangulation
