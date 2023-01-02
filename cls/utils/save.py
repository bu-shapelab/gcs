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
    TODO

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
    TODO

    """
    # TODO: Does this ever raise error? 
    shape.mesh.save(filename=file)
