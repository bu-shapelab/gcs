from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from stl import mesh
import mapbox_earcut as earcut

from utils import (find_scaling_factor,
                   summed_cosine_radii,
                   polar_to_cartesian,
                   cartesian_to_polar,
                   self_intersection,
                   offset_curve)

class CLS:
    """Continuous Line Structure shape.
    """
    def __init__(self, c1_base: float = 0, c2_base: float = 0, c1_top: float = 0,
                 c2_top: float = 0, twist_linear: float = 0, twist_amplitude: float = 0,
                 twist_period: float = 0, ratio: float = 1, height: float = 19,
                 mass: float = 2.1, density: float = 0.0016, thickness: float = 0.75,
                 n_steps: int = 100) -> None:
        """Initialize CLS.

        Args:
            c1_base: The base 4-lobe parameter.
            c2_base: The base 8-lobe parameter.
            c1_top: The top 4-lobe parameter.
            c2_top: The top 8-lobe parameter.
            twist_linear: The linear component of twist.
            twist_amplitude: The amplitude of the oscillating component of twist.
            twist_period: The period of the oscillating component of twist.
            ratio: The ratio of the base to top perimeter.
            height: The height.
            mass: The mass.
            density: The density.
            thickness: The wall thickness.
            n_steps: Number of interpolation steps.
        """
        # Interpolate c1s and c2s
        self._c1s = np.linspace(c1_base, c1_top, n_steps)
        self._c2s = np.linspace(c2_base, c2_top, n_steps)

        # Combine linear and oscillating twist
        linear = np.linspace(0, twist_linear, n_steps)
        oscillating = twist_amplitude * np.sin(np.linspace(0, 2 * np.pi * twist_period, n_steps))
        self._twists = linear + oscillating

        # Find top and bottom scaling factors and interpolate
        base_perimeter = (2 * mass) / (density * height * thickness * (1 + ratio))
        top_perimeter = (2 * mass * ratio) / (density * height * thickness * (1 + ratio))

        self._perimeters  = np.linspace(base_perimeter, top_perimeter, n_steps)
        # R_base = find_scaling_factor(perimeter=base_perimeter, c1=c1_base, c2=c2_base)
        # R_top = find_scaling_factor(perimeter=top_perimeter, c1=c1_top, c2=c2_top)

        # self._Rs = np.linspace(R_base, R_top, n_steps)

        self._height = height
        self._thickness = thickness
        self._n_steps = n_steps

        self._vertices = self._discretize()
        self._mesh = self._triangulate()

        self._flag_small_radius = False
        self._flag_self_intersection = False

    def _discretize(self) -> np.ndarray:
        """Discretize the CLS into vertices.

        Returns:
            The 3D vertices of the shape. The vertices are a tensor of the form
            `(number of vertices) x 3 x (number of steps)`.

            Thus the vertices of step `i` are contained in the matrix

            `_discretize()[:, :, i]`

            with the first column containing the `x`-values, the second column
            containing the `y`-values and the third column containing the `z`-values.
        """
        step_height = self._height / (self._n_steps - 1)

        theta_step = 0.01
        theta = np.arange(0, 2 * np.pi, theta_step)

        # 3D vertices tensor
        vertices_3d = np.empty((theta.size, 3, self._n_steps))

        self._max_radii = []
        self._min_radii = []
        self._radius_0 = []

        for step in range(self._n_steps):
            # CLS parameters for current slice
            c1 = self._c1s[step]
            c2 = self._c2s[step]
            r0 = find_scaling_factor(perimeter=self._perimeters[step], c1=c1, c2=c2)
            # R = self._Rs[step]
            twist = self._twists[step]
            height = step_height * step

            radii = summed_cosine_radii(theta=theta + twist, r0=r0, c1=c1, c2=c2)

            vertices_2d = polar_to_cartesian(theta=theta, radii=radii)

            vertices_3d[:, :2, step] = vertices_2d
            vertices_3d[:, 2, step] = height

        return vertices_3d

    def _triangulate(self) -> mesh.Mesh:
        """Triangulates the CLS to STL format.

        Returns:
            The triangulated mesh.
        """
        # triangulate base face
        verts = self._vertices[:, :2, 0]
        rings = np.array([verts.shape[0]])
        result_base = earcut.triangulate_float32(verts, rings)
        n_facets_base = result_base.shape[0]

        # triangulate top face
        verts = self._vertices[:, :2, -1]
        rings = np.array([verts.shape[0]])
        result_top = earcut.triangulate_float32(verts, rings)
        n_facets_top = result_top.shape[0]

        n_vertices = self._vertices.shape[0]

        n_facets = 2 * n_vertices * (self._n_steps - 1) + n_facets_base + n_facets_top

        data = np.zeros(n_facets, dtype=mesh.Mesh.dtype)

        # add base triangles to mesh
        for facet_idx in range(0, n_facets_base, 3):
            points_idx = result_base[facet_idx:facet_idx + 3]
            # counter-clockwise order for outward facing normals
            points_idx = np.flip(points_idx)
            data['vectors'][facet_idx] = self._vertices[points_idx, :, 0]

        # add top triangles to mesh
        offset = n_facets_base
        for facet_idx in range(0, n_facets_top, 3):
            points_idx = result_top[facet_idx:facet_idx + 3]
            data['vectors'][offset + facet_idx] = self._vertices[points_idx, :, -1]

        # add side triangles to mesh
        offset = n_facets_base + n_facets_top
        for step_idx in range(self._n_steps - 1):
            for vertex_idx in range(n_vertices):
                # bottom right vertex
                p0 = self._vertices[vertex_idx, :, step_idx].reshape(1, -1)
                # top right vertex
                p1 = self._vertices[vertex_idx, :, step_idx + 1].reshape(1, -1)
                # top left vertex
                p2 = self._vertices[vertex_idx - 1, :, step_idx + 1].reshape(1, -1)
                # bottom left vertex
                p3 = self._vertices[vertex_idx - 1, :, step_idx].reshape(1, -1)

                # lower triangle
                data['vectors'][offset + 2 * vertex_idx] = np.concatenate((p0, p2, p3), axis=0)
                # upper triangle
                data['vectors'][offset + 2 * vertex_idx + 1] = np.concatenate((p0, p1, p2), axis=0)
            offset += 2 * n_vertices

        return mesh.Mesh(data)

    def is_valid(self, verbose=False) -> bool:
        """Checks if the parameters form a valid CLS shape. The following
        validity checks are performed on the top and bottom shapes:

        1. Radius too small.
        2. Self intersection.

        Args:
            verbose: If `True`, validity messages are printed to console.
        Returns:
            `True` if the CLS is valid, `False` otherwise.
        """

        if verbose is True:
            print("Performing validity check")

        # Only need to perform validity checks for base/top
        # since interpolating between the two
        # Also, dont need z-dimension for checks
        vertices_base = self._vertices[:, :2, 0]
        vertices_base_outer = offset_curve(vertices_base, self._thickness / 2)
        vertices_base_inner = offset_curve(vertices_base, -self._thickness / 2)

        vertices_top = self._vertices[:, :2, -1]
        vertices_top_outer = offset_curve(vertices_base, self._thickness / 2)
        vertices_top_inner = offset_curve(vertices_base, -self._thickness / 2)

        _, radii_base = cartesian_to_polar(vertices_base)
        _, radii_top = cartesian_to_polar(vertices_top)

        min_radius = 0.01
        min_radius_base = np.amin(radii_base)
        min_radius_top = np.amin(radii_top)

        message = 'Valid CLS.'
        valid = True

        if min_radius_base < min_radius:
            message = f'Invalid CLS: Base radius too small ({min_radius_base}).'
            valid = False
        elif min_radius_top < min_radius:
            message = f'Invalid CLS: Top radius too small ({min_radius_top}).'
            valid = False
        elif self_intersection(vertices_base) is True:
            message = 'Invalid CLS: Base self intersection.'
            valid = False
        elif self_intersection(vertices_base_outer) is True:
            message = 'Invalid CLS: Base (outer) self intersection.'
            valid = False
        elif self_intersection(vertices_base_inner) is True:
            message = 'Invalid CLS: Base (inner) self intersection.'
            valid = False
        elif self_intersection(vertices_top) is True:
            message = 'Invalid CLS: Top self intersection.'
            valid = False
        elif self_intersection(vertices_top_outer) is True:
            message = 'Invalid CLS: Top (outer) self intersection.'
            valid = False
        elif self_intersection(vertices_top_inner) is True:
            message = 'Invalid CLS: Top (inner) self intersection.'
            valid = False

        if verbose is True:
            print(message)
        return valid

    def summary(self) -> None:
        """Visualize a summary of the CLS shape. Specifically, visualization of
           the base shape, top shape, and twist component are shown.
        """
        # base shape
        ax = plt.subplot(221, projection='polar')

        vertices = self._vertices[:, :2, 0]
        theta, radii = cartesian_to_polar(vertices)
        ax.plot(theta, radii, color='C0')

        vertices_offset = offset_curve(vertices, self._thickness / 2)
        theta, radii = cartesian_to_polar(vertices_offset)
        ax.plot(theta, radii, color='C1')

        vertices_offset = offset_curve(vertices, -self._thickness / 2)
        theta, radii = cartesian_to_polar(vertices_offset)
        ax.plot(theta, radii, color='C1')

        ax.set_title('Base')

        # top shape
        ax = plt.subplot(222, projection='polar')

        vertices = self._vertices[:, :2, -1]
        theta, radii = cartesian_to_polar(vertices)
        ax.plot(theta, radii, color='C0')

        vertices_offset = offset_curve(vertices, self._thickness / 2)
        theta, radii = cartesian_to_polar(vertices_offset)
        ax.plot(theta, radii, color='C1')

        vertices_offset = offset_curve(vertices, -self._thickness / 2)
        theta, radii = cartesian_to_polar(vertices_offset)
        ax.plot(theta, radii, color='C1')

        ax.set_title('Top')

        # twist shape
        ax = plt.subplot(212)

        y = self._twists
        x = np.linspace(0, 1, self._twists.shape[0])
        ax.plot(x, y)
        ax.set_title('Twist')

        plt.show()

    def save(self, path: str) -> None:
        """Save the CLS to an STL file.

        Args:
            path: The path to the STL file.
        """
        self._mesh.save(path)
