from __future__ import annotations

import random
from typing import Optional, TYPE_CHECKING

from .rand import rand

if TYPE_CHECKING:
    from cls import CLS


def randn(n: int, fixed_parameters: Optional[dict] = None, seed: Optional[int] = None) -> list[CLS]:
    """Creates multiple valid random CLS.

    Parameters
    ----------
        n : int
            The number of CLS to generate.
        fixed_parameters : dict, optional
            A dictionary of parameters with fixed-values to override randomization.
            The keys for ``fixed_parameters`` are the arguments to initialize a ``CLS``.
        seed : int, optional
            A random seed.

    Returns
    -------
    shape : list[cls.CLS]
        The random CLS.

    Raises
    ------
    TypeError
        If ``n`` is not a number.
    ValueError
        If ``n`` is not positive.

    Examples
    --------
    TODO

    """
    if not isinstance(n, int):
        raise TypeError('TODO')
    if n < 1:
        raise ValueError('TODO')

    if seed is not None:
        random.seed(seed)

    shapes = []

    for _ in range(n):
        shape = rand(fixed_parameters=fixed_parameters, seed=None)
        shapes.append(shape)

    return shapes
