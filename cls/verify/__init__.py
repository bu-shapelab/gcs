"""
``cls.verify``
================

Functions present in ``cls.verify`` are listed below.


Verifying CLS
-------------

   verify_base_perimeter
   verify_parameters
   verify_radius

"""
from .verify_base_perimeter import verify_base_perimeter
from .verify_parameters import verify_parameters
from .verify_radius import verify_radius

__all__ = [
    'verify_base_perimeter',
    'verify_parameters',
    'verify_radius',
]
