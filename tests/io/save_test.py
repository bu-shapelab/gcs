from __future__ import annotations

from pathlib import Path

import pandas as pd

from gcs import Cylinder
from gcs.io import save_mesh, save_parameters


def test_save_parameters() -> None:
    """Tests for ``gcs.io.save_parameters``.

    """
    file_dir = Path(__file__).resolve().parent
    single_file = file_dir / 'single.csv'
    multiple_file = file_dir / 'multiple.csv'

    try:
        # Single shape
        shape = Cylinder(height=25, mass=2, thickness=0.5)

        save_parameters(file=single_file, shapes=[shape])

        assert single_file.exists()

        csv_data = pd.read_csv(filepath_or_buffer=single_file, delimiter=',', header=0)

        assert len(csv_data) == 1

        expected_parameters = csv_data.to_dict(orient='records')[0]

        assert expected_parameters == shape.parameters

        # Multiple shapes
        shape1 = Cylinder(height=25, mass=2, thickness=0.5)
        shape2 = Cylinder(height=30, mass=1, thickness=0.5)

        save_parameters(file=multiple_file, shapes=[shape1, shape2])

        assert multiple_file.exists()

        csv_data = pd.read_csv(filepath_or_buffer=multiple_file, delimiter=',', header=0)

        assert len(csv_data) == 2

        expected_parameters1 = csv_data.to_dict(orient='records')[0]
        expected_parameters2 = csv_data.to_dict(orient='records')[1]

        assert expected_parameters1 == shape1.parameters
        assert expected_parameters2 == shape2.parameters

    finally:
        if single_file.exists():
            single_file.unlink()
        if multiple_file.exists():
            multiple_file.unlink()


def test_save_mesh() -> None:
    """Tests for ``gcs.io.save_mesh``.

    """
    file = Path(__file__).resolve().parent / 'shape.stl'

    try:
        shape = Cylinder(height=25, mass=2, thickness=0.5)

        save_mesh(file=file, shape=shape)

        assert file.exists()
        assert file.stat().st_size > 0

    finally:
        if file.exists():
            file.unlink()
