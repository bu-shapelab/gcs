from __future__ import annotations

from cls import C1_BASE_RANGE
from cls import C2_BASE_RANGE
from cls import C1_TOP_RANGE
from cls import C2_TOP_RANGE
from cls import TWIST_LINEAR_RANGE
from cls import TWIST_AMPLITUDE_RANGE
from cls import TWIST_PERIOD_RANGE
from cls import MIN_HEIGHT
from cls import MIN_MASS
from cls import PERIMETER_RATIO_RANGE
from cls import THICKNESS_RANGE
from cls import CLS

def verify_parameters(shape: CLS, verbose: bool = False) -> bool:
    """Verifies the validity of the parameters of a CLS.

    The validity check is to minimize the risk of printing failures.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    verbose : bool, (default=False)
        Set to `True` to print validity messages.

    Returns
    -------
    valid : bool
        `True` if ``shape`` has valid parameters, `False` otherwise.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> valid = cls.verify_parameters(shape=shape)

    """
    parameters = shape.parameters
    valid = True
    if parameters['c1_base'] < C1_BASE_RANGE[0] or parameters['c1_base'] > C1_BASE_RANGE[1]:
        if verbose:
            print(f'c1_base ({parameters["c1_base"]}) is outside range {C1_BASE_RANGE}.')
        valid = False
    elif parameters['c2_base'] < C2_BASE_RANGE[0] or parameters['c2_base'] > C2_BASE_RANGE[1]:
        if verbose:
            print(f'c2_base ({parameters["c2_base"]}) is outside range {C2_BASE_RANGE}.')
        valid = False
    elif parameters['c1_top'] < C1_TOP_RANGE[0] or parameters['c1_top'] > C1_TOP_RANGE[1]:
        if verbose:
            print(f'c1_top ({parameters["c1_top"]}) is outside range {C1_TOP_RANGE}.')
        valid = False
    elif parameters['c2_top'] < C2_TOP_RANGE[0] or parameters['c2_top'] > C2_TOP_RANGE[1]:
        if verbose:
            print(f'c2_top ({parameters["c2_top"]}) is outside range {C2_TOP_RANGE}.')
        valid = False
    elif parameters['twist_linear'] < TWIST_LINEAR_RANGE[0] or parameters['twist_linear'] > TWIST_LINEAR_RANGE[1]:
        if verbose:
            print(f'twist_linear ({parameters["twist_linear"]}) is outside range {TWIST_LINEAR_RANGE}.')
        valid = False
    elif parameters['twist_amplitude'] < TWIST_AMPLITUDE_RANGE[0] or parameters['twist_amplitude'] > TWIST_AMPLITUDE_RANGE[1]:
        if verbose:
            print(f'twist_amplitude ({parameters["twist_amplitude"]}) is outside range {TWIST_AMPLITUDE_RANGE}.')
        valid = False
    elif parameters['twist_period'] < TWIST_PERIOD_RANGE[0] or parameters['twist_period'] > TWIST_PERIOD_RANGE[1]:
        if verbose:
            print(f'twist_period ({parameters["twist_period"]}) is outside range {TWIST_PERIOD_RANGE}.')
        valid = False
    elif parameters['height'] < MIN_HEIGHT:
        if verbose:
            print(f'height ({parameters["height"]}) is less then minimum {MIN_HEIGHT}.')
        valid = False
    elif parameters['mass'] < MIN_MASS:
        if verbose:
            print(f'mass ({parameters["mass"]}) is less then minimum {MIN_MASS}.')
        valid = False
    elif parameters['perimeter_ratio'] < PERIMETER_RATIO_RANGE[0] or parameters['perimeter_ratio'] > PERIMETER_RATIO_RANGE[1]:
        if verbose:
            print(f'perimeter_ratio ({parameters["perimeter_ratio"]}) is outside range {PERIMETER_RATIO_RANGE}.')
        valid = False
    elif parameters['thickness'] < THICKNESS_RANGE[0] or parameters['thickness'] > THICKNESS_RANGE[1]:
        if verbose:
            print(f'thickness ({parameters["thickness"]}) is outside range {THICKNESS_RANGE}.')
        valid = False

    return valid
