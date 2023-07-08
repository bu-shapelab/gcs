"""
``cls.verify``
================

Functions present in ``cls.verify`` are listed below.


Verifying CLS
-------------

   verify
   verify_base_perimeter
   verify_radius

"""
from .verify_base_perimeter import verify_base_perimeter
from .verify_radius import verify_radius
from .verify import verify

__all__ = [
    'verify_base_perimeter',
    'verify_radius',
    'verify',
]
