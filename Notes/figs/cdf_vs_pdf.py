# Two-panel figure for Week 3 notes: pdf vs. cdf of the logistic distribution (C&B Examples 1.5.5, 1.6.4).
# Run: python cdf_vs_pdf.py  ->  writes cdf_vs_pdf.png next to this script.
import os
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.exp(-x) / (1 + np.exp(-x)) ** 2   # pdf
F = lambda x: 1 / (1 + np.exp(-x))                  # cdf
x = np.linspace(-6, 6, 600)
x0 = 1.0

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(11, 4))

# Right: pdf, with the area to the left of x0 shaded.
ax1.plot(x, f(x), color="#1a4f9c", lw=2)
xs = x[x <= x0]
ax1.fill_between(xs, f(xs), color="#1a4f9c", alpha=0.25)
ax1.axvline(x0, color="gray", ls=":", lw=1)
ax1.annotate(f"shaded area\n$= F_X({x0:g}) \\approx {F(x0):.3f}$", xy=(-0.6, 0.08), xytext=(-5.8, 0.20),
             arrowprops=dict(arrowstyle="->", color="black"), fontsize=11)
ax1.plot([x0], [f(x0)], "o", color="#c0392b")
ax1.annotate(f"height $f_X({x0:g}) \\approx {f(x0):.3f}$", xy=(x0, f(x0)), xytext=(1.6, 0.21),
             arrowprops=dict(arrowstyle="->", color="#c0392b"), color="#c0392b", fontsize=11)
ax1.set_title(r"pdf $f_X(x) = e^{-x}/(1+e^{-x})^2$", fontsize=12)
ax1.set_xlabel("$x$"); ax1.set_ylim(0, 0.3)

# Left: cdf, with the height at x0 and the tangent line (slope = pdf).
ax2.plot(x, F(x), color="#1a4f9c", lw=2)
ax2.axhline(0, color="gray", lw=0.6); ax2.axhline(1, color="gray", lw=0.6, ls="--")
ax2.vlines(x0, 0, F(x0), color="gray", ls=":", lw=1)
ax2.hlines(F(x0), -6, x0, color="#1a4f9c", ls=":", lw=1.2)
ax2.plot([x0], [F(x0)], "o", color="#1a4f9c")
ax2.annotate(f"height $= F_X({x0:g}) \\approx {F(x0):.3f}$\n(the shaded area at right)", xy=(x0, F(x0)), xytext=(-5.8, 0.82),
             arrowprops=dict(arrowstyle="->", color="black"), fontsize=11)
t = np.linspace(x0 - 1.3, x0 + 1.3, 2)
ax2.plot(t, F(x0) + f(x0) * (t - x0), color="#c0392b", lw=1.5)
ax2.annotate(f"slope $= f_X({x0:g}) \\approx {f(x0):.3f}$", xy=(x0 + 0.9, F(x0) + f(x0) * 0.9), xytext=(2.3, 0.45),
             arrowprops=dict(arrowstyle="->", color="#c0392b"), color="#c0392b", fontsize=11)
ax2.set_title(r"cdf $F_X(x) = 1/(1+e^{-x})$", fontsize=12)
ax2.set_xlabel("$x$"); ax2.set_ylim(-0.05, 1.08)

for ax in (ax1, ax2):
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xlim(-6, 6)
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cdf_vs_pdf.png"), dpi=200)
