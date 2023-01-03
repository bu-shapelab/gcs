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
preview
    Functions for previewing CLS shapes.
verify
    Functions for verifying the validity of CLS shapes.
random
    Functions for generating random CLS shapes.

"""
from .cls import *

from .utils.discretization import discretize
from .utils.load import load
from .utils.save import save
from .utils.save import save_mesh
from .utils.triangulation import triangulate

from . import preview
from . import random
from . import verify
