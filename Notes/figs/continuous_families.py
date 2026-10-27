# Two figures for Week 6 notes (C&B Section 3.3).
# normal_approx.png: binomial(25, .6) pmf with the n(15, 2.45^2) pdf and the continuity correction
#                    (Example 3.3.2, Figure 3.3.2).
# beta_cauchy.png:   left, beta densities (Figure 3.3.3); right, n(0, 1) vs Cauchy(0) (Figure 3.3.5).
# Run: python continuous_families.py  ->  writes both pngs next to this script.
import os
from math import comb, gamma
import numpy as np
import matplotlib.pyplot as plt

BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
LIGHT_BLUE = "#b7d3f6"
HERE = os.path.dirname(os.path.abspath(__file__))


def tidy(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#e5e5e5", lw=0.6)
    ax.set_axisbelow(True)


# --- Figure 1: normal approximation with continuity correction ---
n, p = 25, 0.6
mu, sd = n * p, np.sqrt(n * p * (1 - p))
k = np.arange(5, 26)
pmf = np.array([comb(n, j) * p ** j * (1 - p) ** (n - j) for j in k])
x = np.linspace(4.5, 25.5, 800)
phi = np.exp(-(x - mu) ** 2 / (2 * sd ** 2)) / (np.sqrt(2 * np.pi) * sd)

fig, ax = plt.subplots(figsize=(8, 3.8))
colors = [BLUE if j <= 13 else LIGHT_BLUE for j in k]
ax.bar(k, pmf, width=0.94, color=colors, label=r"binomial(25, 0.6) pmf, bars of width 1")
ax.plot(x, phi, color=ORANGE, lw=2, label=r"n$(15, 2.45^2)$ pdf")
ax.axvline(13, color="#555", lw=1, ls=":")
ax.axvline(13.5, color="#555", lw=1, ls="--")
ax.text(12.9, 0.172, "13", ha="right", fontsize=10, color="#333")
ax.text(13.6, 0.172, "13.5", ha="left", fontsize=10, color="#333")
ax.text(5.0, 0.125, r"$P(X \leq 13) = .267$ (dark bars)" "\n"
        r"$P(Y \leq 13) = .206$" "\n" r"$P(Y \leq 13.5) = .271$",
        fontsize=10, color="#333", va="center")
ax.set_title("Normal approximation to the binomial, with continuity correction", fontsize=12)
ax.set_xlabel("$x$"); ax.set_xlim(4.5, 25.5); ax.set_ylim(0, 0.19)
ax.set_xticks(range(5, 26, 2))
tidy(ax)
ax.legend(frameon=False, fontsize=10, loc="upper right")
fig.tight_layout()
fig.savefig(os.path.join(HERE, "normal_approx.png"), dpi=200)

# --- Figure 2: beta shapes; normal vs Cauchy ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

u = np.linspace(0.002, 0.998, 1000)
betas = [((2, 5), BLUE, "unimodal"),
         ((5, 1), ORANGE, "increasing"),
         ((0.5, 0.5), AQUA, "U-shaped"),
         ((2, 2), YELLOW, "symmetric")]
for (a, b), col, word in betas:
    f = u ** (a - 1) * (1 - u) ** (b - 1) * gamma(a + b) / (gamma(a) * gamma(b))
    ax1.plot(u, f, color=col, lw=2, label=rf"$\alpha = {a:g},\ \beta = {b:g}$ ({word})")
ax1.text(0.22, 2.62, "(2, 5)", fontsize=10, color="#333")
ax1.text(0.70, 3.25, "(5, 1)", fontsize=10, color="#333")
ax1.text(0.03, 2.95, "(0.5, 0.5)", fontsize=10, color="#333")
ax1.text(0.44, 1.58, "(2, 2)", fontsize=10, color="#333")
ax1.set_title(r"beta$(\alpha, \beta)$ densities", fontsize=12)
ax1.set_xlabel("$x$"); ax1.set_xlim(0, 1); ax1.set_ylim(0, 5.2)
ax1.legend(frameon=False, fontsize=9, loc="upper left")

z = np.linspace(-6, 6, 1200)
ax2.plot(z, np.exp(-z ** 2 / 2) / np.sqrt(2 * np.pi), color=BLUE, lw=2, label="n(0, 1)")
ax2.plot(z, 1 / (np.pi * (1 + z ** 2)), color=ORANGE, lw=2, label="Cauchy(0)")
ax2.text(0.9, 0.36, "n(0, 1)", fontsize=10, color="#333")
ax2.text(2.4, 0.065, "Cauchy: thicker tails", fontsize=10, color="#333")
ax2.set_title("Standard normal and Cauchy densities", fontsize=12)
ax2.set_xlabel("$x$"); ax2.set_xlim(-6, 6); ax2.set_ylim(0, 0.45)
ax2.legend(frameon=False, fontsize=10, loc="upper left")

for ax in (ax1, ax2):
    tidy(ax)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "beta_cauchy.png"), dpi=200)
