from __future__ import annotations

from typing import Union
import json
import numpy as np
from stl.mesh import Mesh
import cls

# The assumed material density
MATERIAL_DENSITY = 0.0012 # g/mm^3

class CLS:
    """The continuous line structure (CLS) class.

    """

    def __init__(self,
                 c1_base: float,
                 c2_base: float,
                 c1_top: float,
                 c2_top: float,
                 twist_linear: float,
                 twist_amplitude: float,
                 twist_period: float,
                 angle: float,
                 height: float,
                 mass: float,
                 thickness: float,
                 n_steps: int = 100,
                 d_theta: float = 0.01) -> None:
        """Initialize the CLS.

        Parameters
        ----------
        c1_base : float
            The base 4-lobe parameter.
        c2_base : float
            The base 8-lobe parameter.
        c1_top : float
            The top 4-lobe parameter.
        c2_top : float
            The top 8-lobe parameter.
        twist_linear : float
            The linear twist.
        twist_amplitude : float
            The oscillating twist amplitude.
        twist_period : float
            The oscillating twist period.
        angle : float
            The angle (degrees) from the top to base when
            ``c1_base=c2_base=c1_top=c2_top=0``.
        height : float
            The target height (mm).
        mass : float
            The target mass (g).
        thickness : float
            The wall thickness (mm).
        n_steps : int (default=100)
            The number of height discretization steps.
        d_theta : float (default=0.01)
            The angular discretization step size.

        """
        self._c1_base = c1_base
        self._c2_base = c2_base
        self._c1_top = c1_top
        self._c2_top = c2_top
        self._twist_linear = twist_linear
        self._twist_amplitude = twist_amplitude
        self._twist_period = twist_period
        self._angle = angle
        self._height = height
        self._mass = mass
        self._thickness = thickness
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
            'angle': self._angle,
            'height': self._height,
            'mass': self._mass,
            'thickness': self._thickness,
            'n_steps': self._n_steps,
            'd_theta': self._theta_step,
        }

    @property
    def valid_base_perimeter(self) -> bool:
        """`True` if the base perimeter is valid.

        Refer to ``cls.verify.verify_base_perimeter`` for full documentation.

        """
        return cls.verify.verify_base_perimeter(shape=self)

    @property
    def valid_radius(self) -> bool:
        """`True` if the radii are valid.

        Refer to ``cls.verify.verify_radius`` for full documentation.

        """
        return cls.verify.verify_radius(shape=self)

    @property
    def valid(self) -> bool:
        """`True` if the CLS is valid.

        Refer to ``cls.verify.verify`` for full documentation.

        """
        valid = cls.verify.verify(shape=self)
        return valid

    @property
    def base_perimeter(self) -> float:
        """The base perimeter.

        """
        angle = np.deg2rad(self._angle)
        radius = self._mass / (2 * MATERIAL_DENSITY * np.pi * self._height * self._thickness) \
                 - (self._height / 2) * np.tan(angle)
        perimeter = 2 * np.pi * radius
        return perimeter

    @property
    def top_perimeter(self) -> float:
        """The top perimeter.

        """
        angle = np.deg2rad(self._angle)
        radius = self._mass / (2 * MATERIAL_DENSITY * np.pi * self._height * self._thickness) \
                 + (self._height / 2) * np.tan(angle)
        perimeter = 2 * np.pi * radius
        return perimeter

    @property
    def vertices(self) -> Union[np.ndarray, None]:
        """The vertices.

        Refer to ``cls.discretize`` for full documentation.

        """
        if self._vertices is None:
            self._vertices = cls.discretize(shape=self)
        return self._vertices

    @property
    def faces(self) -> np.ndarray:
        """The faces.

        Refer to ``cls.triangulate`` for full documentation.

        """
        if self._faces is None:
            self._faces = cls.triangulate(shape=self)
        return self._faces

    @property
    def mesh(self) -> Mesh:
        """The mesh.

        References
        ----------
        [1] Creating Mesh objects from a list of vertices and faces:
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
        output = f'{super().__str__()}: ' + \
            json.dumps(obj=self.parameters, indent=2)
        return output
