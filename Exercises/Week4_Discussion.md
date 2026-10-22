---
layout: page
title: Week 4 Discussion
---


### Problem 1 (High-water marks: from a cdf to a pdf, and a change of units; C&B Exercise 1.53)

A certain river floods every year. Suppose that the low-water mark is set at 1 and the high-water mark $Y$ has distribution function

$$
F_Y(y) = P(Y \le y) = 1 - \frac{1}{y^2}, \qquad 1 \le y < \infty,
$$

and $F_Y(y) = 0$ for $y < 1$.

**(a)** Verify that $F_Y(y)$ is a cdf, by checking the three conditions of Theorem 1.5.3. Is $Y$ continuous, discrete, or neither?

**(b)** Find $f_Y(y)$, the pdf of $Y$. Find $P(Y > 2)$ twice: once from $F_Y$, and once by integrating $f_Y$.

**(c)** If the low-water mark is reset at 0 and we use a unit of measurement that is $\frac{1}{10}$ of that given previously, the high-water mark becomes $Z = 10(Y - 1)$. Find $F_Z(z)$. *Hint:* write the event $\lbrace Z \le z \rbrace$ as an event about $Y$.

**(d)** Find $f_Z(z)$ in two ways: by differentiating your answer to (c), and by Theorem 2.1.5. What are $\mathcal{Y}$ and $\mathcal{Z}$?

<details markdown="1">
<summary>Show answer</summary>

**(a)** We check the three conditions of Theorem 1.5.3.

- **Limits.** $F_Y(y) = 0$ for all $y < 1$, so $\lim_{y \to -\infty} F_Y(y) = 0$. Also $\lim_{y \to \infty} \left( 1 - y^{-2} \right) = 1$.
- **Nondecreasing.** On $[1, \infty)$, $\frac{d}{dy} \left( 1 - y^{-2} \right) = 2y^{-3} > 0$, and $F_Y$ is constant (0) for $y < 1$. At the junction, $F_Y(1) = 1 - 1 = 0$, so $F_Y$ does not jump down.
- **Right-continuous.** Each piece is continuous, and the two pieces meet at $y = 1$, since $\lim_{y \uparrow 1} F_Y(y) = 0 = F_Y(1)$.

$F_Y$ is in fact continuous everywhere, so $Y$ is a **continuous** random variable (Definition 1.5.7).

**(b)** $f_Y(y) = \frac{d}{dy} F_Y(y) = \frac{2}{y^3}$ for $y > 1$, and $f_Y(y) = 0$ for $y < 1$.

- From the cdf: $P(Y > 2) = 1 - F_Y(2) = \frac{1}{4}$.
- From the pdf: $\int_2^{\infty} 2y^{-3}\, dy = -y^{-2} \Big|_2^{\infty} = \frac{1}{4}$.

**(c)** Since $Z = 10(Y - 1)$, for $z \ge 0$,

$$
\begin{aligned}
F_Z(z) = P(Z \le z) &= P\big( 10(Y - 1) \le z \big) = P\left( Y \le 1 + \frac{z}{10} \right) \\
&= 1 - \frac{1}{(1 + z/10)^2} = 1 - \frac{100}{(10 + z)^2},
\end{aligned}
$$

and $F_Z(z) = 0$ for $z < 0$.

**(d)**

- **Differentiating:** $f_Z(z) = \frac{d}{dz} \left( 1 - 100 (10 + z)^{-2} \right) = \frac{200}{(10 + z)^3}$, for $z > 0$.
- **Theorem 2.1.5:** $g(y) = 10(y - 1)$ is increasing, with $g^{-1}(z) = 1 + z/10$ and $\frac{d}{dz} g^{-1}(z) = \frac{1}{10}$. So

  $$
  \begin{aligned}
  f_Z(z) &= f_Y\left( 1 + \frac{z}{10} \right) \cdot \frac{1}{10} = \frac{2}{(1 + z/10)^3} \cdot \frac{1}{10} \\
  &= \frac{2 \cdot 1000}{(10 + z)^3} \cdot \frac{1}{10} = \frac{200}{(10 + z)^3}.
  \end{aligned}
  $$

- The supports are $\mathcal{Y} = (1, \infty)$ and $\mathcal{Z} = g(\mathcal{Y}) = (0, \infty)$.

Notice the factor $\frac{1}{10}$. Measuring in smaller units stretches the axis by a factor of 10, so the density must be 10 times lower for the total area to stay 1.

</details>

---

### Problem 2 (A discrete transformation; C&B Exercise 2.3)

Suppose $X$ has the geometric pmf $f_X(x) = \frac{1}{3} \left( \frac{2}{3} \right)^x$, $x = 0, 1, 2, \dots$.

**(a)** Verify that $f_X$ is a pmf (Theorem 1.6.5). Then find the cdf $F_X(x)$ for **every** real $x$. *Hint:* use the partial sum of the geometric series, as in (1.5.4).

**(b)** Determine the probability distribution of $Y = X/(X + 1)$. Note that here both $X$ and $Y$ are discrete random variables. To specify the probability distribution of $Y$, specify its pmf.

- What is $\mathcal{Y}$?
- Is $g(x) = x/(x + 1)$ one-to-one on $\mathcal{X}$? What is $g^{-1}(y)$?

**(c)** Find $P(Y \le 0.7)$.

**(d)** All the values of $Y$ lie in $[0, 1)$, and they pile up near 1. Is $Y$ still a discrete random variable? Explain using Definition 1.5.7.

<details markdown="1">
<summary>Show answer</summary>

**(a)** $f_X(x) \ge 0$, and

$$
\sum_{x=0}^{\infty} \frac{1}{3} \left( \frac{2}{3} \right)^x = \frac{1}{3} \cdot \frac{1}{1 - 2/3} = 1.
$$

For an integer $k \ge 0$, the partial sum gives

$$
P(X \le k) = \sum_{x=0}^{k} \frac{1}{3} \left( \frac{2}{3} \right)^x = \frac{1}{3} \cdot \frac{1 - (2/3)^{k+1}}{1 - 2/3} = 1 - \left( \frac{2}{3} \right)^{k+1}.
$$

Between integers the cdf is flat, so for every real $x$,

$$
F_X(x) =
\begin{cases}
0 & x < 0 \\
1 - (2/3)^{\lfloor x \rfloor + 1} & x \ge 0,
\end{cases}
$$

where $\lfloor x \rfloor$ is the largest integer $\le x$. This is a step function, with a jump of size $f_X(k)$ at each $k = 0, 1, 2, \dots$.

**(b)**

- $\mathcal{Y} = \lbrace g(x) : x \in \mathcal{X} \rbrace = \left\lbrace 0, \frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \dots \right\rbrace = \left\lbrace \frac{k}{k+1} : k = 0, 1, 2, \dots \right\rbrace$.
- $g(x) = \frac{x}{x+1} = 1 - \frac{1}{x+1}$ is increasing, hence one-to-one. Solving $y = \frac{x}{x+1}$ gives $g^{-1}(y) = \frac{y}{1 - y}$, so each $g^{-1}(y)$ is a single point.

The sum over $g^{-1}(y)$ has only one term, so

$$
f_Y(y) = f_X\left( \frac{y}{1 - y} \right) = \frac{1}{3} \left( \frac{2}{3} \right)^{y/(1-y)}, \qquad y = 0, \tfrac{1}{2}, \tfrac{2}{3}, \tfrac{3}{4}, \dots,
$$

and $f_Y(y) = 0$ otherwise. Equivalently, $P\left( Y = \frac{k}{k+1} \right) = \frac{1}{3} \left( \frac{2}{3} \right)^k$.

There is no Jacobian factor here. A discrete transformation only *relabels* the points: the probabilities move with them unchanged.

**(c)** Transform the event:

$$
\lbrace Y \le 0.7 \rbrace = \left\lbrace X \le \frac{0.7}{0.3} \right\rbrace = \lbrace X \le 2.33\ldots \rbrace = \lbrace X \le 2 \rbrace.
$$

So $P(Y \le 0.7) = F_X(2) = 1 - (2/3)^3 = \frac{19}{27} \approx 0.704$. This is also Theorem 2.1.3(a): $F_Y(y) = F_X(g^{-1}(y))$ for increasing $g$, which does not require $X$ to be continuous.

**(d)** Yes. $\mathcal{Y}$ is countable, and $F_Y$ is a step function: it jumps by $\frac{1}{3}(2/3)^k$ at each $\frac{k}{k+1}$ and is flat in between. The jumps get closer together near 1, but there are still only countably many of them. Being "discrete" is about the cdf being a step function, not about the values being spread apart or being integers.

</details>

---

### Problem 3 (When the pieces don't match: a piecewise-monotone transformation; C&B Exercise 2.7)

Let $X$ have pdf $f_X(x) = \frac{2}{9}(x + 1)$, $-1 \le x \le 2$, and let $Y = X^2$.

**(a)** Sketch $f_X$ and the graph of $g(x) = x^2$ on $[-1, 2]$. What is $\mathcal{Y}$? Split $\mathcal{X}$ into the two pieces $(-1, 0)$ and $(0, 2)$ on which $g$ is monotone, and find the image of each piece. Which condition of Theorem 2.1.8 fails? (This is why C&B note that Theorem 2.1.8 is not directly applicable in this problem.)

**(b)** Use the cdf method to find $F_Y(y)$. *Hint:* the event $\lbrace X^2 \le y \rbrace = \lbrace -\sqrt{y} \le X \le \sqrt{y} \rbrace$ looks different depending on whether $-\sqrt{y}$ is inside the support of $X$. Treat $0 \le y < 1$ and $1 \le y \le 4$ separately.

**(c)** Differentiate to find the pdf of $Y$. Check that it integrates to 1. Is it bounded?

**(d)** Show that Theorem 2.1.8 remains valid if the sets $A_0, A_1, \dots, A_k$ *contain* $\mathcal{X}$, and apply the extension to solve part (c) using $A_0 = \emptyset$, $A_1 = (-2, 0)$, and $A_2 = (0, 2)$. *Hint:* outside the support, $f_X = 0$.

<details markdown="1">
<summary>Show answer</summary>

**(a)** $\mathcal{Y} = [0, 4]$.

- On $(-1, 0)$, $g$ is decreasing, with image $(0, 1)$.
- On $(0, 2)$, $g$ is increasing, with image $(0, 4)$.

The images differ, so condition **iii** of Theorem 2.1.8 (the same set $\mathcal{Y}$ for each piece) fails. Values $y \in (0, 1)$ have two pre-images, $\pm\sqrt{y}$. Values $y \in (1, 4)$ have only one, $+\sqrt{y}$, because $-\sqrt{y} < -1$ lies outside the support.

**(b)**

- **$0 \le y < 1$:** both endpoints $\pm\sqrt{y}$ lie in $[-1, 1]$, so

  $$
  \begin{aligned}
  F_Y(y) &= P(-\sqrt{y} \le X \le \sqrt{y}) = \int_{-\sqrt{y}}^{\sqrt{y}} \frac{2}{9}(x + 1)\, dx \\
  &= \frac{2}{9} \cdot 2\sqrt{y} = \frac{4\sqrt{y}}{9}.
  \end{aligned}
  $$

  The $x$ term integrates to 0 over the symmetric interval.
- **$1 \le y \le 4$:** now $-\sqrt{y} \le -1$, so the left endpoint is cut off by the support:

  $$
  F_Y(y) = P(-1 \le X \le \sqrt{y}) = \frac{1}{9}(x + 1)^2 \Big|_{-1}^{\sqrt{y}} = \frac{(\sqrt{y} + 1)^2}{9}.
  $$

- $F_Y(y) = 0$ for $y < 0$ and $F_Y(y) = 1$ for $y > 4$.

*Checks:* both formulas give $\frac{4}{9}$ at $y = 1$, which is $P(-1 \le X \le 1)$. The second gives $1$ at $y = 4$.

**(c)** Differentiating,

$$
f_Y(y) =
\begin{cases}
\dfrac{2}{9\sqrt{y}} & 0 < y < 1 \\[2ex]
\dfrac{1}{9}\left( 1 + \dfrac{1}{\sqrt{y}} \right) & 1 < y < 4 \\[2ex]
0 & \text{otherwise.}
\end{cases}
$$

*Check:*

$$
\int_0^1 \frac{2}{9\sqrt{y}}\, dy + \int_1^4 \frac{1}{9}\left( 1 + y^{-1/2} \right) dy = \frac{4}{9} + \frac{1}{9}(3 + 2) = 1.
$$

$f_Y$ is **unbounded** near $y = 0$, yet it still integrates to 1. Compare Check your understanding 1 in Lecture 4.1.

**(d)** The proof of Theorem 2.1.8 only uses the pieces to split the event $\lbrace Y \le y \rbrace$ into parts on which $g$ is monotone. Any $x$ outside $\mathcal{X}$ has $f_X(x) = 0$, so it adds nothing to any integral. Enlarging the pieces to $A_1 = (-2, 0)$ and $A_2 = (0, 2)$ therefore changes nothing, and now each piece maps onto the same set $(0, 4)$, so condition iii holds. With $g_1^{-1}(y) = -\sqrt{y}$, $g_2^{-1}(y) = \sqrt{y}$, and $\left\lvert \frac{d}{dy} g_i^{-1}(y) \right\rvert = \frac{1}{2\sqrt{y}}$,

$$
f_Y(y) = \frac{1}{2\sqrt{y}} \Big( f_X(-\sqrt{y}) + f_X(\sqrt{y}) \Big), \qquad 0 < y < 4.
$$

- For $0 < y < 1$: $\frac{1}{2\sqrt{y}} \cdot \frac{2}{9} \big( (1 - \sqrt{y}) + (1 + \sqrt{y}) \big) = \frac{2}{9\sqrt{y}}$.
- For $1 < y < 4$: $f_X(-\sqrt{y}) = 0$, because $-\sqrt{y} < -1$. So $f_Y(y) = \frac{1}{2\sqrt{y}} \cdot \frac{2}{9}(\sqrt{y} + 1) = \frac{1}{9}\left( 1 + \frac{1}{\sqrt{y}} \right)$.

This matches (c). **Lesson:** the formula is the same everywhere. What changes with $y$ is *which pre-images land inside the support*, which is exactly what the cdf method in (b) makes visible.

</details>
