from __future__ import annotations

import numpy as np

from gcs import Cylinder
from gcs.geometry.meshing import generate_faces, generate_vertices
from ..constants import ATOL


def test_generate_vertices() -> None:
    """Tests for ``gcs.geometry.generate_vertices``.

    """
    # Cylinder vertices
    shape = Cylinder(height=25, mass=2, thickness=0.5, n_height_steps=5, theta_step=0.5)
    parameters = shape.parameters

    vertices = generate_vertices(shape=shape)

    assert vertices.ndim == 2
    assert vertices.shape[1] == 3

    vertices = vertices.reshape((parameters['n_height_steps'], -1, 3))

    # Base and top ring radii
    base_r = np.hypot(vertices[0, :, 0], vertices[0, :, 1])
    top_r = np.hypot(vertices[-1, :, 0], vertices[-1, :, 1])

    np.testing.assert_allclose(actual=base_r, desired=base_r[0], atol=ATOL)
    np.testing.assert_allclose(actual=top_r, desired=top_r[0], atol=ATOL)

    # Vertical vertex pair
    lower = vertices[0, 0, :]
    upper = vertices[1, 0, :]

    np.testing.assert_allclose(actual=lower[2], desired=0.0, atol=ATOL)
    np.testing.assert_allclose(actual=upper[2],
                               desired=parameters['height'] / (parameters['n_height_steps'] - 1),
                               atol=ATOL)
    np.testing.assert_allclose(actual=np.hypot(lower[0], lower[1]),
                               desired=np.hypot(upper[0], upper[1]),
                               atol=ATOL)


def test_generate_faces() -> None:
    """Tests for ``gcs.geometry.generate_faces``.

    """
    # Cylinder faces
    shape = Cylinder(height=25,
                     mass=2,
                     thickness=0.5,
                     n_height_steps=5,
                     theta_step=0.5,
                     triangulate_caps=False)
    parameters = shape.parameters

    faces = generate_faces(shape=shape)
    vertices = shape.vertices

    assert np.max(faces) == vertices.shape[0] - 1

    vertices = vertices.reshape((parameters['n_height_steps'], -1, 3))
    n_vertices_per_step = vertices.shape[1]

    assert faces.ndim == 2
    assert faces.shape[1] == 3
    assert np.min(faces) == 0

    # Side-face lower triangle
    lower = faces[1]

    np.testing.assert_array_equal(lower, np.array([1, n_vertices_per_step, 0]))
