from __future__ import annotations

import random
from typing import Optional, TYPE_CHECKING
from .rand import rand

if TYPE_CHECKING:
    from cls import CLS


def randn(n: int, fixed_parameters: Optional[dict] = None, seed: Optional[int] = None) -> list[CLS]:
    """TODO
    """
    if seed is not None:
        random.seed(seed)

    shapes = []

    for _ in range(n):
        shape = rand(fixed_parameters=fixed_parameters, seed=None)
        shapes.append(shape)

    return shapes
