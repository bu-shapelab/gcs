"""
CLS
===

Provides
  1. An object representing a continuous line structure.
  2. Operations on CLS structures.

How to use the documentation
----------------------------
Documentation is available in docstrings provided with the code.

The docstring examples assume that `cls` has been imported::

  >>> import cls

Code snippets are indicated by three greater-than signs::

  >>> shape = cls.CLS()
  >>> shape.parameters

Available subpackages
---------------------
io
    Functions for loading/saving CLS shapes.
verify
    Functions for verifying the validity of CLS shapes.
random
    Functions for generating random CLS shapes.

"""
from .shape import C1_BASE_RANGE
from .shape import C2_BASE_RANGE
from .shape import C1_TOP_RANGE
from .shape import C2_TOP_RANGE
from .shape import TWIST_LINEAR_RANGE
from .shape import TWIST_AMPLITUDE_RANGE
from .shape import TWIST_PERIOD_RANGE
from .shape import HEIGHT_RANGE
from .shape import MASS_RANGE
from .shape import PERIMETER_RATIO_RANGE
from .shape import THICKNESS_RANGE
from .shape import CLS

from .discretization import discretize
from .triangulation import triangulate

from . import io
from . import random
from . import verify

submodules = [
    'io',
    'random',
    'verify',
]

__all__ = submodules + [
    'C1_BASE_RANGE',
    'C2_BASE_RANGE',
    'C1_TOP_RANGE',
    'C2_TOP_RANGE',
    'TWIST_LINEAR_RANGE',
    'TWIST_AMPLITUDE_RANGE',
    'TWIST_PERIOD_RANGE',
    'HEIGHT_RANGE',
    'MASS_RANGE',
    'PERIMETER_RATIO_RANGE',
    'THICKNESS_RANGE',
    'CLS',
    'discretize',
    'triangulate',
]
