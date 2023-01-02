from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np
import cls
from .utils.coordinates import cartesian_to_polar

if TYPE_CHECKING:
    from stl.mesh import Mesh

# Valid range of c1 (base) values.
C1_BASE_RANGE = [0, 1.2]

# Valid range of c2 (base) values.
C2_BASE_RANGE = [-1, 1]

# Valid range of c1 (top) values.
C1_TOP_RANGE = [0, 1.2]

# Valid range of c2 (top) values.
C2_TOP_RANGE = [-1, 1]

# Valid range of clinear twist values.
TWIST_LINEAR_RANGE = [0, 2 * np.pi]

# Valid range of oscillating twist amplitude values.
TWIST_AMPLITUDE_RANGE = [0, np.pi]

# Valid range of oscillating twist period values.
TWIST_PERIOD_RANGE = [0, 3]

# Valid range of target height values.
HEIGHT_RANGE = [0, np.inf]

# Valid range target mass values.
MASS_RANGE = [0, np.inf]

# Valid range of top/base perimeter ratio values.
PERIMETER_RATIO_RANGE = [1, 3]

# Valid range of wall thickness values.
THICKNESS_RANGE = [0.45, 1]


class CLS:
    """The continuous line structure (CLS) class.
    """

    def __init__(self, c1_base: float = 0, c2_base: float = 0, c1_top: float = 0,
                 c2_top: float = 0, twist_linear: float = 0, twist_amplitude: float = 0,
                 twist_period: float = 0, perimeter_ratio: float = 1, height: float = 19,
                 mass: float = 2.1, thickness: float = 0.75) -> None:
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

        Examples
        --------
        TODO

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

        # Material density (g/mm^3)
        self._density = 0.0012

        # Number of discretization steps
        self._n_steps = 100

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
        return cls.discretize(shape=self, n_steps=self._n_steps)

    @property
    def min_radius(self) -> np.ndarray:
        """The CLS minimum radius.
        """
        radius = np.inf
        vertices = self.vertices
        for step in range(self._n_steps):
            vertices_2d_cartesian = vertices[:, :2, step]
            vertices_2d_polar = cartesian_to_polar(points=vertices_2d_cartesian)
            radii = vertices_2d_polar[:, 1]
            step_radius = np.amin(radii)
            if step_radius < radius:
                radius = step_radius
        return radius

    @property
    def max_radius(self) -> np.ndarray:
        """The CLS maximum radius.
        """
        radius = 0
        vertices = self.vertices
        for step in range(self._n_steps):
            vertices_2d_cartesian = vertices[:, :2, step]
            vertices_2d_polar = cartesian_to_polar(points=vertices_2d_cartesian)
            radii = vertices_2d_polar[:, 1]
            step_radius = np.amax(radii)
            if step_radius > radius:
                radius = step_radius
        return radius

    @property
    def mesh(self) -> Mesh:
        """The CLS mesh.

        Refer to ``cls.triangulate`` for full documentation.
        """
        return cls.triangulate(shape=self)

    def __str__(self):
        output = (super().__str__()
                  + f':\n\tc1_base: {self._c1_base}'
                  + f'\n\tc2_base: {self._c2_base}'
                  + f'\n\tc1_top: {self._c1_top}'
                  + f'\n\tc2_top: {self._c2_top}'
                  + f'\n\ttwist_linear: {self._twist_linear}'
                  + f'\n\ttwist_amplitude: {self._twist_amplitude}'
                  + f'\n\ttwist_period: {self._twist_period}'
                  + f'\n\tperimeter_ratio: {self._perimeter_ratio}'
                  + f'\n\theight: {self._height}mm'
                  + f'\n\tmass: {self._mass}g'
                  + f'\n\tthickness: {self._thickness}mm')

        return output
