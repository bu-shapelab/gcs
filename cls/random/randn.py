from __future__ import annotations

import random
from typing import Optional, TYPE_CHECKING
from cls.random import rand

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
        If ``n`` is not an integer.
    ValueError
        If ``n`` is not positive.

    Examples
    --------
    >>> shapes = cls.random.rand(n=1)
    >>> shape = shapes[0]

    >>> shapes = cls.random.rand(n=3)

    >>> fixed_parameters = { 'c1_base': 0.5, 'height': 20 }
    >>> shapes = cls.random.randn(n=3, fixed_parameters=fixed_parameters)

    """
    if not isinstance(n, int):
        raise TypeError('n needs to be an integer.')
    if n < 1:
        raise ValueError('n needs to be positive.')

    if seed is not None:
        random.seed(seed)

    shapes = []

    for _ in range(n):
        shape = rand(fixed_parameters=fixed_parameters, seed=None)
        shapes.append(shape)

    return shapes
