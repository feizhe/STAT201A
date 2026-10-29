---
layout: page
title: Week 5 Discussion
---

**Covers:** the probability integral transformation and expected values (Lecture 4.2); moments, variance, and mgfs (Lecture 5.1); what the mgf determines.

---

### Problem 1 (The probability integral transformation)

Let $X$ have pdf

$$
f_X(x) =
\begin{cases}
\dfrac{x - 1}{2} & 1 < x < 3 \\[2ex]
0 & \text{otherwise.}
\end{cases}
$$

**(a)** Find the cdf $F_X(x)$. Then find a monotone function $u(x)$ such that the random variable $Y = u(X)$ has a uniform(0, 1) distribution. Verify your answer directly, by computing $P(Y \le y)$ for $0 < y < 1$. *Hint:* Theorem 2.1.10.

**(b)** Now go the other way. Let $V \sim$ uniform(0, 1). Find a function $h$ such that $h(V)$ has the same distribution as $X$, and check that $P(h(V) \le x) = F_X(x)$ for $1 < x < 3$. How would you use this to simulate $X$ on a computer?

**(c)** Find $\mathrm{E}X$ in two ways:

- directly from $f_X$, by (2.2.4);
- as $\mathrm{E}\,h(V)$, using your answer to (b) and the uniform pdf.

Then use the fact that $\mathrm{E}F_X(X) = \frac{1}{2}$ to find $\mathrm{E}(X - 1)^2$ **without** integrating against $f_X$, and deduce $\mathrm{Var}\, X$.

**(d)** Theorem 2.1.10 needs a *continuous* cdf. Let $X$ be uniform on $\lbrace 1, 2, 3 \rbrace$, that is, $P(X = k) = \frac{1}{3}$ for $k = 1, 2, 3$, and let $Y = F_X(X)$.

- Find the pmf of $Y$ and $\mathrm{E}Y$. Is $Y$ uniform(0, 1)?
- Show that $F_Y(y) \le y$ for all $0 < y < 1$, with strict inequality for some $y$. (C&B say $Y$ is *stochastically greater* than a uniform(0, 1).)
- Where does the proof of Theorem 2.1.10 use continuity of $F_X$, and why does that step fail here?

<details markdown="1">
<summary>Show answer</summary>

**(a)** For $1 < x < 3$,

$$
F_X(x) = \int_1^x \frac{s - 1}{2}\, ds = \frac{(x - 1)^2}{4},
$$

with $F_X(x) = 0$ for $x \le 1$ and $F_X(x) = 1$ for $x \ge 3$.

- By Theorem 2.1.10, take $u(x) = F_X(x) = \frac{(x - 1)^2}{4}$. It is increasing on $(1, 3)$.
- *Direct check.* For $0 < y < 1$, and since $X > 1$,

  $$
  \begin{aligned}
  P(Y \le y) &= P\left( \frac{(X - 1)^2}{4} \le y \right) = P\big( X \le 1 + 2\sqrt{y} \big) \\
  &= F_X\big( 1 + 2\sqrt{y} \big) = \frac{(2\sqrt{y})^2}{4} = y.
  \end{aligned}
  $$

**(b)** Invert $F_X$: solving $v = \frac{(x - 1)^2}{4}$ for $x \in (1, 3)$ gives $F_X^{-1}(v) = 1 + 2\sqrt{v}$. So take $h(v) = 1 + 2\sqrt{v}$. For $1 < x < 3$,

$$
P\big( 1 + 2\sqrt{V} \le x \big) = P\left( V \le \frac{(x - 1)^2}{4} \right) = \frac{(x - 1)^2}{4} = F_X(x).
$$

To simulate $X$: generate $V$ from uniform(0, 1) and return $1 + 2\sqrt{V}$. This is the inverse cdf method from Lecture 4.2.

**(c)**

- **Directly:** substituting $s = x - 1$,

  $$
  \mathrm{E}X = \int_1^3 x \cdot \frac{x - 1}{2}\, dx = \frac{1}{2} \int_0^2 (s + 1) s\, ds = \frac{1}{2} \left( \frac{8}{3} + 2 \right) = \frac{7}{3}.
  $$

- **Through $V$:** $X$ has the same distribution as $1 + 2\sqrt{V}$, so

  $$
  \mathrm{E}X = \mathrm{E}\big( 1 + 2\sqrt{V} \big) = 1 + 2 \int_0^1 v^{1/2}\, dv = 1 + 2 \cdot \frac{2}{3} = \frac{7}{3}.
  $$

- **Second moment for free:** $F_X(X) = \frac{(X - 1)^2}{4}$, and $F_X(X) \sim$ uniform(0, 1) by (a). So

  $$
  \mathrm{E}(X - 1)^2 = 4\, \mathrm{E}F_X(X) = 4 \cdot \frac{1}{2} = 2.
  $$

- **Variance:** by Theorem 2.3.4 (a shift does not change the variance) and (2.3.1),

  $$
  \mathrm{Var}\, X = \mathrm{Var}(X - 1) = \mathrm{E}(X - 1)^2 - \big( \mathrm{E}(X - 1) \big)^2 = 2 - \left( \frac{4}{3} \right)^2 = \frac{2}{9}.
  $$

*Check:* $\int_1^3 (x - 1)^2 \frac{x - 1}{2}\, dx = \frac{1}{2} \cdot \frac{2^4}{4} = 2$. ✓

**(d)**

- $F_X(1) = \frac{1}{3}$, $F_X(2) = \frac{2}{3}$, and $F_X(3) = 1$. So $Y$ takes the values $\frac{1}{3}, \frac{2}{3}, 1$, each with probability $\frac{1}{3}$, and

  $$
  \mathrm{E}Y = \frac{1}{3} \left( \frac{1}{3} + \frac{2}{3} + 1 \right) = \frac{2}{3} \ne \frac{1}{2}.
  $$

  $Y$ is discrete, so it is certainly not uniform(0, 1).
- For $0 < y < 1$, $F_Y(y) = \frac{\lfloor 3y \rfloor}{3} \le y$. The inequality is strict except at $y = \frac{1}{3}$ and $y = \frac{2}{3}$. For example, $F_Y\left( \frac{1}{2} \right) = \frac{1}{3} < \frac{1}{2}$.
- The last step of the proof, $F_X\big( F_X^{-1}(y) \big) = y$, is labeled "continuity of $F_X$." It needs every level $y \in (0, 1)$ to be hit by $F_X$. Here $F_X$ jumps from $\frac{1}{3}$ to $\frac{2}{3}$ at $x = 2$, so no $x$ has $F_X(x) = \frac{1}{2}$. By (2.1.13), $F_X^{-1}\left( \frac{1}{2} \right) = 2$ and $F_X(2) = \frac{2}{3} \ne \frac{1}{2}$. The jumps push $F_X(X)$ upward, which is why $Y$ is stochastically greater than a uniform.

</details>

---

### Problem 2 (MGF)

Let $X$ have the geometric pmf

$$
P(X = x) = p(1 - p)^x, \qquad x = 0, 1, 2, \dots, \quad 0 < p < 1.
$$

$X$ counts the failures before the first success in independent trials with success probability $p$. (Week 4 Discussion Problem 2 used $p = \frac{1}{3}$.)

**(a)** Verify that

$$
M_X(t) = \frac{p}{1 - (1 - p)e^t}.
$$

For which $t$ does the sum converge? Does the mgf exist in the sense of Definition 2.3.6?

**(b)** Use Theorem 2.3.7 to find $\mathrm{E}X$, $\mathrm{E}X^2$, and $\mathrm{Var}\, X$.

**(c)** (C&B Exercise 2.32) Let $S(t) = \log M_X(t)$, for any random variable $X$ with an mgf. Show that

$$
S'(0) = \mathrm{E}X \quad \text{and} \quad S''(0) = \mathrm{Var}\, X.
$$

Then redo (b) for the geometric with $S(t)$. Which way is less work?

<details markdown="1">
<summary>Show answer</summary>

**(a)** Write $q = 1 - p$. Then

$$
M_X(t) = \sum_{x=0}^{\infty} e^{tx} p q^x = p \sum_{x=0}^{\infty} \big( q e^t \big)^x = \frac{p}{1 - q e^t},
$$

provided $q e^t < 1$, that is, $t < -\log(1 - p)$.

- Since $0 < q < 1$, the bound $-\log(1 - p)$ is **positive**. So the sum is finite on $(-h, h)$ with $h = -\log(1 - p)$, and the mgf exists.
- For $t \ge -\log(1 - p)$ the terms do not go to 0, and the sum is infinite. Like the gamma mgf (Example 2.3.8), it is finite only on one side of a cutoff, but the cutoff is away from 0.

**(b)** Let $D(t) = 1 - q e^t$, so $D(0) = p$. Then

$$
\begin{aligned}
M_X'(t) &= \frac{p q e^t}{D(t)^2}, \\
M_X''(t) &= \frac{p q e^t}{D(t)^2} + \frac{2 p q^2 e^{2t}}{D(t)^3}.
\end{aligned}
$$

At $t = 0$:

$$
\begin{aligned}
\mathrm{E}X &= M_X'(0) = \frac{pq}{p^2} = \frac{q}{p}, \\
\mathrm{E}X^2 &= M_X''(0) = \frac{q}{p} + \frac{2q^2}{p^2} = \frac{q(2 - p)}{p^2}.
\end{aligned}
$$

By (2.3.1),

$$
\mathrm{Var}\, X = \frac{q(2 - p)}{p^2} - \frac{q^2}{p^2} = \frac{q(2 - p - q)}{p^2} = \frac{1 - p}{p^2}.
$$

**(c)** By the chain rule, $S'(t) = \dfrac{M_X'(t)}{M_X(t)}$, and by the quotient rule

$$
S''(t) = \frac{M_X''(t) M_X(t) - \big( M_X'(t) \big)^2}{M_X(t)^2}.
$$

Since $M_X(0) = 1$, $M_X'(0) = \mathrm{E}X$, and $M_X''(0) = \mathrm{E}X^2$,

$$
S'(0) = \mathrm{E}X, \qquad S''(0) = \mathrm{E}X^2 - (\mathrm{E}X)^2 = \mathrm{Var}\, X.
$$

For the geometric, $S(t) = \log p - \log(1 - q e^t)$, so

$$
S'(t) = \frac{q e^t}{1 - q e^t}, \qquad S''(t) = \frac{q e^t}{(1 - q e^t)^2}.
$$

- At $t = 0$: $S'(0) = \frac{q}{p}$ and $S''(0) = \frac{q}{p^2}$, as in (b).
- $S$ is less work. The logarithm turns the constant $p$ into an additive term that disappears when differentiated, and it gives $\mathrm{Var}\, X$ directly, with no subtraction step.

</details>

---

### Problem 3 (MGF)

**(a)** Each function below is claimed to be the mgf of some random variable $X$. Identify the distribution of $X$, or explain why no such $X$ exists. *Hint:* Theorems 2.3.11 and 2.3.15, and Examples 2.3.8 and 2.3.9.

- **(i)** $M(t) = \left( \frac{1}{3} + \frac{2}{3} e^t \right)^5$, for all $t$.
- **(ii)** $M(t) = \dfrac{e^{2t}}{1 - 3t}$, for $t < \frac{1}{3}$.
- **(iii)** $M(t) = \dfrac{t}{1 - t}$, for $\lvert t \rvert < 1$.

**(b)** For $n = 2, 3, \dots$, let $X_n$ have the geometric pmf of Problem 2 with $p = \frac{1}{n}$, and let $Y_n = X_n / n$. Think of trials run every $\frac{1}{n}$ seconds, each succeeding with probability $\frac{1}{n}$, so that $Y_n$ is the waiting time, in seconds, before the first success.

- Use Problem 2(a) and Theorem 2.3.15 to find $M_{Y_n}(t)$.
- Show that $M_{Y_n}(t) \to \frac{1}{1 - t}$ for every $t < 1$, and say what Theorem 2.3.12 lets you conclude about $F_{Y_n}$. *Hint:* $n\big( e^{t/n} - 1 \big) \to t$.

<details markdown="1">
<summary>Show answer</summary>

**(a)** By Theorem 2.3.11(b), once we find one distribution with a given mgf, it is the only one.

- **(i)** This is Example 2.3.9 with $n = 5$ and $p = \frac{2}{3}$, so $X \sim$ binomial(5, $\frac{2}{3}$).
- **(ii)** $\frac{1}{1 - 3t}$, for $t < \frac{1}{3}$, is the exponential(3) mgf (Example 2.3.8 with $\alpha = 1$, $\beta = 3$). By Theorem 2.3.15 with $a = 1$ and $b = 2$, $e^{2t} M_Z(t)$ is the mgf of $Z + 2$. So $X$ has the same distribution as $Z + 2$, with $Z \sim$ exponential(3), and

  $$
  f_X(x) = \frac{1}{3} e^{-(x - 2)/3}, \qquad x > 2.
  $$

- **(iii)** No such $X$ exists. Every mgf has $M_X(0) = \mathrm{E}e^{0} = 1$, but here $M(0) = 0$.

**(b)**

- With $a = \frac{1}{n}$ and $b = 0$ in Theorem 2.3.15, $M_{Y_n}(t) = M_{X_n}(t/n)$, so

  $$
  M_{Y_n}(t) = \frac{1/n}{1 - \left( 1 - \frac{1}{n} \right) e^{t/n}} = \frac{1}{n\left[ 1 - \left( 1 - \frac{1}{n} \right) e^{t/n} \right]}.
  $$

  By Problem 2(a), this is finite for $t < -n\log(1 - 1/n)$, and $-n\log(1 - 1/n) > 1$. So $M_{Y_n}(t)$ is defined for every $t < 1$.
- Expanding the denominator,

  $$
  \begin{aligned}
  n\left[ 1 - \left( 1 - \frac{1}{n} \right) e^{t/n} \right] &= -n\big( e^{t/n} - 1 \big) + e^{t/n} \\
  &\to -t + 1.
  \end{aligned}
  $$

  Hence $M_{Y_n}(t) \to \frac{1}{1 - t}$ for every $t < 1$, which includes the neighborhood $\lvert t \rvert < 1$ of 0.
- $\frac{1}{1 - t}$ is the mgf of the exponential(1) distribution, with cdf $F(y) = 1 - e^{-y}$, $y \ge 0$. Since this $F$ is continuous, Theorem 2.3.12 gives $F_{Y_n}(y) \to 1 - e^{-y}$ for **every** $y$. Waiting for a rare success in many quick trials takes an approximately exponential time.

</details>
