import time
import heat
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(10, 4), constrained_layout=True)



p2 = ax.imshow(heat.TwoDimLaser(), cmap='plasma', aspect='equal', interpolation='gaussian', origin="lower",
               extent=(0, 25
                       , 0, 5))

fig.colorbar(p2)
ax.set_title('Temperature Field')
ax.set_xlabel('Width (mm)')
ax.set_ylabel('Height (mm)')
fig.canvas.draw()