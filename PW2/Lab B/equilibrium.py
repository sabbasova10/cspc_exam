"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.

def k_imbalance(x):
        return ((2*x)**2)/((a-x)*(b-x)) - K
        
# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.
result_n = newton(k_imbalance, x0=0.5)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
result_m = minimize(lambda x: k_imbalance(x)**2, x0=0.5, bounds=[(0, 0.999)], method="SLSQP")
print(result_n, result_m.x)

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.

x_eq = result_n
h2_n = a-x_eq
i2_n = b-x_eq
hi_n = x_eq*2

print(h2_n, i2_n, hi_n)

x_vals = np.linspace(0,1,200)
h2_vals = a - x_vals
i2_vals = b-x_vals
hi_vals = x_vals*2

fig, ax1 = plt.subplots(1,1)
ax1.plot(x_vals, i2_vals, label="I2 amount")
ax1.plot(x_vals, h2_vals, color="red", label="H2 amount")
ax1.plot(x_vals, hi_vals, color="green", label="HI amount")

ax1.axvline(x=x_eq, color="grey", linestyle=":", label="Equilibrium")
ax1.plot(x_eq, i2_n, 'bo', label="Eq. point")
ax1.plot(x_eq, h2_n, 'bo')

ax1.legend()
ax1.grid(True, alpha=0.3)
fig.savefig("equilibrium.png")
plt.show()
