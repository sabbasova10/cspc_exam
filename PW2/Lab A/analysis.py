"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
t, y = np.loadtxt("freefall.csv", delimiter=',', skiprows=1, unpack=True)

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)
a_mean = np.mean(a)
a_std = np.std(a, axis=0)
print(a_mean, a_std)

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
dv = cumulative_trapezoid(a, t, initial=0) + v[0]
dy = cumulative_trapezoid(dv, t, initial=0) + y[0]

print(np.ptp(y), np.ptp(dy))

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharex=True)
ax1.scatter(t, y, color="red")
ax2.plot(t, v, color="green")
ax3.plot(t, a)
ax3.axhline(-9.81, linestyle="--")
ax1.set_title("Time to pos")
ax2.set_title("Time to v")
ax3.set_title("Time to a")

plt.tight_layout()
# TODO 4: save the figure as figure.png
fig.savefig("motion.png")
plt.show()