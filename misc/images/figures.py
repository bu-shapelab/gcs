from __future__ import annotations

from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
from gcs.utils import summed_cosine

################################
########### logo.svg ###########
################################

n_steps = 100

thetas = np.arange(start=0,
                   stop=2 * np.pi,
                   step=0.01)

c4s = np.linspace(start=0.5,
                  stop=0.2,
                  num=n_steps)
c8s = np.linspace(start=0.2,
                  stop=0.1,
                  num=n_steps)
r0s = np.linspace(start=1,
                  stop=-0.5,
                  num=n_steps)

twists_linear = np.linspace(start=0,
                            stop=1,
                            num=n_steps)
twists_oscillating = 0.8 * np.sin(np.linspace(start=0,
                                              stop=2 * np.pi * 0.6,
                                              num=n_steps))
color_steps = np.linspace(start=0,
                          stop=1,
                          num=n_steps)
cmap = cm.get_cmap()
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

for step in range(n_steps):
    radii = np.apply_along_axis(func1d=summed_cosine,
                                axis=0,
                                arr=thetas +
                                twists_linear[step] + twists_oscillating[step],
                                r0=r0s[step],
                                c4=c4s[step],
                                c8=c8s[step])
    ax.fill(thetas, radii, color=cmap(color_steps[step]))

ax.axis('off')
plt.savefig('misc/images/logo.svg', format='svg', dpi=1200)

################################
############ cs.svg ############
################################

theta = np.linspace(0, 2 * np.pi, 200)

fig, axs = plt.subplots(nrows=7,
                        ncols=7,
                        sharex=True,
                        sharey=True,
                        subplot_kw={'projection': 'polar'})

for row in range(7):
    for col in range(7):
        c4 = (col - 3) * 0.1
        c8 = (row - 3) * -0.1
        radius = summed_cosine(theta=theta,
                               r0=1,
                               c4=c4,
                               c8=c8)
        axs[row, col].plot(theta, radius, color='black')

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

fig.supxlabel('$\mathtt{c4}$')
fig.supylabel('$\mathtt{c8}$')
plt.tight_layout()
plt.savefig('misc/images/cs.svg', format='svg', dpi=300)
plt.show()

################################
########## twist.svg ###########
################################

height = 1
amplitude = np.pi / 16
cycles = 2
linear = 2

y = np.linspace(0, height, 100)
x_linear = np.linspace(0, linear, 100)
x_oscillating = amplitude * np.sin(np.linspace(0, 2 * np.pi * cycles, 100))
plt.plot(x_linear, y, label='Linear Twist')
plt.plot(x_oscillating, y, label='Oscillating Twist')
plt.plot(x_linear+x_oscillating, y, label='Combined Twist')

plt.xlabel('Rotation (rad)')
plt.xticks([-0.5, 0, 0.5, 1, 1.5, 2])
plt.ylabel('$z$ (mm)')
plt.yticks([0, height])
plt.gca().set_yticklabels([0, '$\mathtt{height}$'])
plt.gca().legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig('misc/images/twist.svg', format='svg', dpi=300)
plt.show()
