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
                 cap_height: float = 0, mass: float = 2.1, density: float = 0.0016,
                 thickness: float = 0.75, n_steps: int = 100) -> None:
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
            height: The height of the part.
            cap_height: The height of the cap.
            mass: The mass.
            density: The density.
            thickness: The wall thickness.
            n_steps: Number of interpolation steps.
        """
        self._c1_base = c1_base
        self._c2_base = c2_base
        self._c1_top = c1_top
        self._c2_top = c2_top
        self._twist_linear = twist_linear
        self._twist_amplitude = twist_amplitude
        self._twist_period = twist_period
        self._ratio = ratio
        self._height = height
        self._cap_height = cap_height
        self._mass = mass
        self._density = density
        self._thickness = thickness
        self._n_steps = n_steps

        # Interpolate parameters
        self._c1s = None
        self._c2s = None
        self._perimeters = None
        self._twists = None
        self._interpolate_parameters()

        # Discretize the shape
        self._vertices = None
        self._max_radius = 0
        self._discretize()

        # Create a mesh from the discretization
        self._mesh = None
        self._triangulate()

    def _interpolate_parameters(self) -> None:
        """Interpolates the parameters.
        """
        # c1s and c2s
        self._c1s = np.linspace(self._c1_base, self._c1_top, self._n_steps)
        self._c2s = np.linspace(self._c2_base, self._c2_top, self._n_steps)

        # perimeters
        base_perimeter = (2 * self._mass) / \
                         (self._density * self._height * self._thickness * (1 + self._ratio))
        top_perimeter = (2 * self._mass * self._ratio) / \
                        (self._density * self._height * self._thickness * (1 + self._ratio))
        self._perimeters  = np.linspace(base_perimeter, top_perimeter, self._n_steps)

        # twists
        twists_linear = np.linspace(0, self._twist_linear, self._n_steps)
        twists_oscillating = self._twist_amplitude * \
                             np.sin(np.linspace(0, 2 * np.pi * self._twist_period, self._n_steps))
        self._twists = twists_linear + twists_oscillating

    def _discretize(self) -> None:
        """Discretize the CLS into vertices.

        The vertices are stored in `self._vertices` as a tensor of the form:

        `(number of vertices) x 3 x (number of steps)`.
        """
        height_per_step = self._height / (self._n_steps - 1)

        theta = np.arange(0, 2 * np.pi, 0.01)

        # 3D vertices tensor
        self._vertices = np.empty((theta.size, 3, self._n_steps))

        for step in range(self._n_steps):
            # CLS parameters for current slice
            c1 = self._c1s[step]
            c2 = self._c2s[step]
            r0 = find_scaling_factor(perimeter=self._perimeters[step], c1=c1, c2=c2)
            twist = self._twists[step]
            height = height_per_step * step

            radii = summed_cosine_radii(theta=theta + twist, r0=r0, c1=c1, c2=c2)
            max_radius = np.amax(radii)
            if max_radius > self._max_radius:
                self._max_radius = max_radius

            vertices_2d = polar_to_cartesian(theta=theta, radii=radii)

            self._vertices[:, :2, step] = vertices_2d
            self._vertices[:, 2, step] = height

    def _triangulate_face(self, top: bool) -> np.ndarray:
        """Triangulates the top or bottom face of the shape.

        The triangulation method is a modified ear slicing algorithm:
        https://github.com/mapbox/earcut.hpp

        Args:
            top: If `True`, the top face is triangulated. If `false`,
                 The bottom face is triangulated.

        Returns:
            An (n x 3) matrix of n triangles. Each row contains the indices
            of the vertices forming the triangle.
        """
        vertices_2d = self._vertices[:, :2, 0]
        if top is True:
            vertices_2d = self._vertices[:, :2, -1]

        rings = np.array([vertices_2d.shape[0]])

        # triangulation is a single vector of all vertex indices
        # every 3 indices is a triangle
        triangulation = earcut.triangulate_float32(vertices_2d, rings)

        # reshape to make it easier to interpret
        triangulation = triangulation.reshape((-1, 3))

        return triangulation

    def _triangulate(self) -> None:
        """Triangulates the CLS to STL format.

        Returns:
            The triangulated mesh.
        """
        # triangulate faces
        triangulation_base = self._triangulate_face(top=False)
        triangulation_top = self._triangulate_face(top=True)

        n_vertices = self._vertices.shape[0]

        n_facets = 2 * n_vertices * (self._n_steps - 1) + triangulation_base.shape[0] + triangulation_top.shape[0]

        data = np.zeros(n_facets, dtype=mesh.Mesh.dtype)

        # add base triangles to mesh
        for idx in range(triangulation_base.shape[0]):
            points_idx = triangulation_base[idx]
            # counter-clockwise order for outward facing normals
            points_idx = np.flip(points_idx)
            data['vectors'][idx] = self._vertices[points_idx, :, 0]

        # # add top triangles to mesh
        offset = triangulation_base.shape[0]
        for idx in range(triangulation_top.shape[0]):
            points_idx = triangulation_top[idx]
            data['vectors'][idx + offset] = self._vertices[points_idx, :, -1]

        # add side triangles to mesh
        offset = triangulation_base.shape[0] + triangulation_top.shape[0]
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

        self._mesh = mesh.Mesh(data)

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

    @property
    def max_radius(self) -> float:
        """The maximum radius of the shape.
        """
        return self._max_radius

    def __str__(self):
        output = (super().__str__()
                  + f':\n\tc1_base: {self._c1_base}'
                  + f'\n\tc2_base: {self._c2_base}'
                  + f'\n\tc1_top: {self._c1_top}'
                  + f'\n\tc2_top: {self._c2_top}'
                  + f'\n\ttwist_linear: {self._twist_linear}'
                  + f'\n\ttwist_amplitude: {self._twist_amplitude}'
                  + f'\n\ttwist_period: {self._twist_period}'
                  + f'\n\tratio: {self._ratio}'
                  + f'\n\theight: {self._height}mm'
                  + f'\n\theight: {self._cap_height}mm'
                  + f'\n\tmass: {self._mass}g'
                  + f'\n\tdensity: {self._density}g/mm^3'
                  + f'\n\tthickness: {self._thickness}mm'
                  + f'\n\tn_steps: {self._n_steps} steps')

        return output
