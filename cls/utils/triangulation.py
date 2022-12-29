from __future__ import annotations

import numpy as np
import mapbox_earcut as earcut
from stl import mesh
from cls import CLS


def triangulate_step(shape: CLS, step: int) -> np.ndarray:
    """TODO Triangulates the top or bottom face of the shape.

        The triangulation method is a modified ear slicing algorithm:
        https://github.com/mapbox/earcut.hpp

        Args:
            top: If `True`, the top face is triangulated. If `false`,
                 The bottom face is triangulated.

        Returns:
            An (n x 3) matrix of n triangles. Each row contains the indices
            of the vertices forming the triangle.
    """
    vertices = shape.vertices[:, :2, step]

    rings = np.array([vertices.shape[0]])

    # triangulation is a single vector of all vertex indices
    # every 3 indices is a triangle
    triangulation = earcut.triangulate_float32(vertices, rings)

    # reshape to (n x 3) matrix
    triangulation = triangulation.reshape((-1, 3))

    return triangulation


def triangulate(shape: CLS, n_steps: int = 100) -> np.ndarray:
    """TODO
    """
    triangulation_base = triangulate_step(shape=shape, step=0)
    triangulation_top = triangulate_step(shape=shape, step=-1)

    vertices = shape.vertices
    n_vertices_slice = vertices.shape[0]
    n_triangles_base = triangulation_base.shape[0]
    n_triangles_top = triangulation_top.shape[0]
    n_triangles_side = 2 * n_vertices_slice * (n_steps - 1)

    n_facets = n_triangles_base + n_triangles_top + n_triangles_side

    data = np.zeros(n_facets, dtype=mesh.Mesh.dtype)

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
        for vertex_idx in range(n_vertices_slice):
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
        offset += 2 * n_vertices_slice

    triangulation = mesh.Mesh(data)
    return triangulation
