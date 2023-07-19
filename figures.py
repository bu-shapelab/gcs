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

c1s = np.linspace(start=0.5,
                  stop=0.2,
                  num=n_steps)
c2s = np.linspace(start=0.2,
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
                                c1=c1s[step],
                                c2=c2s[step])
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
        c1 = (col - 3) * 0.1
        c2 = (row - 3) * -0.1
        radius = summed_cosine(theta=theta,
                               r0=1,
                               c1=c1,
                               c2=c2)
        axs[row, col].plot(theta, radius, color='black')

        if c1 == 0:
            c1 = 0
        else:
            c1 = round(c1, 1)
        if c2 == 0:
            c2 = 0
        else:
            c2 = round(c2, 1)

        if row == 6:
            axs[row, col].set_xlabel(c1)
        if col == 0:
            axs[row, col].set_ylabel(c2)
        axs[row, col].set_xticks([])
        axs[row, col].set_yticks([])
        axs[row, col].spines['polar'].set_visible(False)

fig.supxlabel('$\mathtt{c1}$')
fig.supylabel('$\mathtt{c2}$')
plt.tight_layout()
plt.savefig('misc/images/cs.svg', format='svg', dpi=300)
plt.show()

################################
########## twist.svg ###########
################################

height = 1
amplitude = 0.25
period = 2
linear = 1.75

y = np.linspace(0, height, 100)
x_linear = np.linspace(0, linear, 100)
x_oscillating = amplitude * np.sin(np.linspace(0, 2 * np.pi * period, 100))
plt.plot(x_linear, y, label='Linear Twist')
plt.plot(x_oscillating, y, label='Oscillating Twist')
plt.plot(x_linear+x_oscillating, y, label='Combined Twist')
plt.vlines(x=linear,
           ymin=0,
           ymax=height,
           linestyles=':',
           colors='C0',
           label='$\mathtt{twist\_linear}$')
plt.vlines(x=-0.25,
           ymin=0.37,
           ymax=0.88,
           linestyles='--',
           colors='C1',
           label='$\mathtt{twist\_period}$')
plt.hlines(y=0.88,
           xmin=-0.25,
           xmax=0,
           linestyles=':',
           colors='C1',
           label='$\mathtt{twist\_amplitude}$')
plt.xlabel('Rotation (rad)')
plt.xticks([-0.5, 0, 0.5, 1, 1.5, 2])
plt.ylabel('$z$ (mm)')
plt.yticks([0, height])
plt.gca().set_yticklabels([0, '$\mathtt{height}$'])
plt.gca().legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig('misc/images/twist.svg', format='svg', dpi=300)
plt.show()
