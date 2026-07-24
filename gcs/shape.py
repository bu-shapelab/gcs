from __future__ import annotations

from functools import cached_property
import json

import numpy as np

from .geometry.meshing import generate_vertices, generate_faces
from .verify.verify import verify
from .verify.verify_base_perimeter import verify_base_perimeter
from .verify.verify_radius import verify_radius


class GCS:
    """Generalized cylindrical shell (GCS) class.

    """

    def __init__(self,
                 c4_base: float,
                 c8_base: float,
                 c4_top: float,
                 c8_top: float,
                 twist_linear: float,
                 twist_amplitude: float,
                 twist_cycles: float,
                 perimeter_ratio: float,
                 height: float,
                 mass: float,
                 thickness: float,
                 n_height_steps: int = 100,
                 theta_step: float = 0.01,
                 density: float = 0.0012,
                 triangulate_caps: bool = True) -> None:
        """Initialize ``GCS``.

        Parameters
        ----------
        c4_base : float
            Parameter controlling the size and shape of the base 4-lobe feature.
        c8_base : float
            Parameter controlling the size and shape of the base 8-lobe feature.
        c4_top : float
            Parameter controlling the size and shape of the top 4-lobe feature.
        c8_top : float
            Parameter controlling the size and shape of the top 8-lobe feature.
        twist_linear : float
            Rotation (rad) of the top. This creates a linear twist between the base and top.
        twist_amplitude : float
            Amplitude (rad) of the oscillating twist between the base and top.
        twist_cycles : float
            Number of cycles of the oscillating twist between the base and top.
        perimeter_ratio : float
            Ratio between the top and base perimeters.
        height : float
            Height (mm).
        mass : float
            Mass (g).
        thickness : float
            Wall thickness (mm).
        n_height_steps : int (default=`100`)
            Number of sampled cross-sections along the height.
        theta_step : float (default=`0.01`)
            Angular step size used to sample each cross-section in radians.
        density : float (default=`0.0012`)
            Material density (g/mm^3).
        triangulate_caps : bool (default=`True`)
            Set to `True` to triangulate the top and bottom faces.

        Raises
        ------
        ValueError
            If ``n_height_steps`` is less than 2.
            If ``theta_step`` is not in the range (0,2π/3].
            If ``density`` is not positive.

        Examples
        --------
        >>> shape = gcs.GCS(c4_base=0.3, c8_base=-0.2, c4_top=0.4, c8_top=-0.1, twist_linear=1.2, twist_amplitude=0.1, twist_cycles=2.0, perimeter_ratio=1.3, height=25, mass=2, thickness=0.5)

        """
        if n_height_steps < 2:
            raise ValueError(f'n_height_steps ({n_height_steps}) must be at least 2.')
        if theta_step <= 0 or theta_step > 2 * np.pi / 3:
            raise ValueError(f'theta_step ({theta_step}) must be in range (0, 2π/3].')
        if density <= 0:
            raise ValueError(f'density ({density}) must be positive.')

        self.c4_base_ = c4_base
        self.c8_base_ = c8_base
        self.c4_top_ = c4_top
        self.c8_top_ = c8_top
        self.twist_linear_ = twist_linear
        self.twist_amplitude_ = twist_amplitude
        self.twist_cycles_ = twist_cycles
        self.perimeter_ratio_ = perimeter_ratio
        self.height_ = height
        self.mass_ = mass
        self.thickness_ = thickness
        self.n_height_steps_ = n_height_steps
        self.theta_step_ = theta_step
        self.density_ = density
        self.triangulate_caps_ = triangulate_caps

    @property
    def parameters(self) -> dict:
        """GCS parameters.

        """
        return {
            'c4_base': self.c4_base_,
            'c8_base': self.c8_base_,
            'c4_top': self.c4_top_,
            'c8_top': self.c8_top_,
            'twist_linear': self.twist_linear_,
            'twist_amplitude': self.twist_amplitude_,
            'twist_cycles': self.twist_cycles_,
            'perimeter_ratio': self.perimeter_ratio_,
            'height': self.height_,
            'mass': self.mass_,
            'thickness': self.thickness_,
            'n_height_steps': self.n_height_steps_,
            'theta_step': self.theta_step_,
            'density': self.density_,
            'triangulate_caps': self.triangulate_caps_,
        }

    @property
    def valid_base_perimeter(self) -> bool:
        """Checks whether the GCS has a sufficiently large base perimeter.

        Refer to ``gcs.verify.verify_base_perimeter`` for full documentation.

        """
        return verify_base_perimeter(shape=self)

    @property
    def valid_radius(self) -> bool:
        """Checks whether the minimum radius stays above a printable threshold.

        Refer to ``gcs.verify.verify_radius`` for full documentation.

        """
        return verify_radius(shape=self)

    @property
    def valid(self) -> bool:
        """Runs all verification checks for the GCS.

        Refer to ``gcs.verify.verify`` for full documentation.

        """
        return verify(shape=self)

    @property
    def base_perimeter(self) -> float:
        """Base perimeter (mm).

        """
        numerator = 2 * self.mass_
        denominator = self.density_ * self.height_ * self.thickness_ * (1 + self.perimeter_ratio_)

        return numerator / denominator

    @property
    def top_perimeter(self) -> float:
        """Top perimeter (mm).

        """
        numerator = 2 * self.mass_ * self.perimeter_ratio_
        denominator = self.density_ * self.height_ * self.thickness_ * (1 + self.perimeter_ratio_)

        return numerator / denominator

    @cached_property
    def vertices(self) -> np.ndarray:
        """Vertices.

        """
        return generate_vertices(shape=self)

    @cached_property
    def faces(self) -> np.ndarray:
        """Faces.

        """
        return generate_faces(shape=self)

    def __str__(self):
        """Returns a string representation of the GCS parameters.

        """
        return 'GCS parameters: ' + json.dumps(obj=self.parameters, indent=2)

    def __repr__(self) -> str:
        """Returns a developer-friendly representation of the GCS parameters.

        """
        params = ', '.join(f'{key}={value}' for key, value in self.parameters.items())

        return f'{type(self).__name__}({params})'

    def __eq__(self, other: object) -> bool:
        """Checks whether two GCS objects have the same parameters.

        Parameters
        ----------
        other : object
            Object to compare against.

        Returns
        -------
        equal : bool
            `True` if both objects are GCS instances with identical parameters.

        """
        if not isinstance(other, GCS):
            return False

        return self.parameters == other.parameters
