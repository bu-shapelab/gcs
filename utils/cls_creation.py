from __future__ import annotations

import pandas as pd
from shapes import CLS


def create_cls(c1_base: float, c2_base: float, c1_top: float, c2_top: float,
               twist_linear: float, twist_amplitude: float, twist_period: float,
               ratio: float, height: float, mass: float, density: float,
               thickness: float, n_steps: int, save_path: str) -> None:
    """Creates and saves a CLS file.

    Args:
        c1_base: The base 4-lobe parameter.
        c2_base: The base 8-lobe parameter.
        c1_top: The top 4-lobe parameter.
        c2_top: The top 8-lobe parameter.
        twist_linear: The linear component of twist.
        twist_amplitude: The amplitude of the oscillating component of twist.
        twist_period: The period of the oscillating component of twist.
        ratio: The ratio of the base to top perimeter.
        height: The height.
        mass: The mass.
        density: The density.
        thickness: The wall thickness.
        n_steps: Number of interpolation steps.
        save_path: The save path.
    """
    cls = CLS(c1_base=c1_base,
              c2_base=c2_base,
              c1_top=c1_top,
              c2_top=c2_top,
              twist_linear=twist_linear,
              twist_amplitude=twist_amplitude,
              twist_period=twist_period,
              ratio=ratio,
              height=height,
              mass=mass,
              density=density,
              thickness=thickness,
              n_steps=n_steps)

    cls.save(save_path)


def create_cls_from_csv(path: str) -> None:
    """Creates and saves CLS files from parameters saved in a csv file.

    The csv should contain an (n x 14) matrix where:
        - n: The number of CLS shapes to create.
        - 14: Each parameter of `cls_creation.create_cls()`.
    """
    data = pd.read_csv(path, delimiter=',', header=None)

    for idx in range(data.shape[0]):
        parameters = data.iloc[idx, :]
        create_cls(c1_base=parameters[0],
                   c2_base=parameters[1],
                   c1_top=parameters[2],
                   c2_top=parameters[3],
                   twist_linear=parameters[4],
                   twist_amplitude=parameters[5],
                   twist_period=parameters[6],
                   ratio=parameters[7],
                   height=parameters[8],
                   mass=parameters[9],
                   density=parameters[10],
                   thickness=parameters[11],
                   n_steps=parameters[12],
                   save_path=parameters[13])
