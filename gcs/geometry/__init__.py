"""
``gcs.geometry``
================

Functions present in ``gcs.geometry`` are listed below.

Coordinate conversion
---------------------

   pol2cart

   cart2pol

Parameterized Curves
--------------------

    summed_cosine

Polar curves
------------

    arc_length

    optimal_scaling_factor

Meshing
-------

    generate_vertices

    generate_faces

"""
from .coordinates import cart2pol, pol2cart
from .meshing import generate_faces, generate_vertices
from .polar_curves import arc_length, optimal_scaling_factor
from .summed_cosine import summed_cosine

__all__ = [
    'arc_length',
    'cart2pol',
    'generate_faces',
    'generate_vertices',
    'optimal_scaling_factor',
    'pol2cart',
    'summed_cosine',
]
