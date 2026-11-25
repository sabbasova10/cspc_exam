'''
Bonus (if time permits) — A 2D tracked trajectory
Brief
trajectory.csv has three columns, time,x,y: the noisy tracked position of an object moving
in a plane (like GPS). The same idea works in 2D: differentiate x and y separately to get the
velocity and acceleration in each direction.
TODO: Read trajectory.csv, plot the path (x vs y), then compute and plot the 
speedq = v2_x + v2_y
over time using np.gradient on each coordinate
'''

import numpy as np
import matplotlib.pyplot as plt

t, x, y = np.loadtxt("trajectory.csv", delimiter=',', skiprows=1, unpack=True)

vx = np.gradient(x)
vy = np.gradient(y)
speed = np.sqrt(vx**2+vy**2)
ax = np.gradient(vx)
ay = np.gradient(vy)
a = np.sqrt(ax**2+ay**2)

fig, axes = plt.subplots(3,1)
axes[0].plot(x, y)
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].set_title("X over Y")

axes[1].plot(t, speed)
axes[1].set_xlabel("time")
axes[1].set_ylabel("speed")

axes[2].plot(t, a)
axes[2].set_xlabel("time")
axes[2].set_ylabel("acceleration")
plt.show()
fig.savefig("trajectory.png")