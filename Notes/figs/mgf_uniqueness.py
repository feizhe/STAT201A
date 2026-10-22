# Two-panel figure for Week 5 notes (C&B Section 2.3).
# Left: two pdfs with the same moments (Example 2.3.10, Figure 2.3.2).
# Right: Poisson approximation to the binomial, n = 15, p = .3 (Example 2.3.13, Figure 2.3.3).
# Run: python mgf_uniqueness.py  ->  writes mgf_uniqueness.png next to this script.
import os
from math import comb, exp, factorial
import numpy as np
import matplotlib.pyplot as plt

BLUE, ORANGE = "#2a78d6", "#eb6834"

x = np.linspace(1e-4, 5, 2000)
f1 = np.exp(-np.log(x) ** 2 / 2) / (np.sqrt(2 * np.pi) * x)
f2 = f1 * (1 + np.sin(2 * np.pi * np.log(x)))

n, p = 15, 0.3
lam = n * p
k = np.arange(0, 15)
binom = np.array([comb(n, j) * p ** j * (1 - p) ** (n - j) for j in k])
pois = np.array([exp(-lam) * lam ** j / factorial(j) for j in k])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

ax1.plot(x, f1, color=BLUE, lw=2, label=r"$f_1(x)$ (lognormal)")
ax1.plot(x, f2, color=ORANGE, lw=2, label=r"$f_2(x) = f_1(x)[1 + \sin(2\pi \log x)]$")
ax1.text(1.95, 0.19, r"$f_1$", fontsize=12, color="#333")
ax1.text(1.5, 0.6, r"$f_2$", fontsize=12, color="#333")
ax1.set_title("Different pdfs, the same moments $\\mathrm{E}X^r = e^{r^2/2}$", fontsize=12)
ax1.set_xlabel("$x$"); ax1.set_xlim(0, 5); ax1.set_ylim(0, 1.35)

w = 0.38
ax2.bar(k - w / 2 - 0.02, binom, width=w, color=BLUE, label="binomial(15, 0.3)")
ax2.bar(k + w / 2 + 0.02, pois, width=w, color=ORANGE, label=r"Poisson$(\lambda = np = 4.5)$")
ax2.set_title("Poisson approximation to the binomial", fontsize=12)
ax2.set_xlabel("$x$"); ax2.set_xticks(range(0, 15, 2)); ax2.set_xlim(-0.7, 14.5)

for ax in (ax1, ax2):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#e5e5e5", lw=0.6); ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mgf_uniqueness.png"), dpi=200)
