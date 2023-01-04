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
    step = 0
    if top:
        step = -1

    vertices = shape.vertices[:, :2, step]

    rings = np.array([vertices.shape[0]])

    # triangulation is a single vector of all vertex indices
    # every 3 indices is a triangle
    triangulation = earcut.triangulate_float32(vertices, rings)

    # reshape to (n x 3) matrix
    triangulation = triangulation.reshape((-1, 3))

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
    n_vertices_step = vertices.shape[0]
    n_steps = vertices.shape[2]
    n_triangles_base = triangulation_base.shape[0]
    n_triangles_top = triangulation_top.shape[0]
    n_triangles_side = 2 * n_vertices_step * (n_steps - 1)

    n_facets = n_triangles_base + n_triangles_top + n_triangles_side

    data = np.zeros(n_facets, dtype=Mesh.dtype)

    # add base triangles to mesh
    for idx in range(n_triangles_base):
        points_idx = triangulation_base[idx]
        # counter-clockwise order for outward facing normals
        points_idx = np.flip(points_idx)
        data['vectors'][idx] = vertices[points_idx, :, 0]

    # # add top triangles to mesh
    offset = n_triangles_base
    for idx in range(n_triangles_top):
        points_idx = triangulation_top[idx]
        data['vectors'][idx + offset] = vertices[points_idx, :, -1]

    # add side triangles to mesh
    offset += n_triangles_top
    for step_idx in range(n_steps - 1):
        for vertex_idx in range(n_vertices_step):
            # bottom right vertex
            p0 = vertices[vertex_idx, :, step_idx].reshape(1, -1)
            # top right vertex
            p1 = vertices[vertex_idx, :, step_idx + 1].reshape(1, -1)
            # top left vertex
            p2 = vertices[vertex_idx - 1, :, step_idx + 1].reshape(1, -1)
            # bottom left vertex
            p3 = vertices[vertex_idx - 1, :, step_idx].reshape(1, -1)

            # lower triangle
            data['vectors'][offset + 2 * vertex_idx] = np.concatenate((p0, p2, p3), axis=0)
            # upper triangle
            data['vectors'][offset + 2 * vertex_idx + 1] = np.concatenate((p0, p1, p2), axis=0)
        offset += 2 * n_vertices_step

    triangulation = Mesh(data)
    return triangulation
