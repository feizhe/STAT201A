# Two-panel figure for Week 4 notes: gamma pdf and inverted gamma pdf (C&B Example 2.1.6), n = 3.
# Run: python gamma_invgamma.py  ->  writes gamma_invgamma.png next to this script.
import os
from math import factorial
import numpy as np
import matplotlib.pyplot as plt

n = 3
betas = [0.5, 1, 2]
colors = ["#6da7ec", "#256abf", "#0d366b"]   # one hue, light -> dark as beta increases
c = lambda b: 1 / (factorial(n - 1) * b ** n)
gam = lambda x, b: c(b) * x ** (n - 1) * np.exp(-x / b)
inv = lambda y, b: c(b) * (1 / y) ** (n + 1) * np.exp(-1 / (b * y))

x = np.linspace(1e-4, 15, 800)
y = np.linspace(1e-3, 2, 800)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

for b, col in zip(betas, colors):
    ax1.plot(x, gam(x, b), color=col, lw=2, label=rf"$\beta = {b:g}$")
    ax2.plot(y, inv(y, b), color=col, lw=2, label=rf"$\beta = {b:g}$")
    # direct labels at each mode: gamma mode (n-1)beta; inverted gamma mode 1/((n+1)beta)
    xm = (n - 1) * b; ax1.annotate(rf"$\beta = {b:g}$", (xm, gam(xm, b)), xytext=(6, 4), textcoords="offset points", fontsize=10, color="#333")
    ym = 1 / ((n + 1) * b); ax2.annotate(rf"$\beta = {b:g}$", (ym, inv(ym, b)), xytext=(6, 2), textcoords="offset points", fontsize=10, color="#333")

ax1.set_title(rf"gamma pdf of $X$ ($n = {n}$): mean $n\beta$", fontsize=12)
ax1.set_xlabel("$x$"); ax1.set_xlim(0, 15); ax1.set_ylim(0, 0.62)
ax2.set_title(rf"inverted gamma pdf of $Y = 1/X$ ($n = {n}$)", fontsize=12)
ax2.set_xlabel("$y$"); ax2.set_xlim(0, 2); ax2.set_ylim(0, 5.4)

for ax in (ax1, ax2):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#e5e5e5", lw=0.6); ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gamma_invgamma.png"), dpi=200)
