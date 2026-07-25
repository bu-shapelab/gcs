from __future__ import annotations

from pathlib import Path

from matplotlib import pyplot as plt


def main() -> None:
    _, axes = plt.subplots(nrows=2, ncols=4, constrained_layout=True, figsize=(6.4, 3.2))

    current_dir = Path(__file__).parent

    ordering = [5, 3, 7, 4, 1, 6, 2, 8]

    index = 0
    for i in range(2):
        for j in range(4):
            image = plt.imread(fname=current_dir / 'images' / f'{ordering[index]}.png')
            axes[i, j].imshow(X=image)
            axes[i, j].set_axis_off()

            index += 1

    path = Path(__file__).parent.resolve() / 'images' / 'teaser.png'
    plt.savefig(path, format='png', dpi=200) # (6.4, 3.2) * 200 = (1280, 640)

    plt.show()


if __name__ == '__main__':
    main()
