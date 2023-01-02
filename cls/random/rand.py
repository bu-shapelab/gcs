from __future__ import annotations

from typing import Optional
import random
from cls import CLS
from cls import C1_BASE_RANGE
from cls import C2_BASE_RANGE
from cls import C1_TOP_RANGE
from cls import C2_TOP_RANGE
from cls import TWIST_LINEAR_RANGE
from cls import TWIST_AMPLITUDE_RANGE
from cls import TWIST_PERIOD_RANGE
from cls import PERIMETER_RATIO_RANGE
from cls import THICKNESS_RANGE

# Fixed mass range instead of [0, inf]
MASS_RANGE = [2, 6]

# Fixed height range instead of [0, inf]
HEIGHT_RANGE = [10, 30]


def rand(fixed_parameters: Optional[dict] = None, seed: Optional[int] = None) -> CLS:
    """Creates a valid random CLS.

    Parameters
    ----------
        fixed_parameters : dict, optional
            A dictionary of parameters with fixed-values to override randomization.
            The keys for ``fixed_parameters`` are the arguments to initialize a ``CLS``.
        seed : int, optional
            A random seed.

    Returns
    -------
    shape : cls.CLS
        The random CLS.

    Examples
    --------
    TODO

    """
    if seed is not None:
        random.seed(seed)

    if fixed_parameters is None:
        fixed_parameters = {}

    shape = None

    while True:
        c1_base = random.uniform(a=C1_BASE_RANGE[0], b=C1_BASE_RANGE[1])
        if 'c1_base' in fixed_parameters:
            c1_base = fixed_parameters['c1_base']

        c2_base = random.uniform(a=C2_BASE_RANGE[0], b=C2_BASE_RANGE[1])
        if 'c2_base' in fixed_parameters:
            c2_base = fixed_parameters['c2_base']

        c1_top = random.uniform(a=C1_TOP_RANGE[0], b=C1_TOP_RANGE[1])
        if 'c1_top' in fixed_parameters:
            c1_top = fixed_parameters['c1_top']

        c2_top = random.uniform(a=C2_TOP_RANGE[0], b=C2_TOP_RANGE[1])
        if 'c2_top' in fixed_parameters:
            c2_top = fixed_parameters['c2_top']

        twist_linear = random.uniform(a=TWIST_LINEAR_RANGE[0], b=TWIST_LINEAR_RANGE[1])
        if 'twist_linear' in fixed_parameters:
            twist_linear = fixed_parameters['twist_linear']

        twist_amplitude = random.uniform(a=TWIST_AMPLITUDE_RANGE[0], b=TWIST_AMPLITUDE_RANGE[1])
        if 'twist_amplitude' in fixed_parameters:
            twist_amplitude = fixed_parameters['twist_amplitude']

        twist_period = random.uniform(a=TWIST_PERIOD_RANGE[0], b=TWIST_PERIOD_RANGE[1])
        if 'twist_period' in fixed_parameters:
            twist_period = fixed_parameters['twist_period']

        perimeter_ratio = random.uniform(a=PERIMETER_RATIO_RANGE[0], b=PERIMETER_RATIO_RANGE[1])
        if 'perimeter_ratio' in fixed_parameters:
            perimeter_ratio = fixed_parameters['perimeter_ratio']

        height = random.uniform(a=HEIGHT_RANGE[0], b=HEIGHT_RANGE[1])
        if 'height' in fixed_parameters:
            height = fixed_parameters['height']

        mass = random.uniform(a=MASS_RANGE[0], b=MASS_RANGE[1])
        if 'mass' in fixed_parameters:
            mass = fixed_parameters['mass']

        thickness = random.uniform(a=THICKNESS_RANGE[0], b=THICKNESS_RANGE[1])
        if 'thickness' in fixed_parameters:
            thickness = fixed_parameters['thickness']

        shape = CLS(c1_base=c1_base,
                    c2_base=c2_base,
                    c1_top=c1_top,
                    c2_top=c2_top,
                    twist_linear=twist_linear,
                    twist_amplitude=twist_amplitude,
                    twist_period=twist_period,
                    perimeter_ratio=perimeter_ratio,
                    height=height,
                    mass=mass,
                    thickness=thickness)

        if shape.valid:
            break

    return shape
