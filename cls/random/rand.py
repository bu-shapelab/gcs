from __future__ import annotations

from typing import Optional
import random
from cls import C1_BASE_RANGE
from cls import C2_BASE_RANGE
from cls import C1_TOP_RANGE
from cls import C2_TOP_RANGE
from cls import TWIST_LINEAR_RANGE
from cls import TWIST_AMPLITUDE_RANGE
from cls import TWIST_PERIOD_RANGE
from cls import PERIMETER_RATIO_RANGE
from cls import THICKNESS_RANGE
from cls import MASS_RANGE
from cls import HEIGHT_RANGE
from cls import CLS


def rand(seed: Optional[int] = None,
         fixed_kwargs: Optional[dict] = None) -> CLS:
    """Creates a random (valid) CLS.

    Parameters
    ----------
    seed : int, optional
        A random seed.
    fixed_kwargs : dict, optional
        The kwargs of fixed parameters for ``cls.CLS`` initalization.

    Returns
    -------
    shape : cls.CLS
        The random CLS.

    Examples
    --------
    >>> shape = cls.random.rand()

    >>> fixed_kwargs = { 'c1_base': 0.5, 'height': 20 }
    >>> shape = cls.random.rand(fixed_kwargs=fixed_kwargs)

    """
    if seed is not None:
        random.seed(seed)

    shape = None

    while True:
        kwargs = {}
        if fixed_kwargs is not None:
            kwargs = fixed_kwargs.copy()

        if 'c1_base' not in kwargs:
            kwargs['c1_base'] = random.uniform(a=C1_BASE_RANGE[0],
                                               b=C1_BASE_RANGE[1])

        if 'c2_base' not in kwargs:
            kwargs['c2_base'] = random.uniform(a=C2_BASE_RANGE[0],
                                               b=C2_BASE_RANGE[1])

        if 'c1_top' not in kwargs:
            kwargs['c1_top'] = random.uniform(a=C1_TOP_RANGE[0],
                                              b=C1_TOP_RANGE[1])

        if 'c2_top' not in kwargs:
            kwargs['c2_top'] = random.uniform(a=C2_TOP_RANGE[0],
                                              b=C2_TOP_RANGE[1])

        if 'twist_linear' not in kwargs:
            kwargs['twist_linear'] = random.uniform(a=TWIST_LINEAR_RANGE[0],
                                                    b=TWIST_LINEAR_RANGE[1])

        if 'twist_amplitude' not in kwargs:
            kwargs['twist_amplitude'] = random.uniform(a=TWIST_AMPLITUDE_RANGE[0],
                                                       b=TWIST_AMPLITUDE_RANGE[1])

        if 'twist_period' not in kwargs:
            kwargs['twist_period'] = random.uniform(a=TWIST_PERIOD_RANGE[0],
                                                    b=TWIST_PERIOD_RANGE[1])

        if 'perimeter_ratio' not in kwargs:
            kwargs['perimeter_ratio'] = random.uniform(a=PERIMETER_RATIO_RANGE[0],
                                                       b=PERIMETER_RATIO_RANGE[1])

        if 'height' not in kwargs:
            kwargs['height'] = random.uniform(a=HEIGHT_RANGE[0],
                                              b=HEIGHT_RANGE[1])

        if 'mass' not in kwargs:
            kwargs['mass'] = random.uniform(a=MASS_RANGE[0],
                                            b=MASS_RANGE[1])

        if 'thickness' not in kwargs:
            kwargs['thickness'] = random.uniform(a=THICKNESS_RANGE[0],
                                                 b=THICKNESS_RANGE[1])

        shape = CLS(**kwargs)

        if shape.valid:
            break

    return shape
