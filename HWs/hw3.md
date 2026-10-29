---
layout: page
---

# STAT 201A Homework 3

Show all work and justify every step from definitions, axioms, or results proved in class. You may discuss the problems with classmates, but the solutions you submit must be written by you. Pdf files of typed or hand-written-and-scan answers are both acceptable.

**Covers:** distributions of functions of a random variable, the probability integral transformation, expected values, moments and variance, moment generating functions, and differentiating under an integral sign (Weeks 4–5, C&B §§2.1–2.4).

---

**1. (Exercise 2.2(c))** Let $X$ have pdf

$$
f_X(x) = \frac{1}{\sigma^2} x e^{-(x/\sigma)^2/2}, \qquad 0 < x < \infty, \quad \sigma^2 \text{ a positive constant.}
$$

Find the pdf of $Y = e^X$, and show that it integrates to 1.

**2. (Exercise 2.6(b))** Let $X$ have pdf $f_X(x) = \frac{3}{8} (x + 1)^2$, $-1 < x < 1$. Find the pdf of $Y = 1 - X^2$, and show that it integrates to 1.

**3. An inverse cdf with a jump (adapted from Exercise 2.8(c)).** Show that

$$
F_X(x) =
\begin{cases}
e^x/4 & x < 0 \\
1 - e^{-x}/4 & x \ge 0
\end{cases}
$$

is a cdf, and find $F_X^{-1}(y) = \inf \lbrace x : F_X(x) \ge y \rbrace$ (2.1.13) for $0 < y < 1$. Then let $V \sim$ uniform(0, 1) and $X = F_X^{-1}(V)$: find $P(X = 0)$ from the distribution of $V$, and check that it equals the jump of $F_X$ at 0. Is $F_X(X)$ uniform(0, 1)? Explain why this does not contradict Theorem 2.1.10.

**4. Expectations from tail probabilities (adapted from Exercises 2.14(a) and 2.16).** Let $X$ be a continuous, nonnegative random variable [$f_X(x) = 0$ for $x < 0$]. Show that

$$
\mathrm{E}X = \int_0^{\infty} \big[ 1 - F_X(x) \big]\, dx.
$$

*Hint:* write $x = \int_0^x dt$. You may interchange the order of integration, since the integrand is nonnegative. Then use this to find the mean duration $\mathrm{E}T$ of a telephone call, in minutes, if $P(T > t) = 0.8 e^{-t/2} + 0.2 e^{-t/10}$ for $t \ge 0$.

**5. Medians (Exercises 2.17 and 2.18).** A *median* of a distribution is a value $m$ such that $P(X \le m) \ge \frac{1}{2}$ and $P(X \ge m) \ge \frac{1}{2}$. (If $X$ is continuous, $m$ satisfies $\int_{-\infty}^m f(x)\, dx = \int_m^{\infty} f(x)\, dx = \frac{1}{2}$.)

- **(a)** Find the median of the following distributions:
  - **(i)** $f(x) = 3x^2$, $0 < x < 1$
  - **(ii)** $f(x) = \dfrac{1}{\pi (1 + x^2)}$, $-\infty < x < \infty$
- **(b)** Show that if $X$ is a continuous random variable with $\mathrm{E}\lvert X \rvert < \infty$, then

  $$
  \min_a \mathrm{E}\lvert X - a \rvert = \mathrm{E}\lvert X - m \rvert,
  $$

  where $m$ is the median of $X$. *Hint:* split $\mathrm{E}\lvert X - a \rvert$ into an integral over $x < a$ and one over $x > a$, write it in terms of $F_X(a)$, $\int_{-\infty}^a x f(x)\, dx$, and $\int_a^{\infty} x f(x)\, dx$, and differentiate in $a$ using the fundamental theorem of calculus. Compare with Example 2.2.6.

**6. Moments and variance (adapted from Exercises 2.23 and 2.24).**

- **(a)** Let $X$ have pdf $f(x) = \frac{1}{2} (1 + x)$, $-1 < x < 1$. Find the pdf of $Y = X^2$, and find $\mathrm{E}Y$ and $\mathrm{Var}\, Y$.
- **(b)** Let $X$ have pdf $f(x) = a x^{a - 1}$, $0 < x < 1$, where $a > 0$. Compute $\mathrm{E}X$ and $\mathrm{Var}\, X$. Find the limits of both as $a \to \infty$ and as $a \to 0$, and explain what they say about where the distribution puts its mass.

**7. Moment generating functions (adapted from Exercises 2.25 and 2.30).**

- **(a)** Find the moment generating function corresponding to each of the following, and say for which $t$ it exists:
  - **(i)** $f(x) = \frac{1}{c}$, $0 < x < c$
  - **(ii)** $f(x) = \frac{2x}{c^2}$, $0 < x < c$
  - **(iii)** $f(x) = \frac{1}{2\beta} e^{-\lvert x - \alpha \rvert / \beta}$, $-\infty < x < \infty$, $-\infty < \alpha < \infty$, $\beta > 0$
- **(b)** Use the mgf in (iii) to find $\mathrm{E}X$ and $\mathrm{Var}\, X$. *Hint:* Theorem 2.3.15 lets you reduce to $\alpha = 0$, $\beta = 1$ first.
- **(c)** (Exercise 2.25) Suppose the pdf $f_X(x)$ is an *even function*: $f_X(x) = f_X(-x)$ for every $x$. Show that $X$ and $-X$ are identically distributed, and that $M_X(t)$ is symmetric about 0. Check this against (iii) with $\alpha = 0$.

**8. Five moments are not enough (adapted from Exercise 2.34).** Let $X \sim \mathrm{N}(0, 1)$, with pdf $f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$, $-\infty < x < \infty$. Define a discrete random variable $Y$ by

$$
P\big( Y = \sqrt{3} \big) = P\big( Y = -\sqrt{3} \big) = \frac{1}{6}, \qquad P(Y = 0) = \frac{2}{3}.
$$

- **(a)** Show that $\mathrm{E}X^r = \mathrm{E}Y^r$ for $r = 1, 2, 3, 4, 5$. *Hint:* for $X$, integrate by parts to show $\mathrm{E}X^n = (n - 1) \mathrm{E}X^{n - 2}$ for $n \ge 2$.
- **(b)** Compare $\mathrm{E}X^6$ and $\mathrm{E}Y^6$.
- **(c)** Find $M_Y(t)$ for all $t$. You may use $M_X(t) = e^{t^2/2}$ (Exercise 2.33(c)). $X$ and $Y$ have different distributions even though their first five moments agree. Explain why this does not contradict Theorem 2.3.11.

**9. (Exercise 2.39(c, d))** In each of the following cases calculate the indicated derivative, justifying all operations. For each, say which result from §2.4 you use (Leibniz's Rule, Theorem 2.4.3, or Corollary 2.4.4) and check its conditions.

- **(a)** $\dfrac{d}{dt} \displaystyle\int_t^1 \frac{1}{x^2}\, dx$, for $0 < t < 1$
- **(b)** $\dfrac{d}{dt} \displaystyle\int_1^{\infty} \frac{1}{(x - t)^2}\, dx$, for $t < 1$
