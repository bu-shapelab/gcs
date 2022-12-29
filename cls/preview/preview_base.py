from __future__ import annotations

from typing import TYPE_CHECKING
from .preview_step import preview_step

if TYPE_CHECKING:
    from cls import CLS


def preview_base(shape: CLS) -> None:
    """TODO
    """
    preview_step(shape=shape, step=0, title='Top Preview')
