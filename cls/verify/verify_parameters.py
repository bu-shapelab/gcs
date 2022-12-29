from __future__ import annotations

from typing import TYPE_CHECKING
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

if TYPE_CHECKING:
    from cls import CLS


def verify_parameters(shape: CLS, verbose: bool = False) -> bool:
    """TODO
    """
    parameters = shape.parameters
    valid = True
    if parameters['c1_base'] < C1_BASE_RANGE[0] or parameters['c1_base'] > C1_BASE_RANGE[1]:
        if verbose:
            print('TODO')
        valid = False
    elif parameters['c2_base'] < C2_BASE_RANGE[0] or parameters['c2_base'] > C2_BASE_RANGE[1]:
        if verbose:
            print('TODO')
        valid = False
    elif parameters['c1_top'] < C1_TOP_RANGE[0] or parameters['c1_top'] > C1_TOP_RANGE[1]:
        if verbose:
            print('TODO')
        valid = False
    elif parameters['c2_top'] < C2_TOP_RANGE[0] or parameters['c2_top'] > C2_TOP_RANGE[1]:
        if verbose:
            print('TODO')
        valid = False
    elif parameters['twist_linear'] < TWIST_LINEAR_RANGE[0] or parameters['twist_linear'] > TWIST_LINEAR_RANGE[1]:
        if verbose:
            print('TODO')
        valid = False
    elif parameters['twist_amplitude'] < TWIST_AMPLITUDE_RANGE[0] or parameters['twist_amplitude'] > TWIST_AMPLITUDE_RANGE[1]:
        if verbose:
            print('TODO')
        valid = False
    elif parameters['twist_period'] < TWIST_PERIOD_RANGE[0] or parameters['twist_period'] > TWIST_PERIOD_RANGE[1]:
        if verbose:
            print('TODO')
        valid = False
    elif parameters['height'] < HEIGHT_RANGE[0] or parameters['height'] > HEIGHT_RANGE[1]:
        if verbose:
            print('TODO')
        valid = False
    elif parameters['mass'] < MASS_RANGE[0] or parameters['mass'] > MASS_RANGE[1]:
        if verbose:
            print('TODO')
        valid = False
    elif parameters['perimeter_ratio'] < PERIMETER_RATIO_RANGE[0] or parameters['perimeter_ratio'] > PERIMETER_RATIO_RANGE[1]:
        if verbose:
            print('TODO')
        valid = False
    elif parameters['thickness'] < THICKNESS_RANGE[0] or parameters['thickness'] > THICKNESS_RANGE[1]:
        if verbose:
            print('TODO')
        valid = False

    return valid

