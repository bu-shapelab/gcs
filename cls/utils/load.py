from __future__ import annotations

from typing import Union, TYPE_CHECKING
import pandas as pd

from cls import CLS

if TYPE_CHECKING:
    from os import PathLike


def load(file: Union[str, bytes, PathLike], verbose: bool = False) -> list[CLS]:
    """Load CLS from a CSV file.

    Parameters
    ----------
    file : {str, bytes, PathLike}
        The path to the CSV file.
    verbose : bool, (default=False)
        Set to `True` to print loading messages.

    Returns
    -------
    shapes : list[cls.CLS]
        The loaded CLS.

    Examples
    --------
    >>> file = 'saved_shapes.csv'
    >>> shapes = cls.load(file=file)

    """
    try:
        csv = pd.read_csv(filepath_or_buffer=file, sep=',', header=0)
    except FileNotFoundError:
        if verbose:
            print(f'{file} not found.')
        return []
    except pd.errors.EmptyDataError:
        if verbose:
            print(f'{file} is empty.')
        return []

    shapes = []

    for _, row in csv.iterrows():
        parameters = row.to_dict()

        try:
            shape = CLS(**parameters)
        except TypeError:
            if verbose:
                print(f'{file} contains invalid column(s).')
            return []

        shapes.append(shape)

    return shapes
