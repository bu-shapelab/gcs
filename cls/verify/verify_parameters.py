from __future__ import annotations

from cls import C1_BASE_RANGE
from cls import C2_BASE_RANGE
from cls import C1_TOP_RANGE
from cls import C2_TOP_RANGE
from cls import TWIST_LINEAR_RANGE
from cls import TWIST_AMPLITUDE_RANGE
from cls import TWIST_PERIOD_RANGE
from cls import HEIGHT_RANGE
from cls import MASS_RANGE
from cls import PERIMETER_RATIO_RANGE
from cls import THICKNESS_RANGE
from cls import CLS


def verify_parameters(shape: CLS, verbose: bool = False) -> bool:
    """Checks if the ``cls.CLS`` parameters are valid.

    This check reduces the risk of print defects by ensuring ``cls.CLS``
    have valid parameters.

    Parameters
    ----------
    shape : CLS.cls
        The CLS.
    verbose : bool, (default=`False`)
        Set to `True` to receive verify messages.

    Returns
    -------
    valid : bool
        `True` if ``shape`` has valid parameters.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> valid = cls.verify_parameters(shape=shape)

    """
    parameters = shape.parameters
    valid = True
    if not C1_BASE_RANGE[0] <= parameters['c1_base'] <= C1_BASE_RANGE[1]:
        if verbose:
            print(f'c1_base ({parameters["c1_base"]}) ',
                  f'is outside range {C1_BASE_RANGE}.')
        valid = False
    elif not C2_BASE_RANGE[0] <= parameters['c2_base'] <= C2_BASE_RANGE[1]:
        if verbose:
            print(f'c2_base ({parameters["c2_base"]}) ',
                  f'is outside range {C2_BASE_RANGE}.')
        valid = False
    elif not C1_TOP_RANGE[0] <= parameters['c1_top'] <= C1_TOP_RANGE[1]:
        if verbose:
            print(f'c1_top ({parameters["c1_top"]}) ',
                  f'is outside range {C1_TOP_RANGE}.')
        valid = False
    elif not C2_TOP_RANGE[0] <= parameters['c2_top'] <= C2_TOP_RANGE[1]:
        if verbose:
            print(f'c2_top ({parameters["c2_top"]}) ',
                  f'is outside range {C2_TOP_RANGE}.')
        valid = False
    elif not TWIST_LINEAR_RANGE[0] <= parameters['twist_linear'] <= TWIST_LINEAR_RANGE[1]:
        if verbose:
            print(f'twist_linear ({parameters["twist_linear"]}) ',
                  f'is outside range {TWIST_LINEAR_RANGE}.')
        valid = False
    elif not TWIST_AMPLITUDE_RANGE[0] <= parameters['twist_amplitude'] <= TWIST_AMPLITUDE_RANGE[1]:
        if verbose:
            print(f'twist_amplitude ({parameters["twist_amplitude"]}) ',
                  f'is outside range {TWIST_AMPLITUDE_RANGE}.')
        valid = False
    elif not TWIST_PERIOD_RANGE[0] <= parameters['twist_period'] <= TWIST_PERIOD_RANGE[1]:
        if verbose:
            print(f'twist_period ({parameters["twist_period"]}) ',
                  f'is outside range {TWIST_PERIOD_RANGE}.')
        valid = False
    elif not HEIGHT_RANGE[0] <= parameters['height'] <= HEIGHT_RANGE[1]:
        if verbose:
            print(f'height ({parameters["height"]}) ',
                  f'is outside range {HEIGHT_RANGE}.')
        valid = False
    elif not MASS_RANGE[0] <= parameters['mass'] <= MASS_RANGE[1]:
        if verbose:
            print(f'mass ({parameters["mass"]}) ',
                  f'is outside range {MASS_RANGE}.')
        valid = False
    elif not PERIMETER_RATIO_RANGE[0] <= parameters['perimeter_ratio'] <= PERIMETER_RATIO_RANGE[1]:
        if verbose:
            print(f'perimeter_ratio ({parameters["perimeter_ratio"]}) ',
                  f'is outside range {PERIMETER_RATIO_RANGE}.')
        valid = False
    elif not THICKNESS_RANGE[0] <= parameters['thickness'] <= THICKNESS_RANGE[1]:
        if verbose:
            print(f'thickness ({parameters["thickness"]}) ',
                  f'is outside range {THICKNESS_RANGE}.')
        valid = False

    return valid
