from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np
import mapbox_earcut as earcut
from stl.mesh import Mesh

if TYPE_CHECKING:
    from cls import CLS


def _triangulate_face(shape: CLS, top: bool) -> np.ndarray:
    """Triangulates the base/top face of a CLS.

    The triangulation method is a modified ear slicing algorithm.

    Parameters
    ----------
    shape : cls.CLS
        The CLS.
    top : bool
        If `True`, the top face is triangulated.
        If `false`, the bottom face is triangulated.

    Returns
    -------
    tri : np.ndarray
        A (N, 3) matrix of N triangles. Each row contains the indices
        of the vertices forming the triangle.

    References
    ----------
    .. [1] https://github.com/mapbox/earcut.hpp

    """
    vertices = shape.vertices
    n_vertices_per_step = vertices.shape[0] // shape.n_steps
    
    face_vertices = vertices[:n_vertices_per_step, :2]
    if top:
        face_vertices = vertices[-n_vertices_per_step:, :2]

    rings = np.array([face_vertices.shape[0]])

    # triangulation is a single vector of all vertex indices
    # every 3 indices is a triangle
    triangulation = earcut.triangulate_float32(face_vertices, rings)

    # reshape to (n x 3) matrix
    triangulation = triangulation.reshape((-1, 3))

    # reverse order of triangles on bottom for outward facing normals
    if not top:
        triangulation = np.fliplr(m=triangulation)
    
    # offset to be last step
    offset = (shape.n_steps - 1) * n_vertices_per_step
    if top:
        triangulation = triangulation + offset

    return triangulation


def triangulate(shape: CLS) -> Mesh:
    """Triangulates a CLS.

    Parameters
    ----------
    shape : cls.CLS
        The CLS.

    Returns
    -------
        mesh : stl.mesh.Mesh
            The triangulated mesh.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> mesh = cls.triangulate(shape=shape)

    >>> shape = cls.CLS()
    >>> mesh = shape.mesh

    """

    triangulation_base = _triangulate_face(shape=shape, top=False)
    triangulation_top = _triangulate_face(shape=shape, top=True)

    vertices = shape.vertices

    n_steps = shape.n_steps
    n_vertices_per_step = vertices.shape[0] // shape.n_steps

    n_facets_base = triangulation_base.shape[0]
    n_facets_top = triangulation_top.shape[0]
    n_facets_side = 2 * n_vertices_per_step * (n_steps - 1)

    n_facets = n_facets_side + n_facets_base + n_facets_top

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

    # add base triangles
    offset = n_facets_side
    triangulation[offset:offset+n_facets_base, :] = triangulation_base

    # add top triangles
    offset += n_facets_base
    triangulation[offset:offset+n_facets_top, :] = triangulation_top

    triangulation = triangulation.astype(int)

    return triangulation
