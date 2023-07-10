from __future__ import annotations

from typing import Union, TYPE_CHECKING, List
import pandas as pd

if TYPE_CHECKING:
    from os import PathLike
    from cls import CLS


def save(file: Union[str, bytes, PathLike],
         shapes: List[CLS]) -> None:
    """Saves ``CLS`` to a csv file.

    Parameters
    ----------
    file : {str, bytes, PathLike}
        The file.
    shapes : List[cls.CLS]
        The CLS.

    """
    parameters = [shape.parameters for shape in shapes]
    csv = pd.DataFrame.from_records(parameters)
    csv.to_csv(path_or_buf=file,
               header=True,
               index=False)


def save_mesh(file: Union[str, bytes, PathLike],
              shape: CLS) -> None:
    """Saves ``CLS`` mesh to an stl file.

    Parameters
    ----------
    file : {str, bytes, PathLike}
        The file.
    shape : cls.CLS
        The CLS.

    """
    shape.mesh.save(filename=file)
