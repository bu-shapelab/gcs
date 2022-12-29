from __future__ import annotations

from typing import TYPE_CHECKING

from .preview_step import preview_step

if TYPE_CHECKING:
    from cls import CLS


def preview_top(shape: CLS) -> None:
    """TODO
    """
    preview_step(shape=shape, step=-1, title='Top Preview')
