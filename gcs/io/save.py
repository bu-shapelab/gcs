from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
import pandas as pd
from stl import Mode
from stl.mesh import Mesh

if TYPE_CHECKING:
    from os import PathLike

    from ..shape import GCS


def save_parameters(file: str | PathLike[str], shapes: list[GCS]) -> None:
    """Saves one or more GCS parameters to a CSV file.

    Parameters
    ----------
    file : {str, PathLike[str]}
        Output CSV file path.
    shapes : list[gcs.GCS]
        GCS shapes to save.

    Examples
    --------
    >>> shape = gcs.Cylinder(height=25, mass=2, thickness=0.5)
    >>> gcs.io.save_parameters(file='saved.csv', shapes=[shape])

    >>> shape = gcs.Cylinder(height=25, mass=2, thickness=0.5)
    >>> shape = gcs.Cylinder(height=30, mass=1, thickness=0.5)
    >>> gcs.io.save_parameters(file='saved.csv', shapes=[shape1, shape2])

    """
    parameters = [shape.parameters for shape in shapes]

    csv_data = pd.DataFrame.from_records(data=parameters)
    csv_data.to_csv(path_or_buf=file, header=True, index=False)


def save_mesh(file: str | PathLike[str], shape: GCS) -> None:
    """Saves a GCS mesh to an STL file.

    Parameters
    ----------
    file : {str, PathLike[str]}
        Output STL file path.
    shape : gcs.GCS
        GCS shape to save.

    Examples
    --------
    >>> shape = gcs.Cylinder(height=25, mass=2, thickness=0.5)
    >>> gcs.io.save_mesh(file='saved.stl', shape=shape)

    References
    ----------
    .. [1] https://github.com/wolph/numpy-stl/tree/develop#creating-mesh-objects-from-a-list-of-vertices-and-faces

    """
    vertices = shape.vertices
    faces = shape.faces

    mesh = Mesh(data=np.zeros(shape=(faces.shape[0],), dtype=Mesh.dtype))

    for i, face in enumerate(faces):
        for dim in range(3):
            mesh.vectors[i][dim] = vertices[face[dim], :]

    mesh.save(filename=file, mode=Mode.BINARY)
