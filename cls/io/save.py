from __future__ import annotations

from typing import Union, TYPE_CHECKING, List
import pandas as pd

if TYPE_CHECKING:
    from os import PathLike
    from cls import CLS


def save(shapes: List[CLS],
         file: Union[str, bytes, PathLike]) -> None:
    """Saves ``cls.CLS`` parameters to a csv file.

    Parameters
    ----------
    shapes : list[cls.CLS]
        The CLS.
    file : {str, bytes, PathLike}
        The csv file.

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
    parameters = [shape.parameters for shape in shapes]
    csv = pd.DataFrame.from_records(parameters)
    csv.to_csv(path_or_buf=file, header=True, index=False)

def save_mesh(shape: CLS, file: Union[str, bytes, PathLike]) -> None:
    """Saves ``cls.CLS`` mesh to an stl file.

    Parameters
    ----------
    shape : cls.CLS
        The CLS.
    file : {str, bytes, PathLike}
        The stl file.

    Examples
    --------
    >>> shape = cls.CLS()
    >>> file = 'saved_mesh.stl'
    >>> cls.save_mesh(shape=shape, file=file)

    """
    shape.mesh.save(filename=file)
