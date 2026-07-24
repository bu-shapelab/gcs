from __future__ import annotations

from pathlib import Path

from matplotlib import pyplot as plt
import numpy as np


def main() -> None:
    ###########################
    ########## Setup ##########
    ###########################

    h = 1
    amplitude = np.pi / 16
    cycles = 2
    linear = 2

    n_steps = 100
    height = np.linspace(start=0, stop=h, num=n_steps)
    linear_theta = np.linspace(start=0, stop=linear, num=n_steps)

    frequency = np.linspace(start=0, stop=2 * np.pi * cycles, num=n_steps)
    oscillating_theta = amplitude * np.sin(frequency)

    ##############################
    ########## Plotting ##########
    ##############################

    _, ax = plt.subplots(nrows=1, ncols=1, constrained_layout=True, figsize=(6.4, 4.8))

    ax.plot(height, linear_theta, label='Linear Twist')
    ax.plot(height, oscillating_theta, label='Oscillating Twist')
    ax.plot(height, linear_theta + oscillating_theta, label='Combined Twist')

    ax.set_ylabel(ylabel='Rotation (rad)')
    ax.set_yticks([-0.5, 0, 0.5, 1, 1.5, 2])
    ax.set_xlabel(xlabel='Normalized height')
    ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    ax.legend(loc='upper left')

    folder = Path(__file__).parent.resolve()
    plt.savefig(folder / 'images' / f'{Path(__file__).stem}.svg')
    plt.show()


if __name__ == '__main__':
    main()
