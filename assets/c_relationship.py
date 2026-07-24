from __future__ import annotations

from pathlib import Path

from gcs.geometry import summed_cosine
from matplotlib import pyplot as plt
import numpy as np


def main() -> None:
    ###########################
    ########## Setup ##########
    ###########################

    theta = np.linspace(start=0, stop=2 * np.pi, num=200)

    ##############################
    ########## Plotting ##########
    ##############################

    fig, axs = plt.subplots(nrows=7,
                            ncols=7,
                            sharex=True,
                            sharey=True,
                            constrained_layout=True,
                            figsize=(4.8, 4.8),
                            subplot_kw={'projection': 'polar'})

    for row in range(7):
        for col in range(7):
            c4 = (col - 3) * 0.1
            c8 = (row - 3) * -0.1
            r = summed_cosine(theta=theta, r0=1, c4=c4, c8=c8)

            axs[row, col].plot(theta, r, color='black')

            if c4 == 0:
                c4 = 0
            else:
                c4 = round(c4, 1)
            if c8 == 0:
                c8 = 0
            else:
                c8 = round(c8, 1)

            if row == 6:
                axs[row, col].set_xlabel(c4)
            if col == 0:
                axs[row, col].set_ylabel(c8)

            axs[row, col].set_xticks([])
            axs[row, col].set_yticks([])
            axs[row, col].spines['polar'].set_visible(False)

    fig.supxlabel(r'$\mathtt{c4}$')
    fig.supylabel(r'$\mathtt{c8}$')

    folder = Path(__file__).parent.resolve()
    plt.savefig(folder / 'images' / f'{Path(__file__).stem}.svg')
    plt.show()


if __name__ == '__main__':
    main()
