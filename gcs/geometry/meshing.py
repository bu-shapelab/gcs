from __future__ import annotations

from typing import TYPE_CHECKING

import mapbox_earcut as earcut
import numpy as np

from .coordinates import pol2cart
from .polar_curves import optimal_scaling_factor
from .summed_cosine import summed_cosine

if TYPE_CHECKING:
    from ..shape import GCS


def generate_vertices(shape: GCS) -> np.ndarray:
    """Generates the vertices of a GCS.

    Parameters
    ----------
    shape : gcs.GCS
        GCS shape.

    Returns
    -------
    vertices : (N, 3) np.ndarray
        Vertices.

    """
    parameters = shape.parameters

    thetas = np.arange(start=0, stop=2 * np.pi, step=parameters['theta_step'])
    c4s = np.linspace(start=parameters['c4_base'],
                      stop=parameters['c4_top'],
                      num=parameters['n_height_steps'])
    c8s = np.linspace(start=parameters['c8_base'],
                      stop=parameters['c8_top'],
                      num=parameters['n_height_steps'])
    perimeters = np.linspace(start=shape.base_perimeter,
                             stop=shape.top_perimeter,
                             num=parameters['n_height_steps'])
    twists_linear = np.linspace(start=0,
                                stop=parameters['twist_linear'],
                                num=parameters['n_height_steps'])
    frequencies = np.linspace(start=0,
                              stop=2 * np.pi * parameters['twist_cycles'],
                              num=parameters['n_height_steps'])
    twists_oscillating = parameters['twist_amplitude'] * np.sin(frequencies)

    height_per_step = parameters['height'] / (parameters['n_height_steps'] - 1)

    vertices = np.empty(shape=(parameters['n_height_steps'], thetas.size, 3), dtype=float)

    for step in range(parameters['n_height_steps']):
        c4 = c4s[step]
        c8 = c8s[step]
        perimeter = perimeters[step]
        twist_linear = twists_linear[step]
        twist_oscillating = twists_oscillating[step]
        height = height_per_step * step

        r0 = optimal_scaling_factor(length=perimeter, c4=c4, c8=c8, n_steps=thetas.size)

        step_thetas = thetas + twist_linear + twist_oscillating
        r = summed_cosine(theta=step_thetas, r0=r0, c4=c4, c8=c8)

        x, y = pol2cart(r=r, theta=thetas)

        vertices[step, :, 0] = x
        vertices[step, :, 1] = y
        vertices[step, :, 2] = height

    return vertices.reshape(-1, 3)


def generate_faces(shape: GCS) -> np.ndarray:
    """Generates the faces of a GCS.

    Parameters
    ----------
    shape : gcs.GCS
        GCS shape.

    Returns
    -------
    faces : (N, 3) np.ndarray
        Faces.

    """
    parameters = shape.parameters

    vertices = shape.vertices

    n_vertices_per_step = vertices.shape[0] // parameters['n_height_steps']

    vertex_indicies = np.arange(start=0, stop=vertices.shape[0], dtype=int)
    vertex_grid = vertex_indicies.reshape(parameters['n_height_steps'], n_vertices_per_step)

    bottom_right = vertex_grid[:-1, :]
    bottom_left = np.roll(a=bottom_right, shift=1, axis=1)
    top_right = vertex_grid[1:, :]
    top_left = np.roll(a=top_right, shift=1, axis=1)

    lower_faces = np.stack((bottom_right, top_left, bottom_left), axis=-1).reshape(-1, 3)
    upper_faces = np.stack((bottom_right, top_right, top_left), axis=-1).reshape(-1, 3)

    faces = np.vstack((lower_faces, upper_faces))

    if parameters['triangulate_caps']:
        base_vertices = vertices[:n_vertices_per_step:, :2]
        top_vertices = vertices[-n_vertices_per_step:, :2]

        # from mapbox_earcut:
        # An array of end-indices for each ring (1st ring is outer contour of the polygon).
        rings = np.array([n_vertices_per_step])

        triangles_indices_base = earcut.triangulate_float32(base_vertices, rings)
        triangles_indices_top = earcut.triangulate_float32(top_vertices, rings)

        # offset top indices to correct indices
        triangles_indices_top += (vertices.shape[0] - n_vertices_per_step)

        faces_base = triangles_indices_base.reshape(-1, 3)
        faces_top = triangles_indices_top.reshape(-1, 3)

        # Flip order of base vertices for outward facing normals
        faces_base = np.fliplr(m=faces_base)

        faces = np.vstack((faces, faces_base, faces_top))

    return faces
