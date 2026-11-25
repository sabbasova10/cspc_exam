"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
V, pH = np.loadtxt("data/titration.csv", delimiter=',', skiprows=1, unpack=True)

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
slope = np.gradient(pH, V)
V_eq = V[np.argmax(slope)]
print(V_eq)
pH_eq = pH[np.argmax(slope)]
print(pH_eq)

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.

fig, axes = plt.subplots(1,2)
axes[0].plot(V, pH, color="red", label="V by pH")
axes[1].plot(V, slope, color="green", label="V by slope")
axes[0].axhline(pH_eq, linestyle="--")

axes[0].set_title("pH vs V")
axes[1].set_title("slope vs V")
fig.legend()
plt.tight_layout()
# TODO 4: save the figure as figure.png
fig.savefig("results/titration.png")
plt.show()