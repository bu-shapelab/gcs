from __future__ import annotations

import json
import numpy as np
import cls
from cls._utils import _cartesian_to_polar
from stl.mesh import Mesh
    

# Parameter ranges
C1_BASE_RANGE = [0, 1.2]
C2_BASE_RANGE = [-1, 1]
C1_TOP_RANGE = [0, 1.2]
C2_TOP_RANGE = [-1, 1]
TWIST_LINEAR_RANGE = [0, 2 * np.pi]
TWIST_AMPLITUDE_RANGE = [0, np.pi]
TWIST_PERIOD_RANGE = [0, 3]
HEIGHT_RANGE = [10, 30]
MASS_RANGE = [1.5, 4]
PERIMETER_RATIO_RANGE = [1, 3]
THICKNESS_RANGE = [0.45, 1]


class CLS:
    """The continuous line structure (CLS) class.

    """

    def __init__(self, c1_base: float = 0, c2_base: float = 0, c1_top: float = 0,
                 c2_top: float = 0, twist_linear: float = 0, twist_amplitude: float = 0,
                 twist_period: float = 0, perimeter_ratio: float = 1, height: float = 19,
                 mass: float = 2.1, thickness: float = 0.75, density: float = 0.0012,
                 n_steps: int = 100, d_theta: float = 0.01) -> None:
        """Initialize the CLS.

        Parameters
        ----------
        c1_base : float (default=0)
            The base 4-lobe parameter.
        c2_base : float (default=0)
            The base 8-lobe parameter.
        c1_top : float (default=0)
            The top 4-lobe parameter.
        c2_top : float (default=0)
            The top 8-lobe parameter.
        twist_linear : float (default=0)
            The linear twist.
        twist_amplitude : float (default=0)
            The oscillating twist amplitude.
        twist_period : float (default=0)
            The oscillating twist period.
        perimeter_ratio : float (default=1)
            The top/base perimeter ratio.
        height : float (default=19)
            The target height (mm).
        mass : float (default=2.1)
            The target mass (g).
        thickness : float (default=0.75)
            The wall thickness (mm).
        density : float (default=0.0012)
            The material density (g/mm^3)
        n_steps : int (default=100)
            The number of height discretization steps.
        d_theta : float (default=0.01)
            The angular discretization step size.

        Examples
        --------
        >>> shape = cls.CLS()

        >>> shape = cls.CLS(mass=3.3, thickness=0.83)

        """
        self._c1_base = c1_base
        self._c2_base = c2_base
        self._c1_top = c1_top
        self._c2_top = c2_top
        self._twist_linear = twist_linear
        self._twist_amplitude = twist_amplitude
        self._twist_period = twist_period
        self._perimeter_ratio = perimeter_ratio
        self._height = height
        self._mass = mass
        self._thickness = thickness
        self._density = density
        self._n_steps = n_steps
        self._theta_step = d_theta

        self._vertices = None
        self._faces = None

    @property
    def parameters(self) -> dict:
        """The CLS parameters.

        """
        return {
            'c1_base': self._c1_base,
            'c2_base': self._c2_base,
            'c1_top': self._c1_top,
            'c2_top': self._c2_top,
            'twist_linear': self._twist_linear,
            'twist_amplitude': self._twist_amplitude,
            'twist_period': self._twist_period,
            'perimeter_ratio': self._perimeter_ratio,
            'height': self._height,
            'mass': self._mass,
            'thickness': self._thickness,
        }

    @property
    def valid(self) -> bool:
        """The CLS validity.

        Refer to ``cls.verify.verify_all`` for full documentation.

        """
        return cls.verify.verify_all(shape=self, verbose=False)

    @property
    def base_perimeter(self) -> float:
        """The CLS base perimeter.

        """
        return (2 * self._mass) / (self._density * self._height * self._thickness * (1 + self._perimeter_ratio))

    @property
    def top_perimeter(self) -> float:
        """The CLS top perimeter.

        """
        return (2 * self._mass * self._perimeter_ratio) / (self._density * self._height * self._thickness * (1 + self._perimeter_ratio))

    @property
    def vertices(self) -> np.ndarray:
        """The CLS vertices.

        Refer to ``cls.discretize`` for full documentation.

        """
        if self._vertices is None:
            self._vertices = cls.discretize(shape=self,
                                            n_steps=self._n_steps,
                                            theta_step=self._theta_step)
        return self._vertices

    @property
    def min_radius(self) -> np.ndarray:
        """The CLS minimum radius.

        """
        vertices = self.vertices
        vertices_2d_cartesian = vertices[:, :2]
        vertices_2d_polar = _cartesian_to_polar(points=vertices_2d_cartesian)
        radii = vertices_2d_polar[:, 1]
        radius = np.amin(radii)
        return radius

    @property
    def max_radius(self) -> np.ndarray:
        """The CLS maximum radius.

        """
        vertices = self.vertices
        vertices_2d_cartesian = vertices[:, :2]
        vertices_2d_polar = _cartesian_to_polar(points=vertices_2d_cartesian)
        radii = vertices_2d_polar[:, 1]
        radius = np.amax(radii)
        return radius

    @property
    def faces(self) -> np.ndarray:
        """The CLS faces defined by ``CLS.vertices``.
        
        Refer to ``cls.triangulate`` for full documentation.

        """
        if self._faces is None:
            self._faces = cls.triangulate(shape=self)
        return self._faces

    @property
    def mesh(self) -> Mesh:
        """The CLS mesh.

        References
        ----------
        .. [1] Creating Mesh objects from a list of vertices and faces:
            https://pypi.org/project/numpy-stl/

        """
        vertices = self.vertices
        faces = self.faces

        mesh = Mesh(np.zeros(faces.shape[0], dtype=Mesh.dtype))

        for idx, face in enumerate(faces):
            for dim in range(3):
                mesh.vectors[idx][dim] = vertices[face[dim], :]
        
        return mesh

    def __str__(self):
        output = f'{super().__str__()}: ' + json.dumps(obj=self.parameters, indent=2)
        return output
