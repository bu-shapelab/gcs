import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from gcs.utils.summed_cosine import summed_cosine


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
cmap = cm.get_cmap('plasma')

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

for step in range(n_steps):
    radii = np.apply_along_axis(func1d=summed_cosine,
                axis=0,
                arr=thetas + twists_linear[step] + twists_oscillating[step],
                r0=r0s[step],
                c1=c1s[step],
                c2=c2s[step])
    ax.fill(thetas, radii, color=cmap(color_steps[step]))

ax.axis('off')
plt.savefig('misc/images/logo.svg', format='svg', dpi=1200)
