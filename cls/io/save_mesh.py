from __future__ import annotations

from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from os import PathLike
    from cls import CLS


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
    shape.mesh.save(filename=file)
