from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd

from ..shape import GCS

if TYPE_CHECKING:
    from os import PathLike


def load_parameters(file: str | PathLike[str]) -> list[GCS]:
    """Loads one or more GCS parameters from a CSV file.

    Parameters
    ----------
    file : {str, PathLike[str]}
        Input CSV file path.

    Returns
    -------
    shapes : list[gcs.GCS]
        Loaded GCS shapes.

    Examples
    --------
    >>> shape = gcs.Cylinder(height=25, mass=2, thickness=0.5)
    >>> gcs.io.save_parameters(file='saved.csv', shapes=[shape])
    >>> shapes = gcs.io.load_parameters(file='saved.csv')
    >>> shape == shapes[0]
    True

    Notes
    -----
    The input CSV must contain one row per shape, with columns matching the
    parameter names accepted by ``gcs.GCS``. Files written by
    ``gcs.io.save_parameters`` use the expected format.

    """
    csv_data = pd.read_csv(filepath_or_buffer=file, sep=',', header=0)

    shapes = []
    for _, row in csv_data.iterrows():
        parameters = row.to_dict()
        shape = GCS(**parameters)

        shapes.append(shape)

    return shapes
