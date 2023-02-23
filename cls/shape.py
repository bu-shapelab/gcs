from __future__ import annotations

import numpy as np
import cls
from cls._utils import _cartesian_to_polar
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

# The minimum height (mm).
MIN_HEIGHT = 1

# The minimum mass (g).
MIN_MASS = 1

# Valid range of top/base perimeter ratio values.
PERIMETER_RATIO_RANGE = [1, 3]

# Valid range of wall thickness values (mm).
THICKNESS_RANGE = [0.45, 1]


class CLS:
    """The continuous line structure (CLS) class.

    """

    def __init__(self, c1_base: float = 0, c2_base: float = 0, c1_top: float = 0,
                 c2_top: float = 0, twist_linear: float = 0, twist_amplitude: float = 0,
                 twist_period: float = 0, perimeter_ratio: float = 1, height: float = 19,
                 mass: float = 2.1, thickness: float = 0.75, fix: bool = False) -> None:
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
        fix : bool (default=False)
            Set to `True` to set invalid parameters to the closest valid value.

        Examples
        --------
        >>> shape = cls.CLS()

        >>> shape = cls.CLS(mass=3.3, thickness=0.83)

        """
        self._c1_base = c1_base
        if fix:
            if self._c1_base < C1_BASE_RANGE[0]:
                self._c1_base = C1_BASE_RANGE[0]
            elif self._c1_base > C1_BASE_RANGE[1]:
                self._c1_base = C1_BASE_RANGE[1]
        self._c2_base = c2_base
        if fix:
            if self._c2_base < C2_BASE_RANGE[0]:
                self._c2_base = C2_BASE_RANGE[0]
            elif self._c2_base > C2_BASE_RANGE[1]:
                self._c2_base = C2_BASE_RANGE[1]
        self._c1_top = c1_top
        if fix:
            if self._c1_top < C1_TOP_RANGE[0]:
                self._c1_top = C1_TOP_RANGE[0]
            elif self._c1_top > C1_TOP_RANGE[1]:
                self._c1_top = C1_TOP_RANGE[1]
        self._c2_top = c2_top
        if fix:
            if self._c2_top < C2_TOP_RANGE[0]:
                self._c2_top = C2_TOP_RANGE[0]
            elif self._c2_top > C2_TOP_RANGE[1]:
                self._c2_top = C2_TOP_RANGE[1]
        self._twist_linear = twist_linear
        if fix:
            if self._twist_linear < TWIST_LINEAR_RANGE[0]:
                self._twist_linear = TWIST_LINEAR_RANGE[0]
            elif self._twist_linear > TWIST_LINEAR_RANGE[1]:
                self._twist_linear = TWIST_LINEAR_RANGE[1]
        self._twist_amplitude = twist_amplitude
        if fix:
            if self._twist_amplitude < TWIST_AMPLITUDE_RANGE[0]:
                self._twist_amplitude = TWIST_AMPLITUDE_RANGE[0]
            elif self._twist_amplitude > TWIST_AMPLITUDE_RANGE[1]:
                self._twist_amplitude = TWIST_AMPLITUDE_RANGE[1]
        self._twist_period = twist_period
        if fix:
            if self._twist_period < TWIST_PERIOD_RANGE[0]:
                self._twist_period = TWIST_PERIOD_RANGE[0]
            elif self._twist_period > TWIST_PERIOD_RANGE[1]:
                self._twist_period = TWIST_PERIOD_RANGE[1]
        self._perimeter_ratio = perimeter_ratio
        if fix:
            if self._perimeter_ratio < PERIMETER_RATIO_RANGE[0]:
                self._perimeter_ratio = PERIMETER_RATIO_RANGE[0]
            elif self._perimeter_ratio > PERIMETER_RATIO_RANGE[1]:
                self._perimeter_ratio = PERIMETER_RATIO_RANGE[1]
        self._height = height
        if fix:
            if self._height < MIN_HEIGHT:
                self._height = MIN_HEIGHT
        self._mass = mass
        if fix:
            if self._mass < MIN_MASS:
                self._mass = MIN_MASS
        self._thickness = thickness
        if fix:
            if self._thickness < THICKNESS_RANGE[0]:
                self._thickness = THICKNESS_RANGE[0]
            elif self._thickness > THICKNESS_RANGE[1]:
                self._thickness = THICKNESS_RANGE[1]

        # Material density (g/mm^3)
        self._density = 0.0012

        # The number of height discretization steps.
        self._n_steps = 100

        # The angular discretization step size
        self._theta_step = 0.01

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
                                            n_steps=self.n_steps,
                                            theta_step=self.theta_step)
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

    @property
    def n_steps(self) -> int:
        """The number of height discretization steps.

        """
        return self._n_steps
    
    @n_steps.setter
    def n_steps(self, steps: int) -> None:
        """Set the number of height discretization steps.

        """
        if isinstance(steps, int) and steps > 0:
            self._n_steps = steps

    @property
    def theta_step(self) -> int:
        """The angular discretization step size.

        """
        return self._theta_step
    
    @theta_step.setter
    def theta_step(self, step: float) -> None:
        """Set the angular discretization step size.

        """
        if isinstance(step, (int, float)) and step > 0 and step < 2 * np.pi:
            self._theta_step = step

    def copy(self) -> CLS:
        """Get a copy of the CLS.

        Returns
        -------
        shape : cls.CLS
            A copy of the shape.

        """
        parameters = self.parameters
        copy_shape = CLS(**parameters)
        copy_shape.n_steps = self.n_steps

        return copy_shape

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
