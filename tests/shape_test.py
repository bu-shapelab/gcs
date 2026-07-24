from __future__ import annotations

import numpy as np
from pytest import approx, raises

from gcs import GCS
from gcs.geometry import generate_vertices, generate_faces
from gcs.verify import verify, verify_base_perimeter, verify_radius
from tests.constants import ATOL


def test_gcs() -> None:
    """Tests for ``gcs.GCS``.

    """
    # Willow
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
        'n_height_steps': 100,
        'theta_step': 0.01,
        'density': 0.0012,
        'triangulate_caps': False,
    }
    shape = GCS(**parameters)

    # Properties
    assert shape.parameters == parameters
    assert shape.valid_base_perimeter == verify_base_perimeter(shape=shape)
    assert shape.valid_radius == verify_radius(shape=shape)
    assert shape.valid == verify(shape=shape)
    assert shape.base_perimeter == approx(expected=73.75740901233866, abs=ATOL)
    assert shape.top_perimeter == approx(expected=113.22984156090399, abs=ATOL)
    np.testing.assert_allclose(actual=shape.vertices,
                               desired=generate_vertices(shape=shape),
                               atol=ATOL)
    np.testing.assert_equal(actual=shape.faces, desired=generate_faces(shape=shape))

    # Equality
    same_shape = GCS(**shape.parameters)
    different_shape = GCS(**(shape.parameters | {'height': 30}))

    assert shape == same_shape
    assert shape != different_shape
    assert shape != 'wrong type'

    # Invalid number of height steps
    invalid_parameters = parameters | {'n_height_steps': 1}
    with raises(expected_exception=ValueError):
        GCS(**invalid_parameters)

    # Invalid theta step
    invalid_parameters = parameters | {'theta_step': 0.0}
    with raises(expected_exception=ValueError):
        GCS(**invalid_parameters)

    invalid_parameters = parameters | {'theta_step': 2 * np.pi / 3 + 0.1}
    with raises(expected_exception=ValueError):
        GCS(**invalid_parameters)

    # Invalid density
    invalid_parameters = parameters | {'density': 0.0}
    with raises(expected_exception=ValueError):
        GCS(**invalid_parameters)
