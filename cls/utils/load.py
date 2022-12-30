from __future__ import annotations

from typing import Union, TYPE_CHECKING
import pandas as pd

from cls import CLS

if TYPE_CHECKING:
    from os import PathLike


def load(file: Union[str, bytes, PathLike], verbose: bool = False) -> list[CLS]:
    """TODO
    """
    try:
        csv = pd.read_csv(filepath_or_buffer=file, sep=',', header=0)
    except FileNotFoundError:
        if verbose:
            print('TODO')
        return []
    except pd.errors.EmptyDataError:
        if verbose:
            print('TODO')
        return []

    shapes = []

    for _, row in csv.iterrows():
        parameters = row.to_dict()

        try:
            shape = CLS(**parameters)
        except TypeError:
            if verbose:
                print('TODO')
            return []

        shapes.append(shape)

    return shapes
