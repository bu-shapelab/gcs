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

"""

from .shape import CLS

from .discretization import discretize
from .triangulation import triangulate

from . import io
from . import verify

submodules = [
    'io',
    'verify',
]

__all__ = submodules + [
    'CLS',
    'discretize',
    'triangulate',
]
