from __future__ import annotations

import random
from typing import Optional, TYPE_CHECKING, List
from cls.random import rand

if TYPE_CHECKING:
    from cls import CLS


def randn(num: int,
          seed: Optional[int] = None,
          fixed_kwargs: Optional[dict] = None) -> List[CLS]:
    """Creates multiple valid random (valid) CLS.

    Parameters
    ----------
    num : int
        The number of CLS to generate.
    seed : int, optional
        A random seed.
    fixed_kwargs : dict, optional
        The kwargs of fixed parameters for ``cls.CLS`` initalization.

    Returns
    -------
    shapes : List[cls.CLS]
        The random CLS.

    Examples
    --------
    >>> shapes = cls.random.rand(num=1)
    >>> shape = shapes[0]

    >>> shapes = cls.random.rand(num=3)

    >>> fixed_parameters = { 'c1_base': 0.5, 'height': 20 }
    >>> shapes = cls.random.randn(n=3, fixed_parameters=fixed_parameters)

    """
    if seed is not None:
        random.seed(seed)

    shapes = []

    for _ in range(num):
        shape = rand(fixed_kwargs=fixed_kwargs)
        shapes.append(shape)

    return shapes
