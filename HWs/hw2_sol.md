---
layout: page
---

# STAT 201A Homework 2 Solutions

Theorem numbers refer to Casella & Berger (C&B). The tools used most often are

- **Definition 1.3.2 (conditional probability).** If $P(B) > 0$, then $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$.
- **Law of total probability.** If $A_1, A_2, \dots$ partition $S$, then $P(B) = \sum_i P(B \mid A_i) P(A_i)$. Combined with Definition 1.3.2, this gives **Bayes' rule** (Theorem 1.3.5).
- **Theorem 1.5.3.** $F$ is a cdf if and only if (a) $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to \infty} F(x) = 1$; (b) $F$ is nondecreasing; and (c) $F$ is right-continuous.

---

**1. (Exercise 1.21)** *A closet contains $n$ pairs of shoes. If $2r$ shoes are chosen at random $(2r < n)$, what is the probability that there will be no matching pair in the sample?*

- **Sample space.** "At random" means every subset of $2r$ of the $2n$ shoes is equally likely, so there are $\binom{2n}{2r}$ outcomes.
- **Favorable outcomes.** No matching pair means the $2r$ shoes come from $2r$ **different** pairs.
  - Choose which $2r$ of the $n$ pairs are used: $\binom{n}{2r}$ ways.
  - From each chosen pair, choose the left or the right shoe: $2^{2r}$ ways.

Hence

$$
P(\text{no matching pair}) = \frac{\binom{n}{2r}\, 2^{2r}}{\binom{2n}{2r}}.
$$

*Check:* with $n = 5$ and $r = 2$, the formula gives $\frac{5 \cdot 16}{210} = \frac{8}{21}$, which matches a direct enumeration of all $\binom{10}{4} = 210$ subsets.

*Alternative (ordered draws).* Draw the shoes one at a time. The first can be anything; the second must avoid the first one's mate; and so on:

$$
\frac{2n}{2n} \cdot \frac{2n - 2}{2n - 1} \cdot \frac{2n - 4}{2n - 2} \cdots \frac{2n - 2(2r - 1)}{2n - 2r + 1},
$$

which simplifies to the same answer.

---

**2. (Exercise 1.33)** *5% of men and .25% of women are color-blind. A person chosen at random is color-blind. What is the probability that the person is male?*

Let $M$ = "male" and $C$ = "color-blind." We are given $P(M) = P(M^c) = \frac{1}{2}$, $P(C \mid M) = 0.05$, and $P(C \mid M^c) = 0.0025$.

- **Total probability:**

  $$
  \begin{aligned}
  P(C) &= P(C \mid M) P(M) + P(C \mid M^c) P(M^c) \\
  &= 0.05(0.5) + 0.0025(0.5) = 0.02625.
  \end{aligned}
  $$

- **Bayes' rule:**

  $$
  P(M \mid C) = \frac{P(C \mid M) P(M)}{P(C)} = \frac{0.025}{0.02625} = \frac{20}{21} \approx 0.952.
  $$

Color blindness is 20 times as common among men, so about 20 of every 21 color-blind people are men.

---

**3. (Exercise 1.38)** *Assume that any conditioning event has positive probability.*

**(a)** *If $P(B) = 1$, then $P(A \mid B) = P(A)$ for any $A$.*

- $P(B^c) = 1 - P(B) = 0$. Since $A \cap B^c \subset B^c$, monotonicity (Theorem 1.2.9(c)) gives $0 \le P(A \cap B^c) \le P(B^c) = 0$.
- $A$ is the disjoint union of $A \cap B$ and $A \cap B^c$, so $P(A) = P(A \cap B) + P(A \cap B^c) = P(A \cap B)$.
- Therefore $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)} = \dfrac{P(A)}{1} = P(A)$. $\square$

**(b)** *If $A \subset B$, then $P(B \mid A) = 1$ and $P(A \mid B) = P(A)/P(B)$.*

If $A \subset B$, then $A \cap B = A$. So

$$
\begin{aligned}
P(B \mid A) &= \frac{P(A \cap B)}{P(A)} = \frac{P(A)}{P(A)} = 1, \\
P(A \mid B) &= \frac{P(A \cap B)}{P(B)} = \frac{P(A)}{P(B)}. \quad \square
\end{aligned}
$$

**(c)** *If $A$ and $B$ are mutually exclusive, then $P(A \mid A \cup B) = \dfrac{P(A)}{P(A) + P(B)}$.*

- $A \subset A \cup B$, so $A \cap (A \cup B) = A$.
- $A \cap B = \emptyset$, so by Axiom 3, $P(A \cup B) = P(A) + P(B)$.

Therefore

$$
P(A \mid A \cup B) = \frac{P\big( A \cap (A \cup B) \big)}{P(A \cup B)} = \frac{P(A)}{P(A) + P(B)}. \quad \square
$$

**(d)** *$P(A \cap B \cap C) = P(A \mid B \cap C)\, P(B \mid C)\, P(C)$.*

By Definition 1.3.2, applied twice,

$$
\begin{aligned}
P(A \mid B \cap C)\, P(B \mid C)\, P(C) &= \frac{P(A \cap B \cap C)}{P(B \cap C)} \cdot \frac{P(B \cap C)}{P(C)} \cdot P(C) \\
&= P(A \cap B \cap C).
\end{aligned}
$$

The assumption that conditioning events have positive probability ($P(B \cap C) > 0$, $P(C) > 0$) is what makes the cancellations legal. $\square$

---

**4. (Exercise 1.39)** *Suppose $P(A) > 0$ and $P(B) > 0$.* Then $P(A) P(B) > 0$.

**(a)** If $A$ and $B$ are mutually exclusive, then $A \cap B = \emptyset$, so $P(A \cap B) = 0 \ne P(A) P(B)$. Hence $A$ and $B$ are not independent. $\square$

**(b)** If $A$ and $B$ are independent, then $P(A \cap B) = P(A) P(B) > 0$. Since $P(\emptyset) = 0$, the event $A \cap B$ cannot be empty, so $A$ and $B$ are not mutually exclusive. $\square$

(Part (b) is the contrapositive of part (a).) The intuition: if $A$ and $B$ are mutually exclusive, learning that $A$ occurred tells you for certain that $B$ did not, which is as far from "no information" as possible.

---

**5. Two medical tests.** We are given $P(D) = 0.01$, $P(T_i \mid D) = 0.95$, and $P(T_i \mid D^c) = 0.10$, with $T_1$ and $T_2$ independent given $D$ and given $D^c$.

**(a)** By total probability,

$$
P(T_1) = 0.95(0.01) + 0.10(0.99) = 0.1085,
$$

and by Bayes' rule

$$
P(D \mid T_1) = \frac{P(T_1 \mid D) P(D)}{P(T_1)} = \frac{0.0095}{0.1085} = \frac{19}{217} \approx 0.0876.
$$

Even after a positive test, the chance of disease is under 9%, because healthy people are 99 times as common as sick ones.

**(b)** By conditional independence,

$$
P(T_1 \cap T_2 \mid D) = 0.95^2 = 0.9025, \qquad P(T_1 \cap T_2 \mid D^c) = 0.10^2 = 0.01.
$$

So by total probability,

$$
P(T_1 \cap T_2) = 0.9025(0.01) + 0.01(0.99) = 0.018925,
$$

and by Bayes' rule

$$
P(D \mid T_1 \cap T_2) = \frac{0.009025}{0.018925} = \frac{361}{757} \approx 0.477.
$$

**(c)** Use $p' = P(D \mid T_1) = \frac{19}{217}$ as the prior and apply Bayes' rule to test 2 alone:

$$
\frac{0.95\, p'}{0.95\, p' + 0.10\, (1 - p')} = \frac{0.95(19)}{0.95(19) + 0.10(198)} = \frac{18.05}{37.85} = \frac{361}{757},
$$

the same answer as (b).

*Why this works.* Bayes' rule within the world where $T_1$ has occurred reads

$$
\begin{aligned}
&P(D \mid T_1 \cap T_2) \\
&\quad = \frac{P(T_2 \mid D \cap T_1)\, P(D \mid T_1)}{P(T_2 \mid D \cap T_1)\, P(D \mid T_1) + P(T_2 \mid D^c \cap T_1)\, P(D^c \mid T_1)}.
\end{aligned}
$$

Conditional independence lets us drop $T_1$ from the likelihoods:

$$
P(T_2 \mid D \cap T_1) = \frac{P(T_1 \cap T_2 \mid D)}{P(T_1 \mid D)} = \frac{P(T_1 \mid D) P(T_2 \mid D)}{P(T_1 \mid D)} = P(T_2 \mid D),
$$

and likewise with $D^c$. Once the disease status is known, the first result says nothing more about the second, so updating one test at a time gives the same posterior as updating on both at once. Yesterday's posterior is today's prior.

**(d)**

$$
P(T_1 \cap T_2) = 0.018925, \qquad P(T_1) P(T_2) = 0.1085^2 \approx 0.01177.
$$

These differ, so $T_1$ and $T_2$ are **not** independent. In fact $P(T_2 \mid T_1) = 0.018925 / 0.1085 \approx 0.174 > 0.1085 = P(T_2)$.

*In words:* both tests depend on the same hidden cause, the disease status. If we do not know that status, a positive first test makes disease more likely, which in turn makes a positive second test more likely. Conditioning on $D$ (or $D^c$) fixes the common cause and removes the link, which is why the tests are independent given $D$ but not unconditionally.

---

**6. (Exercise 1.47)** We check the three conditions of Theorem 1.5.3, then classify $X$ by Definition 1.5.7.

**(a)** $F(x) = \frac{1}{2} + \frac{1}{\pi} \tan^{-1}(x)$.

- **Limits:** $\tan^{-1}(x) \to \mp \frac{\pi}{2}$ as $x \to \mp\infty$, so $F(x) \to \frac{1}{2} - \frac{1}{2} = 0$ and $F(x) \to \frac{1}{2} + \frac{1}{2} = 1$.
- **Nondecreasing:** $F'(x) = \dfrac{1}{\pi(1 + x^2)} > 0$.
- **Right-continuous:** $F$ is continuous everywhere.

$F$ is a continuous cdf, so $X$ is **continuous**. (This is the Cauchy distribution, with pdf $F'(x)$.)

**(b)** $F(x) = e^{-e^{-x}}$.

- **Limits:** as $x \to -\infty$, $e^{-x} \to \infty$, so $F(x) \to e^{-\infty} = 0$. As $x \to \infty$, $e^{-x} \to 0$, so $F(x) \to e^0 = 1$.
- **Nondecreasing:** $F'(x) = e^{-x} e^{-e^{-x}} > 0$.
- **Right-continuous:** $F$ is a composition of continuous functions, so it is continuous.

$X$ is **continuous**, with pdf $f(x) = e^{-x} e^{-e^{-x}}$. (This is the Gumbel, or extreme value, distribution.)

**(c)** The function (1.5.6) is, for some $0 < \epsilon < 1$,

$$
F_Y(y) =
\begin{cases}
\dfrac{1 - \epsilon}{1 + e^{-y}} & y < 0 \\[2ex]
\epsilon + \dfrac{1 - \epsilon}{1 + e^{-y}} & y \ge 0.
\end{cases}
$$

- **Limits:** as $y \to -\infty$, $1 + e^{-y} \to \infty$, so $F_Y(y) \to 0$. As $y \to \infty$, $F_Y(y) \to \epsilon + (1 - \epsilon) = 1$.
- **Nondecreasing:** $\frac{1}{1 + e^{-y}}$ is increasing, so each piece is increasing. At the break, the left limit is $F_Y(0^-) = \frac{1 - \epsilon}{2}$, and $F_Y(0) = \epsilon + \frac{1 - \epsilon}{2} = \frac{1 + \epsilon}{2}$, which is larger. So $F_Y$ never decreases.
- **Right-continuous:** each piece is continuous, and $F_Y(0)$ is given by the right-hand piece, so $\lim_{y \downarrow 0} F_Y(y) = F_Y(0)$.

$F_Y$ jumps by $\epsilon$ at $0$, so it is **not continuous**. It increases strictly between jumps, so it is **not a step function**. Hence $Y$ is **neither** continuous nor discrete: it has $P(Y = 0) = \epsilon$ plus a continuous part of total probability $1 - \epsilon$.

---

**7. A cdf with jumps.**

**(a)**

- $\lbrace X \le b \rbrace$ is the disjoint union of $\lbrace X \le a \rbrace$ and $\lbrace a < X \le b \rbrace$. So $F(b) = F(a) + P(a < X \le b)$, that is, $P(a < X \le b) = F(b) - F(a)$.
- Let $A_n = \lbrace X \le a - \frac{1}{n} \rbrace$. Then $A_1 \subset A_2 \subset \cdots$, and $\bigcup_n A_n = \lbrace X < a \rbrace$: if $X(s) < a$, then $X(s) \le a - \frac{1}{n}$ for all large $n$, and conversely every $A_n$ lies inside $\lbrace X < a \rbrace$. By continuity from below,

  $$
  P(X < a) = \lim_{n \to \infty} P(A_n) = \lim_{n \to \infty} F\left( a - \frac{1}{n} \right) = F(a^-).
  $$

  The last step holds because $F$ is nondecreasing and bounded, so its left limit exists and equals the limit along any sequence increasing to $a$.
- $\lbrace X \le a \rbrace$ is the disjoint union of $\lbrace X < a \rbrace$ and $\lbrace X = a \rbrace$, so $P(X = a) = F(a) - F(a^-)$. $\square$

**(b)**

- **Limits:** $F(x) = 0$ for all $x < 0$, and $1 - \frac{1}{4} e^{-(x - 2)} \to 1$ as $x \to \infty$.
- **Nondecreasing:** each piece is nondecreasing ($x/4$ increases, $\frac{1}{2}$ is flat, and $1 - \frac{1}{4}e^{-(x-2)}$ increases). At the breaks:
  - at $0$: $F(0^-) = 0 = F(0)$;
  - at $1$: $F(1^-) = \frac{1}{4} < \frac{1}{2} = F(1)$, a jump up of $\frac{1}{4}$;
  - at $2$: $F(2^-) = \frac{1}{2} < \frac{3}{4} = F(2)$, a jump up of $\frac{1}{4}$.
- **Right-continuous:** each piece is continuous, and every interval in the definition is closed on the left, so $F(a)$ equals the right limit at each break.

$F$ has jumps at 1 and 2, so it is not continuous. It increases on $(0, 1)$ and $(2, \infty)$, so it is not a step function. Hence $X$ is **neither** continuous nor discrete.

**(c)** Using (a):

$$
\begin{aligned}
P(X = 1) &= F(1) - F(1^-) = \tfrac{1}{2} - \tfrac{1}{4} = \tfrac{1}{4}, \\
P(X = 2) &= F(2) - F(2^-) = \tfrac{3}{4} - \tfrac{1}{2} = \tfrac{1}{4}, \\
P\left( \tfrac{1}{2} < X < 2 \right) &= F(2^-) - F\left( \tfrac{1}{2} \right) = \tfrac{1}{2} - \tfrac{1}{8} = \tfrac{3}{8}, \\
P(X > 3) &= 1 - F(3) = \tfrac{1}{4} e^{-1} \approx 0.092.
\end{aligned}
$$

For the conditional probability, $\lbrace X \ge 1 \rbrace \cap \lbrace X \le 2 \rbrace = \lbrace 1 \le X \le 2 \rbrace$, so

$$
P(X \ge 1 \mid X \le 2) = \frac{F(2) - F(1^-)}{F(2)} = \frac{\frac{3}{4} - \frac{1}{4}}{\frac{3}{4}} = \frac{2}{3}.
$$

Watch the endpoints: $P(\frac{1}{2} < X < 2)$ excludes the jump at 2, and $P(X \ge 1)$ includes the jump at 1.

**(d)** The jumps carry total mass $\frac{1}{4} + \frac{1}{4} = \frac{1}{2}$, and the increasing parts carry the other $\frac{1}{2}$: slope $\frac{1}{4}$ on $(0, 1)$ gives $\frac{1}{4}$, and density $\frac{1}{4}e^{-(x-2)}$ on $(2, \infty)$ gives $\frac{1}{4}$. So the coin is fair. Flip a fair coin:

- **Heads:** draw $X$ from the discrete distribution $P(X = 1) = P(X = 2) = \frac{1}{2}$.
- **Tails:** draw $X$ from the continuous density

  $$
  g(x) =
  \begin{cases}
  \frac{1}{2} & 0 < x < 1 \\[1ex]
  \frac{1}{2} e^{-(x - 2)} & x > 2 \\[1ex]
  0 & \text{otherwise,}
  \end{cases}
  $$

  which integrates to $\frac{1}{2} + \frac{1}{2} = 1$.

*Check* that $F = \frac{1}{2} F_{\text{disc}} + \frac{1}{2} F_{\text{cont}}$ (total probability over the coin):

- $0 \le x < 1$: $\frac{1}{2}(0) + \frac{1}{2} \cdot \frac{x}{2} = \frac{x}{4}$;
- $1 \le x < 2$: $\frac{1}{2} \cdot \frac{1}{2} + \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{2}$;
- $x \ge 2$: $\frac{1}{2}(1) + \frac{1}{2} \left[ \frac{1}{2} + \frac{1}{2}\left( 1 - e^{-(x-2)} \right) \right] = 1 - \frac{1}{4} e^{-(x - 2)}$.

---

**8. (Exercise 1.55)** $T$ is exponential with mean 1.5, so $P(T \le t) = 1 - e^{-t/1.5}$ for $t > 0$.

$V = 5$ if $T < 3$, and $V = 2T \ge 6$ if $T \ge 3$. So $V$ takes the value 5 or a value in $[6, \infty)$.

- **$v < 5$:** $V$ is never below 5, so $F_V(v) = 0$.
- **$5 \le v < 6$:** $V \le v$ happens only when $V = 5$, that is, when $T < 3$:

  $$
  F_V(v) = P(T < 3) = 1 - e^{-3/1.5} = 1 - e^{-2}.
  $$

- **$v \ge 6$:** $V \le v$ happens when $T < 3$, or when $3 \le T$ and $2T \le v$. These are disjoint and together make up $\lbrace T \le v/2 \rbrace$:

  $$
  F_V(v) = P(T < 3) + P\left( 3 \le T \le \frac{v}{2} \right) = P\left( T \le \frac{v}{2} \right) = 1 - e^{-v/3}.
  $$

Hence

$$
F_V(v) =
\begin{cases}
0 & v < 5 \\
1 - e^{-2} & 5 \le v < 6 \\
1 - e^{-v/3} & v \ge 6.
\end{cases}
$$

- $F_V$ jumps by $1 - e^{-2} \approx 0.865$ at $v = 5$, which is $P(V = 5)$.
- $F_V$ is flat on $[5, 6)$, since $V$ never lands there, and it is **continuous** at $v = 6$: $1 - e^{-6/3} = 1 - e^{-2}$.
- Like Problem 7, $V$ is neither discrete nor continuous.

---

**9. A pmf and a pdf with the same tail.**

**(a)** The partial sums telescope:

$$
\sum_{k=1}^{N} \frac{c}{k(k+1)} = c \sum_{k=1}^{N} \left( \frac{1}{k} - \frac{1}{k+1} \right) = c \left( 1 - \frac{1}{N + 1} \right) \xrightarrow{N \to \infty} c.
$$

A pmf must sum to 1, so $c = 1$. With $c = 1$, $f_X(k) > 0$ for every $k$, so nonnegativity also holds.

**(b)** For $x < 1$, $F_X(x) = 0$. For $k \le x < k + 1$ with $k \ge 1$, the same telescoping gives $F_X(x) = \sum_{j=1}^{k} \frac{1}{j(j+1)} = 1 - \frac{1}{k + 1}$. So

$$
F_X(x) =
\begin{cases}
0 & x < 1 \\
1 - \dfrac{1}{\lfloor x \rfloor + 1} & x \ge 1.
\end{cases}
$$

- **Sketch:** a right-continuous step function, equal to $\frac{1}{2}$ on $[1, 2)$, $\frac{2}{3}$ on $[2, 3)$, $\frac{3}{4}$ on $[3, 4)$, and so on, rising toward 1. The jump at each integer $k \ge 1$ has height $\frac{1}{k(k+1)}$. Each step includes its left endpoint (solid dot) and excludes its right endpoint (open dot).
- **Tail:** $P(X > n) = 1 - F_X(n) = \dfrac{1}{n + 1}$.

**(c)** Normalization:

$$
\int_1^{\infty} \frac{c}{y^2}\, dy = c \left[ -\frac{1}{y} \right]_1^{\infty} = c, \quad \text{so } c = 1.
$$

Then $F_Y(y) = 0$ for $y \le 1$, and for $y > 1$,

$$
F_Y(y) = \int_1^{y} \frac{1}{t^2}\, dt = 1 - \frac{1}{y}.
$$

Since $Y$ is continuous, $P(Y = n) = 0$, so for $n \ge 1$, $P(Y \ge n) = 1 - F_Y(n) = \dfrac{1}{n}$.

**(d)** $Y > 1$, so $\lfloor Y \rfloor$ takes the values $1, 2, \dots$ For $k \ge 1$, $\lbrace \lfloor Y \rfloor = k \rbrace = \lbrace k \le Y < k + 1 \rbrace$, so

$$
P(\lfloor Y \rfloor = k) = F_Y(k + 1) - F_Y(k) = \frac{1}{k} - \frac{1}{k + 1} = \frac{1}{k(k + 1)} = f_X(k).
$$

$\lfloor Y \rfloor$ and $X$ have the same support and the same probabilities, so they have the same distribution. $\square$

**(e)**

- **A pmf is a probability.** $f_X(x) = P(X = x)$, and $\lbrace X = x \rbrace \subset S$, so $f_X(x) \le P(S) = 1$ by monotonicity.
- **A pdf need not be $\le 1$.** A density value is not a probability; only its integral over a set is. For example, the uniform$(0, \frac{1}{2})$ pdf

  $$
  f(y) =
  \begin{cases}
  2 & 0 < y < \frac{1}{2} \\
  0 & \text{otherwise}
  \end{cases}
  $$

  is nonnegative and integrates to $2 \cdot \frac{1}{2} = 1$, yet equals 2 everywhere on its support.
- A pdf can even be **unbounded**: $f(y) = \frac{1}{2\sqrt{y}}$ on $(0, 1)$ integrates to $\sqrt{y}\, \big\rvert_0^1 = 1$ but $f(y) \to \infty$ as $y \downarrow 0$.
