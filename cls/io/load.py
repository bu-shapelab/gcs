from __future__ import annotations

from typing import Union, TYPE_CHECKING, List
import pandas as pd

from cls import CLS

if TYPE_CHECKING:
    from os import PathLike


def load(file: Union[str, bytes, PathLike]) -> List[CLS]:
    """Loads ``CLS`` from a csv file.

    Parameters
    ----------
    file : {str, bytes, PathLike}
        The file.

    Returns
    -------
    shapes : List[cls.CLS]
        The loaded ``CLS``.

    Examples
    --------
    >>> shapes = cls.io.load(file='saved.csv')

    """
    csv = pd.read_csv(filepath_or_buffer=file,
                      sep=',',
                      header=0)

    shapes = []
    for _, row in csv.iterrows():
        parameters = row.to_dict()
        shape = CLS(**parameters)
        shapes.append(shape)

    return shapes
