from __future__ import annotations

from typing import Union, TYPE_CHECKING
import pandas as pd

from ..cls import CLS

if TYPE_CHECKING:
    from os import PathLike


def load(file: Union[str, bytes, PathLike]) -> list[CLS]:
    """TODO
    """
    csv = pd.read_csv(filepath_or_buffer=file, sep=',', header=0)

    shapes = []

    for _, row in csv.iterrows():
        parameters = row.to_dict()
        shape = CLS(**parameters)
        shapes.append(shape)

    return shapes
