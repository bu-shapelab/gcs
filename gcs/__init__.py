"""
Generalized Cylindrical Shells
==============================

Python library for generating 3D meshes of generalized cylindrical shells.

How to use the documentation
----------------------------
Documentation is available in docstrings provided with the code.

The docstring examples assume that `gcs` has been imported::

    >>> import gcs

Code snippets are indicated by three greater-than signs::

    >>> shape = gcs.GCS(...)TODO
    >>> shape.parameters

Available subpackages
---------------------
geometry
    Functions for geometry generation and analysis.
io
    Functions for loading/saving GCS shapes.
verify
    Functions for verifying the validity of GCS shapes.

"""
from .named_shapes import Cylinder
from .named_shapes import Iroko
from .named_shapes import Willow
from .shape import GCS

from . import geometry
from . import io
from . import verify

submodules = [
    'geometry',
    'io',
    'verify',
]

__all__ = submodules + [
    'GCS',
    'Cylinder',
    'Iroko',
    'Willow',
]
