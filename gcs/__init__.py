"""
Generalized Cylindrical Shells
==============================

Provides
    1. An object representing generalized cylindrical shell (GCS) structures.
    2. Operations on GCS structures.

How to use the documentation
----------------------------
Documentation is available in docstrings provided with the code.

The docstring examples assume that `gcs` has been imported::

    >>> import gcs

Code snippets are indicated by three greater-than signs::

    >>> shape = gcs.GCS(...)
    >>> shape.parameters

Available subpackages
---------------------
io
    Functions for loading/saving GCS shapes.
verify
    Functions for verifying the validity of GCS shapes.

"""
from .shape import GCS, Cylinder

from .discretization import discretize
from .triangulation import triangulate

from . import io
from . import verify

submodules = [
    'io',
    'verify',
]

__all__ = submodules + [
    'GCS',
    'Cylinder',
    'discretize',
    'triangulate',
]
