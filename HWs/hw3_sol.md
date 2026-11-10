---
layout: page
---

# STAT 201A Homework 3 Solutions

Theorem numbers refer to Casella & Berger (C&B). The tools used most often are

- **Theorem 2.1.5 (monotone transformations).** If $g$ is monotone on $\mathcal{X}$, $f_X$ is continuous on $\mathcal{X}$, and $g^{-1}$ has a continuous derivative on $\mathcal{Y}$, then $f_Y(y) = f_X\big( g^{-1}(y) \big) \left\lvert \frac{d}{dy} g^{-1}(y) \right\rvert$ for $y \in \mathcal{Y}$. **Theorem 2.1.8** adds these terms over the pieces on which $g$ is monotone.
- **Definition 2.2.1 and Theorem 2.2.5.** $\mathrm{E}\,g(X) = \int g(x) f_X(x)\, dx$ when $\mathrm{E}\lvert g(X) \rvert < \infty$, and expectation is linear.
- **Theorems 2.3.7 and 2.3.15.** $\mathrm{E}X^n = M_X^{(n)}(0)$, and $M_{aX + b}(t) = e^{bt} M_X(at)$.

---

**1. (Exercise 2.2(c))** *Let $f_X(x) = \frac{1}{\sigma^2} x e^{-(x/\sigma)^2/2}$, $0 < x < \infty$. Find the pdf of $Y = e^X$, and show that it integrates to 1.*

The supports are $\mathcal{X} = (0, \infty)$ and $\mathcal{Y} = (1, \infty)$. The function $g(x) = e^x$ is increasing, with $g^{-1}(y) = \log y$ and $\frac{d}{dy} g^{-1}(y) = \frac{1}{y}$, which is continuous on $\mathcal{Y}$. Since $f_X$ is continuous on $\mathcal{X}$, Theorem 2.1.5 gives

$$
f_Y(y) = f_X(\log y) \cdot \frac{1}{y} = \frac{\log y}{\sigma^2 y}\, e^{-(\log y)^2 / (2\sigma^2)}, \qquad 1 < y < \infty,
$$

and $f_Y(y) = 0$ otherwise.

*It integrates to 1.* Substitute $u = \log y$, $du = dy/y$:

$$
\int_1^{\infty} f_Y(y)\, dy = \int_0^{\infty} \frac{u}{\sigma^2} e^{-u^2/(2\sigma^2)}\, du = \Big[ -e^{-u^2/(2\sigma^2)} \Big]_0^{\infty} = 0 - (-1) = 1.
$$

(The substitution undoes the transformation, so this is the statement that $f_X$ integrates to 1.)

---

**2. (Exercise 2.6(b))** *Let $f_X(x) = \frac{3}{8} (x + 1)^2$, $-1 < x < 1$. Find the pdf of $Y = 1 - X^2$, and show that it integrates to 1.*

$g(x) = 1 - x^2$ is not monotone on $\mathcal{X} = (-1, 1)$, so we use Theorem 2.1.8 with

$$
A_0 = \lbrace 0 \rbrace, \qquad A_1 = (-1, 0), \qquad A_2 = (0, 1).
$$

- $P(X \in A_0) = 0$, and $f_X$ is continuous on $A_1$ and $A_2$.
- $g$ is increasing on $A_1$ and decreasing on $A_2$, and both pieces map onto $\mathcal{Y} = (0, 1)$.
- The inverses are $g_1^{-1}(y) = -\sqrt{1 - y}$ and $g_2^{-1}(y) = \sqrt{1 - y}$, with $\left\lvert \frac{d}{dy} g_i^{-1}(y) \right\rvert = \frac{1}{2\sqrt{1 - y}}$, continuous on $(0, 1)$.

Write $s = \sqrt{1 - y}$. Then

$$
\begin{aligned}
f_Y(y) &= \frac{1}{2s} \Big[ f_X(-s) + f_X(s) \Big] = \frac{1}{2s} \cdot \frac{3}{8} \Big[ (1 - s)^2 + (1 + s)^2 \Big] \\
&= \frac{3}{8} \cdot \frac{2 + 2s^2}{2s} = \frac{3}{8} \cdot \frac{2 - y}{\sqrt{1 - y}}, \qquad 0 < y < 1,
\end{aligned}
$$

and $f_Y(y) = 0$ otherwise. (The pdf is unbounded near $y = 1$, which corresponds to $X$ near 0, where $g$ is flat.)

*It integrates to 1.* Substitute $w = 1 - y$:

$$
\int_0^1 \frac{3}{8} \cdot \frac{2 - y}{\sqrt{1 - y}}\, dy = \frac{3}{8} \int_0^1 \frac{1 + w}{\sqrt{w}}\, dw = \frac{3}{8} \Big[ 2w^{1/2} + \tfrac{2}{3} w^{3/2} \Big]_0^1 = \frac{3}{8} \cdot \frac{8}{3} = 1.
$$

---

**3. An inverse cdf with a jump (adapted from Exercise 2.8(c)).** *Show that $F_X(x) = e^x/4$ for $x < 0$ and $1 - e^{-x}/4$ for $x \ge 0$ is a cdf, and find $F_X^{-1}(y)$. With $X = F_X^{-1}(V)$, find $P(X = 0)$. Is $F_X(X)$ uniform(0, 1)?*

**It is a cdf** (Theorem 1.5.3).

- **Limits.** $\lim_{x \to -\infty} e^x/4 = 0$ and $\lim_{x \to \infty} \big( 1 - e^{-x}/4 \big) = 1$.
- **Nondecreasing.** Both pieces are increasing. At $x = 0$, $F_X$ jumps *up*, from $\lim_{x \uparrow 0} F_X(x) = \frac{1}{4}$ to $F_X(0) = \frac{3}{4}$.
- **Right-continuous.** Each piece is continuous, and at $x = 0$, $\lim_{x \downarrow 0} F_X(x) = \frac{3}{4} = F_X(0)$.

$F_X$ has a jump of size $\frac{1}{2}$ at 0 and increases continuously elsewhere, so $X$ is neither continuous nor discrete.

**The inverse cdf.** For $0 < y < 1$, $F_X^{-1}(y) = \inf \lbrace x : F_X(x) \ge y \rbrace$. The values of $F_X$ are $(0, \frac{1}{4})$ on $x < 0$ and $[\frac{3}{4}, 1)$ on $x \ge 0$.

- If $0 < y < \frac{1}{4}$: for $x < 0$, $e^x/4 \ge y \iff x \ge \log(4y)$, and $\log(4y) < 0$, so $F_X^{-1}(y) = \log(4y)$ in this range.
- If $\frac{1}{4} \le y \le \frac{3}{4}$: $F_X(x) < \frac{1}{4} \le y$ for every $x < 0$, while $F_X(0) = \frac{3}{4} \ge y$. So $F_X^{-1}(y) = 0$.
- If $\frac{3}{4} < y < 1$: for $x \ge 0$, $1 - e^{-x}/4 \ge y \iff x \ge -\log\big( 4(1 - y) \big)$, and this is positive. So $F_X^{-1}(y) = -\log\big( 4(1 - y) \big)$.

$$
F_X^{-1}(y) =
\begin{cases}
\log(4y) & 0 < y < \frac{1}{4} \\
0 & \frac{1}{4} \le y \le \frac{3}{4} \\
-\log\big( 4(1 - y) \big) & \frac{3}{4} < y < 1.
\end{cases}
$$

The whole interval $[\frac{1}{4}, \frac{3}{4}]$ of $y$ values is sent to the single point 0. This is how the inverse cdf handles a jump.

**$P(X = 0)$.** With $X = F_X^{-1}(V)$,

$$
P(X = 0) = P\left( \tfrac{1}{4} \le V \le \tfrac{3}{4} \right) = \frac{1}{2} = F_X(0) - \lim_{x \uparrow 0} F_X(x) = \frac{3}{4} - \frac{1}{4},
$$

the size of the jump of $F_X$ at 0.

**Is $F_X(X)$ uniform?** No. On $\lbrace X = 0 \rbrace$, $F_X(X) = F_X(0) = \frac{3}{4}$, so

$$
P\left( F_X(X) = \tfrac{3}{4} \right) \ge P(X = 0) = \frac{1}{2},
$$

while a uniform(0, 1) random variable gives probability 0 to every single point. (In fact $F_X(X) = V$ when $V \notin [\frac{1}{4}, \frac{3}{4}]$, and $F_X(X) = \frac{3}{4}$ otherwise; $F_X(X)$ never takes values in $(\frac{1}{4}, \frac{3}{4})$.)

This does not contradict Theorem 2.1.10, which assumes that $F_X$ is **continuous**. Here $F_X$ jumps at 0. The other direction still works: $F_X^{-1}(V)$ has cdf $F_X$ for *any* cdf, which is why the inverse cdf method can simulate distributions with jumps.

---

**4. Expectations from tail probabilities (adapted from Exercises 2.14(a) and 2.16).** *For a continuous, nonnegative $X$, show that $\mathrm{E}X = \int_0^{\infty} [1 - F_X(x)]\, dx$. Use this to find $\mathrm{E}T$ if $P(T > t) = 0.8 e^{-t/2} + 0.2 e^{-t/10}$, $t \ge 0$.*

Write $x = \int_0^x dt$. Since $f_X(x) = 0$ for $x < 0$,

$$
\begin{aligned}
\mathrm{E}X &= \int_0^{\infty} x f_X(x)\, dx = \int_0^{\infty} \left( \int_0^x dt \right) f_X(x)\, dx \\
&= \int_0^{\infty} \int_t^{\infty} f_X(x)\, dx\, dt = \int_0^{\infty} P(X > t)\, dt = \int_0^{\infty} \big[ 1 - F_X(t) \big]\, dt.
\end{aligned}
$$

The third equality interchanges the order of integration over the region $\lbrace (t, x) : 0 < t < x < \infty \rbrace$. For fixed $x$, $t$ runs over $(0, x)$; for fixed $t$, $x$ runs over $(t, \infty)$. The interchange is allowed because the integrand $f_X(x) \ge 0$. The identity holds even when $\mathrm{E}X = \infty$: both sides are then infinite.

**Telephone calls.** $T \ge 0$, and its cdf $1 - P(T > t)$ is continuous, so

$$
\mathrm{E}T = \int_0^{\infty} \Big( 0.8 e^{-t/2} + 0.2 e^{-t/10} \Big)\, dt = 0.8 \cdot 2 + 0.2 \cdot 10 = 3.6 \text{ minutes},
$$

using $\int_0^{\infty} e^{-t/\lambda}\, dt = \lambda$.

*Interpretation.* $P(T > t)$ is the survival function of a mixture: with probability 0.8 the call is "short," exponential with mean 2, and with probability 0.2 it is "long," exponential with mean 10. The mean of the mixture is the weighted average of the two means.

---

**5. Medians (Exercises 2.17 and 2.18).**

**(a)(i)** For $0 < m < 1$, $\int_0^m 3x^2\, dx = m^3$. Setting $m^3 = \frac{1}{2}$ gives

$$
m = 2^{-1/3} \approx 0.794.
$$

**(a)(ii)** The Cauchy cdf is $F(x) = \frac{1}{2} + \frac{1}{\pi} \tan^{-1} x$, so $F(m) = \frac{1}{2}$ gives $\tan^{-1} m = 0$, that is, $m = 0$. (Alternatively, the pdf is symmetric about 0.) The Cauchy distribution has no mean (Example 2.2.4), but it does have a median.

In both cases $F$ is strictly increasing on the support, so the median is unique.

**(b)** Let $G(a) = \mathrm{E}\lvert X - a \rvert$, which is finite because $\lvert X - a \rvert \le \lvert X \rvert + \lvert a \rvert$ and $\mathrm{E}\lvert X \rvert < \infty$. Splitting at $a$,

$$
\begin{aligned}
G(a) &= \int_{-\infty}^{a} (a - x) f(x)\, dx + \int_{a}^{\infty} (x - a) f(x)\, dx \\
&= a F(a) - \int_{-\infty}^{a} x f(x)\, dx + \int_{a}^{\infty} x f(x)\, dx - a \big[ 1 - F(a) \big].
\end{aligned}
$$

Differentiate in $a$ by the fundamental theorem of calculus (at points where $f$ is continuous):

$$
\begin{aligned}
G'(a) &= \big[ F(a) + a f(a) \big] - a f(a) - a f(a) - \big[ 1 - F(a) - a f(a) \big] \\
&= 2F(a) - 1.
\end{aligned}
$$

So $G'(a) \le 0$ when $F(a) \le \frac{1}{2}$, that is, for $a \le m$, and $G'(a) \ge 0$ for $a \ge m$. $G$ decreases up to $m$ and increases after it, so it is minimized at $a = m$:

$$
\min_a \mathrm{E}\lvert X - a \rvert = \mathrm{E}\lvert X - m \rvert.
$$

*A version that does not need $f$ continuous.* Integration by parts turns the first two terms of $G$ into $\int_{-\infty}^a F(s)\, ds$ and the last two into $\int_a^{\infty} \big[ 1 - F(s) \big]\, ds$. Since $F$ is continuous, $G'(a) = F(a) - \big[ 1 - F(a) \big] = 2F(a) - 1$ for every $a$.

*Compare with Example 2.2.6.* Under squared error, the best constant is the mean, $\mathrm{E}X$. Under absolute error, it is the median.

---

**6. Moments and variance (adapted from Exercises 2.23 and 2.24).**

**(a)** $\mathcal{X} = (-1, 1)$, and $g(x) = x^2$ is monotone on $(-1, 0)$ and on $(0, 1)$, each with image $(0, 1)$. By Theorem 2.1.8 (as in Example 2.1.7),

$$
f_Y(y) = \frac{1}{2\sqrt{y}} \Big[ f(\sqrt{y}) + f(-\sqrt{y}) \Big] = \frac{1}{2\sqrt{y}} \left[ \frac{1 + \sqrt{y}}{2} + \frac{1 - \sqrt{y}}{2} \right] = \frac{1}{2\sqrt{y}}, \qquad 0 < y < 1.
$$

The asymmetric part of $f$ cancels: $Y$ has the same distribution as $U^2$ with $U \sim$ uniform(0, 1). Then

$$
\mathrm{E}Y = \int_0^1 \frac{y}{2\sqrt{y}}\, dy = \frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3}, \qquad
\mathrm{E}Y^2 = \int_0^1 \frac{y^2}{2\sqrt{y}}\, dy = \frac{1}{2} \cdot \frac{2}{5} = \frac{1}{5},
$$

$$
\mathrm{Var}\, Y = \frac{1}{5} - \frac{1}{9} = \frac{4}{45}.
$$

*Check:* $\mathrm{E}Y = \mathrm{E}X^2 = \int_{-1}^1 x^2 \frac{1 + x}{2}\, dx = \frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3}$, since the $x^3$ term integrates to 0.

**(b)** For $a > 0$,

$$
\mathrm{E}X = \int_0^1 a x^a\, dx = \frac{a}{a + 1}, \qquad \mathrm{E}X^2 = \int_0^1 a x^{a + 1}\, dx = \frac{a}{a + 2},
$$

so

$$
\mathrm{Var}\, X = \frac{a}{a + 2} - \frac{a^2}{(a + 1)^2} = \frac{a \big[ (a + 1)^2 - a(a + 2) \big]}{(a + 2)(a + 1)^2} = \frac{a}{(a + 2)(a + 1)^2}.
$$

- **As $a \to \infty$:** $\mathrm{E}X \to 1$ and $\mathrm{Var}\, X \to 0$. The cdf $F(x) = x^a \to 0$ for every $x < 1$, so the mass piles up at 1.
- **As $a \to 0$:** $\mathrm{E}X \to 0$ and $\mathrm{Var}\, X \to 0$. Now $F(x) = x^a \to 1$ for every $x > 0$, so the mass piles up at 0.

In both limits the distribution concentrates at a single point, which is why the variance goes to 0. The variance is largest for intermediate $a$ (for example, $a = 1$ is uniform(0, 1), with variance $\frac{1}{12}$).

---

**7. Moment generating functions (adapted from Exercises 2.25 and 2.30).**

**(a)(i)** For $t \ne 0$,

$$
M_X(t) = \int_0^c \frac{1}{c} e^{tx}\, dx = \frac{e^{ct} - 1}{ct},
$$

and $M_X(0) = 1$. This is finite for every $t$, since the support is bounded. (The formula tends to 1 as $t \to 0$.)

**(a)(ii)** Integrating by parts, $\int_0^c x e^{tx}\, dx = \frac{c e^{ct}}{t} - \frac{e^{ct} - 1}{t^2}$ for $t \ne 0$. So

$$
M_X(t) = \frac{2}{c^2} \left[ \frac{c e^{ct}}{t} - \frac{e^{ct} - 1}{t^2} \right] = \frac{2 \big[ (ct - 1) e^{ct} + 1 \big]}{c^2 t^2}, \qquad t \ne 0,
$$

and $M_X(0) = 1$. Again this is finite for every $t$.

**(a)(iii)** First take $\alpha = 0$, $\beta = 1$: $Z$ has pdf $\frac{1}{2} e^{-\lvert z \rvert}$. Then

$$
M_Z(t) = \frac{1}{2} \int_0^{\infty} e^{-(1 - t) z}\, dz + \frac{1}{2} \int_{-\infty}^0 e^{(1 + t) z}\, dz = \frac{1}{2} \cdot \frac{1}{1 - t} + \frac{1}{2} \cdot \frac{1}{1 + t} = \frac{1}{1 - t^2}.
$$

The first integral is finite only for $t < 1$ and the second only for $t > -1$, so $M_Z(t)$ exists for $\lvert t \rvert < 1$.

For general $\alpha$ and $\beta$, $X = \alpha + \beta Z$ has pdf $\frac{1}{\beta} f_Z\big( (x - \alpha)/\beta \big) = \frac{1}{2\beta} e^{-\lvert x - \alpha \rvert / \beta}$ by Theorem 2.1.5. By Theorem 2.3.15,

$$
M_X(t) = e^{\alpha t} M_Z(\beta t) = \frac{e^{\alpha t}}{1 - \beta^2 t^2}, \qquad \lvert t \rvert < \frac{1}{\beta}.
$$

**(b)** For $\lvert t \rvert < 1$, $M_Z(t) = 1 + t^2 + t^4 + \cdots$. By Theorem 2.3.7, $\mathrm{E}Z^n$ is $n!$ times the coefficient of $t^n$, so

$$
\mathrm{E}Z = 0, \qquad \mathrm{E}Z^2 = 2! \cdot 1 = 2, \qquad \mathrm{Var}\, Z = 2.
$$

(Directly: $M_Z'(t) = \frac{2t}{(1 - t^2)^2}$, so $M_Z'(0) = 0$; and $M_Z''(t) = \frac{2}{(1 - t^2)^2} + \frac{8t^2}{(1 - t^2)^3}$, so $M_Z''(0) = 2$.) Since $X = \alpha + \beta Z$,

$$
\mathrm{E}X = \alpha, \qquad \mathrm{Var}\, X = \beta^2 \mathrm{Var}\, Z = 2\beta^2.
$$

(Alternatively, with $S(t) = \log M_X(t) = \alpha t - \log(1 - \beta^2 t^2)$: $S'(0) = \alpha$ and $S''(0) = 2\beta^2$.)

**(c)** **$X$ and $-X$ are identically distributed.** For every $y$, substituting $u = -x$ and using $f_X(-u) = f_X(u)$,

$$
P(-X \le y) = P(X \ge -y) = \int_{-y}^{\infty} f_X(x)\, dx = \int_{-\infty}^{y} f_X(-u)\, du = \int_{-\infty}^{y} f_X(u)\, du = F_X(y).
$$

So $-X$ and $X$ have the same cdf, and by Theorem 1.5.10 they are identically distributed.

**$M_X$ is symmetric about 0.** Since $-X$ has the same distribution as $X$, it has the same mgf. So, wherever $M_X$ exists,

$$
M_X(-t) = \mathrm{E}e^{-tX} = \mathrm{E}e^{t(-X)} = M_{-X}(t) = M_X(t).
$$

*Check with (iii):* with $\alpha = 0$, $f$ is even and $M_X(t) = \frac{1}{1 - \beta^2 t^2}$, which is indeed an even function of $t$. (With $\alpha \ne 0$, the factor $e^{\alpha t}$ breaks the symmetry, as it should: the pdf is then symmetric about $\alpha$, not about 0.)

---

**8. Five moments are not enough (adapted from Exercise 2.34).**

**(a)** *Moments of $X$.* Let $\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$, so $\phi'(x) = -x \phi(x)$. All moments of $X$ are finite, because $\lvert x \rvert^n \phi(x)$ is integrable for every $n$. For $n \ge 2$, integrate by parts with $u = x^{n - 1}$ and $dv = x \phi(x)\, dx = -d\phi$:

$$
\mathrm{E}X^n = \int_{-\infty}^{\infty} x^{n - 1} \cdot x \phi(x)\, dx = \Big[ -x^{n - 1} \phi(x) \Big]_{-\infty}^{\infty} + (n - 1) \int_{-\infty}^{\infty} x^{n - 2} \phi(x)\, dx = (n - 1)\, \mathrm{E}X^{n - 2},
$$

since $x^{n - 1} \phi(x) \to 0$ as $x \to \pm\infty$. Starting from $\mathrm{E}X^0 = 1$ and $\mathrm{E}X = 0$ (the integrand $x \phi(x)$ is odd and integrable),

$$
\mathrm{E}X^2 = 1, \quad \mathrm{E}X^3 = 0, \quad \mathrm{E}X^4 = 3, \quad \mathrm{E}X^5 = 0, \quad \mathrm{E}X^6 = 15.
$$

*Moments of $Y$.* For odd $r$, $\mathrm{E}Y^r = \frac{1}{6} (\sqrt{3})^r + \frac{1}{6} (-\sqrt{3})^r = 0$. For even $r$,

$$
\mathrm{E}Y^r = 2 \cdot \frac{1}{6} \cdot 3^{r/2} = 3^{r/2 - 1}, \qquad \text{so } \mathrm{E}Y^2 = 1, \quad \mathrm{E}Y^4 = 3.
$$

So $\mathrm{E}X^r = \mathrm{E}Y^r$ for $r = 1, 2, 3, 4, 5$.

**(b)** $\mathrm{E}X^6 = 15$, but $\mathrm{E}Y^6 = 3^2 = 9$. The sixth moments differ.

**(c)** For every $t$,

$$
M_Y(t) = \frac{2}{3} + \frac{1}{6} e^{\sqrt{3} t} + \frac{1}{6} e^{-\sqrt{3} t} = \frac{2}{3} + \frac{1}{3} \cosh\big( \sqrt{3}\, t \big).
$$

Expanding both mgfs in powers of $t$ shows exactly where they part ways:

$$
\begin{aligned}
M_Y(t) &= 1 + \frac{t^2}{2} + \frac{t^4}{8} + \frac{t^6}{80} + \cdots, \\
M_X(t) = e^{t^2/2} &= 1 + \frac{t^2}{2} + \frac{t^4}{8} + \frac{t^6}{48} + \cdots.
\end{aligned}
$$

The coefficients of $t^n$ are $\mathrm{E}X^n / n!$ and $\mathrm{E}Y^n / n!$. They agree up to $t^5$ and differ at $t^6$ ($\frac{15}{720} = \frac{1}{48}$ vs. $\frac{9}{720} = \frac{1}{80}$). So $M_X(t) \ne M_Y(t)$ for all small $t \ne 0$, and $X$ and $Y$ have different distributions ($Y$ is discrete, $X$ is continuous).

*No contradiction with Theorem 2.3.11.* Part (a) of the theorem needs **all** moments to agree (and bounded support, which $X$ does not have). Part (b) needs the mgfs to agree on a whole neighborhood of 0. Here only the first five moments agree, and the mgfs differ near 0. In general, finitely many moments do not determine a distribution.

---

**9. (Exercise 2.39(c, d))**

**(a)** For $0 < t < 1$, use **Leibniz's Rule** (Theorem 2.4.1) with $f(x, t) = x^{-2}$, $a(t) = t$, and $b(t) = 1$. The limits are finite and differentiable, and $f$ is continuous on $[t, 1]$ and does not depend on $t$, so $\frac{\partial}{\partial t} f = 0$. Then

$$
\frac{d}{dt} \int_t^1 \frac{1}{x^2}\, dx = f(1, t) \cdot 0 - f(t, t) \cdot 1 + \int_t^1 0\, dx = -\frac{1}{t^2}.
$$

*Check:* $\int_t^1 x^{-2}\, dx = \frac{1}{t} - 1$, whose derivative is $-\frac{1}{t^2}$.

**(b)** The range of integration is infinite, so Leibniz's Rule does not apply. We use **Corollary 2.4.4**. Let $f(x, t) = (x - t)^{-2}$ for $x > 1$ and $t < 1$. It is differentiable in $t$, with

$$
\frac{\partial}{\partial t} f(x, t) = \frac{2}{(x - t)^3}.
$$

*Dominating function.* Fix $t < 1$ and let $\delta_0 = \frac{1 - t}{2} > 0$, so that $t + \delta_0 < 1$. For every $t'$ with $\lvert t' - t \rvert \le \delta_0$ and every $x > 1$, we have $x - t' \ge x - (t + \delta_0) > 0$. Hence

$$
\left\lvert \left. \frac{\partial}{\partial t} f(x, t) \right\rvert_{t = t'} \right\rvert = \frac{2}{(x - t')^3} \le \frac{2}{(x - t - \delta_0)^3} =: g(x, t),
$$

which is condition (2.4.4). The bound is integrable:

$$
\int_1^{\infty} g(x, t)\, dx = \left[ -\frac{1}{(x - t - \delta_0)^2} \right]_1^{\infty} = \frac{1}{(1 - t - \delta_0)^2} < \infty.
$$

(Define $f$ and $g$ to be 0 for $x \le 1$ to match the corollary's integral over $(-\infty, \infty)$.) So we may differentiate under the integral sign:

$$
\frac{d}{dt} \int_1^{\infty} \frac{dx}{(x - t)^2} = \int_1^{\infty} \frac{2}{(x - t)^3}\, dx = \left[ -\frac{1}{(x - t)^2} \right]_1^{\infty} = \frac{1}{(1 - t)^2}.
$$

*Check:* $\int_1^{\infty} (x - t)^{-2}\, dx = \frac{1}{1 - t}$, whose derivative is $\frac{1}{(1 - t)^2}$.

*Why $\delta_0$ matters.* The bound $g$ must work for all $t'$ near $t$ at once. Choosing $\delta_0 < 1 - t$ keeps $t'$ away from 1, so $x - t'$ stays bounded away from 0 on $x > 1$.
