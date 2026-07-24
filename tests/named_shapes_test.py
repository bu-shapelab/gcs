from __future__ import annotations

from gcs import GCS, Cylinder, Iroko, Willow


def test_cylinder() -> None:
    """Tests for ``gcs.Cylinder``.

    """
    height = 25
    mass = 2
    thickness = 0.5

    parameters = {
        'c4_base': 0,
        'c8_base': 0,
        'c4_top': 0,
        'c8_top': 0,
        'twist_linear': 0,
        'twist_amplitude': 0,
        'twist_cycles': 0,
        'perimeter_ratio': 1,
        'height': height,
        'mass': mass,
        'thickness': thickness,
    }

    shape1 = GCS(**parameters)
    shape2 = Cylinder(height=height, mass=mass, thickness=thickness)

    assert shape1 == shape2


def test_iroko() -> None:
    """Tests for ``gcs.Iroko``.

    """
    parameters = {
        'c4_base': 0.730333927354502,
        'c8_base': -0.0821084429646878,
        'c4_top': 0.455688084446719,
        'c8_top': -0.200458707161255,
        'twist_linear': 0.11822302314236,
        'twist_amplitude': 0.262031108639582,
        'twist_cycles': 0.591614200392281,
        'perimeter_ratio': 1.17143242893827,
        'height': 20.7821180708855,
        'mass': 2.15501149030671,
        'thickness': 0.578365564080763,
    }

    shape1 = GCS(**parameters)
    shape2 = Iroko()

    assert shape1 == shape2


def test_willow() -> None:
    """Tests for ``gcs.Willow``.

    """
    parameters = {
        'c4_base': 0.137494858826025,
        'c8_base': -0.223924307740836,
        'c4_top': 0.990048662372857,
        'c8_top': 0.281006846858847,
        'twist_linear': 1.65277226755515,
        'twist_amplitude': 0.136307527192256,
        'twist_cycles': 0.892285681537298,
        'perimeter_ratio': 1.53516566101125,
        'height': 26.2960096899026,
        'mass': 2.27727026727678,
        'thickness': 0.771900777794452,
    }

    shape1 = GCS(**parameters)
    shape2 = Willow()

    assert shape1 == shape2

