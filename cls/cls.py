from __future__ import annotations

import numpy as np

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
    """TODO
    """

    def __init__(self, c1_base: float = 0, c2_base: float = 0, c1_top: float = 0,
                 c2_top: float = 0, twist_linear: float = 0, twist_amplitude: float = 0,
                 twist_period: float = 0, perimeter_ratio: float = 1, height: float = 19,
                 mass: float = 2.1, thickness: float = 0.75) -> None:
        """TODO
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

    @property
    def base_perimeter(self):
        """TODO
        """
        return (2 * self._mass) / (self._density * self._height * self._thickness * (1 + self._perimeter_ratio))

    @property
    def top_perimeter(self):
        """TODO
        """
        return (2 * self._mass * self._perimeter_ratio) / (self._density * self._height * self._thickness * (1 + self._perimeter_ratio))

    def __str__(self):
        output = (
            super().__str__()
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
            + f'\n\tdensity: {self._density}g/mm^3'
            + f'\n\tthickness: {self._thickness}mm'
        )

        return output