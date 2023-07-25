from __future__ import annotations

from typing import Union, TYPE_CHECKING, List
import pandas as pd

if TYPE_CHECKING:
    from os import PathLike
    import gcs


def save(file: Union[str, bytes, PathLike],
         shapes: List[gcs.GCS]) -> None:
    """Saves GCS to a csv file.

    Parameters
    ----------
    file : {str, bytes, PathLike}
        The file.
    shapes : List[gcs.GCS]
        The GCS.

    Examples
    --------
    >>> shape = gcs.GCS(...)
    >>> gcs.io.save(file='saved.csv', shapes=[shape])

    >>> shape1 = gcs.GCS(...)
    >>> shape2 = gcs.GCS(...)
    >>> gcs.io.save(file='saved.csv', shapes=[shape1, shape2])

    """
    parameters = [shape.parameters for shape in shapes]
    csv = pd.DataFrame.from_records(parameters)
    csv.to_csv(path_or_buf=file,
               header=True,
               index=False)


def save_mesh(file: Union[str, bytes, PathLike],
              shape: gcs.GCS) -> None:
    """Saves GCS mesh to an stl file.

    Parameters
    ----------
    file : {str, bytes, PathLike}
        The file.
    shape : gcs.GCS
        The GCS.

    Examples
    --------
    >>> shape = gcs.GCS(...)
    >>> gcs.io.save_mesh(file='saved.stl', shape=shape)

    """
    shape.mesh.save(filename=file)
