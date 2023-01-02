from __future__ import annotations

from typing import Union, TYPE_CHECKING
import pandas as pd

from ..cls import CLS

if TYPE_CHECKING:
    from os import PathLike


def save(shapes: list[CLS], file: Union[str, bytes, PathLike]) -> None:
    """Saves CLS to a CSV file.

    Parameters
    ----------
    shapes : list[cls.CLS]
        The CLS.
    file : {str, bytes, PathLike}
        The path to the CSV file.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> file = 'saved_shapes.csv'
    >>> cls.save(shapes=[shape], file=file)

    >>> shape1 = cls.CLS()
    >>> shape2 = cls.CLS()
    >>> shapes = [shape1, shape2]
    >>> file = 'saved_shapes.csv'
    >>> cls.save(shapes=shapes, file=file)

    """
    csv = pd.DataFrame()

    parameters = [shape.parameters for shape in shapes]

    csv = pd.concat([csv, pd.DataFrame.from_records(parameters)],
                    ignore_index=True)

    csv.to_csv(path_or_buf=file, header=True, index=False)


def save_mesh(shape: CLS, file: Union[str, bytes, PathLike]) -> None:
    """Saves CLS mesh to a STL file.

    Parameters
    ----------
    shape : cls.CLS
        The CLS.
    file : {str, bytes, PathLike}
        The path to the STL file.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> file = 'saved_mesh.stl'
    >>> cls.save_mesh(shape=shape, file=file)

    """
    # TODO: Does this ever raise error?
    shape.mesh.save(filename=file)
