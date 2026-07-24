from __future__ import annotations

from pathlib import Path

from gcs import Cylinder
from gcs.io import load_parameters, save_parameters


def test_load_parameters() -> None:
    """Tests for ``gcs.io.load_parameters``.

    """
    file_dir = Path(__file__).resolve().parent
    single_file = file_dir / 'single.csv'
    multiple_file = file_dir / 'multiple.csv'

    try:
        # Single shape
        shape = Cylinder(height=25, mass=2, thickness=0.5)

        save_parameters(file=single_file, shapes=[shape])
        shapes = load_parameters(file=single_file)

        assert len(shapes) == 1
        assert shapes[0] == shape

        # Multiple shapes
        shape1 = Cylinder(height=25, mass=2, thickness=0.5)
        shape2 = Cylinder(height=30, mass=1, thickness=0.5)

        save_parameters(file=multiple_file, shapes=[shape1, shape2])
        shapes = load_parameters(file=multiple_file)

        assert len(shapes) == 2
        assert shapes[0] == shape1
        assert shapes[1] == shape2

    finally:
        if single_file.exists():
            single_file.unlink()
        if multiple_file.exists():
            multiple_file.unlink()
