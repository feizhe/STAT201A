---
layout: page
---

# STAT 201A Homework 2

Show all work and justify every step from definitions, axioms, or results proved in class. You may discuss the problems with classmates, but the solutions you submit must be written by you. Pdf files of typed or hand-written-and-scan answers are both acceptable.

**Covers:** counting, conditional probability and Bayes' rule, independence, random variables, cdfs, pmfs, and pdfs (Weeks 2–3, C&B §§1.2.3–1.6).

---

**1. (Exercise 1.21)** A closet contains $n$ pairs of shoes. If $2r$ shoes are chosen at random $(2r < n)$, what is the probability that there will be no matching pair in the sample?

**2. (Exercise 1.33)** Suppose that 5% of men and .25% of women are color-blind. A person is chosen at random and that person is color-blind. What is the probability that the person is male? (Assume males and females to be in equal numbers.)

**3. (Exercise 1.38)** Prove each of the following statements. (Assume that any conditioning event has positive probability.)

- **(a)** If $P(B) = 1$, then $P(A \mid B) = P(A)$ for any $A$.
- **(b)** If $A \subset B$, then $P(B \mid A) = 1$ and $P(A \mid B) = P(A)/P(B)$.
- **(c)** If $A$ and $B$ are mutually exclusive, then

  $$
  P(A \mid A \cup B) = \frac{P(A)}{P(A) + P(B)}.
  $$

- **(d)** $P(A \cap B \cap C) = P(A \mid B \cap C) P(B \mid C) P(C)$.

**4. (Exercise 1.39)** A pair of events $A$ and $B$ cannot be simultaneously *mutually exclusive* and *independent*. Prove that if $P(A) > 0$ and $P(B) > 0$, then:

- **(a)** If $A$ and $B$ are mutually exclusive, they cannot be independent.
- **(b)** If $A$ and $B$ are independent, they cannot be mutually exclusive.

**5. Two medical tests.** A disease has prevalence 1%. A screening test is positive with probability 0.95 for a person with the disease and with probability 0.10 for a person without it. A randomly chosen person takes the test twice. Let $D$ = "the person has the disease" and $T_i$ = "test $i$ is positive," $i = 1, 2$. Assume the two results are independent **given** the disease status: $P(T_1 \cap T_2 \mid D) = P(T_1 \mid D) P(T_2 \mid D)$, and the same with $D^c$ in place of $D$.

- **(a)** Find $P(D \mid T_1)$.
- **(b)** Find $P(D \mid T_1 \cap T_2)$.
- **(c)** Show that you get the same answer as (b) by applying Bayes' rule to test 2 alone, using your answer to (a) as the "prior" probability of $D$. Explain why this works.
- **(d)** Are $T_1$ and $T_2$ independent? Compute $P(T_1 \cap T_2)$ and $P(T_1) P(T_2)$, and explain in words why "independent given $D$" does not imply "independent."

**6. (Exercise 1.47)** Prove that the following functions are cdfs.

- **(a)** $\frac{1}{2} + \frac{1}{\pi} \tan^{-1}(x)$, $x \in (-\infty, \infty)$
- **(b)** $e^{-e^{-x}}$, $x \in (-\infty, \infty)$
- **(c)** the function defined in (1.5.6)

For each, state whether the corresponding random variable is continuous, discrete, or neither (Definition 1.5.7).

**7. A cdf with jumps.** Let $X$ have cdf

$$
F(x) =
\begin{cases}
0 & x < 0 \\
x/4 & 0 \le x < 1 \\
1/2 & 1 \le x < 2 \\
1 - \frac{1}{4} e^{-(x - 2)} & x \ge 2.
\end{cases}
$$

Write $F(a^-) = \lim_{x \uparrow a} F(x)$.

- **(a)** For any random variable with cdf $F$ and any $a < b$, show that $P(a < X \le b) = F(b) - F(a)$ and $P(X = a) = F(a) - F(a^-)$. *Hint:* $\lbrace X < a \rbrace = \bigcup_{n=1}^{\infty} \lbrace X \le a - \frac{1}{n} \rbrace$. You may use the fact that if $A_1 \subset A_2 \subset \cdots$, then $P\big( \bigcup_{n} A_n \big) = \lim_{n \to \infty} P(A_n)$.
- **(b)** Check that $F$ satisfies the three conditions of Theorem 1.5.3. Is $X$ continuous, discrete, or neither?
- **(c)** Find $P(X = 1)$, $P(X = 2)$, $P(\frac{1}{2} < X < 2)$, $P(X > 3)$, and $P(X \ge 1 \mid X \le 2)$.
- **(d)** Describe a two-stage experiment that produces a random variable with cdf $F$: first flip a fair coin, then, depending on the result, draw $X$ from a discrete distribution or from a continuous one. Specify both distributions.

**8. (Exercise 1.55)** An electronic device has lifetime denoted by $T$. The device has value $V = 5$ if it fails before time $t = 3$; otherwise, it has value $V = 2T$. Find the cdf of $V$, if $T$ has pdf

$$
f_T(t) = \frac{1}{1.5} e^{-t/(1.5)}, \qquad t > 0.
$$

**9. A pmf and a pdf with the same tail.**

- **(a)** Let $f_X(k) = \dfrac{c}{k(k+1)}$ for $k = 1, 2, \dots$, and $0$ otherwise. Find the constant $c$ that makes $f_X$ a pmf. *Hint:* $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$.
- **(b)** Find the cdf $F_X(x)$ for **every** real $x$, and sketch it. Find $P(X > n)$ for $n = 1, 2, \dots$
- **(c)** Let $f_Y(y) = \dfrac{c}{y^2}$ for $y > 1$, and $0$ otherwise. Find $c$ so that $f_Y$ is a pdf, and find $F_Y(y)$ and $P(Y \ge n)$.
- **(d)** Show that $\lfloor Y \rfloor$, the integer part of $Y$, has the same distribution as $X$. *Hint:* find $P(\lfloor Y \rfloor = k)$ by writing the event $\lbrace \lfloor Y \rfloor = k \rbrace$ in terms of $Y$.
- **(e)** A pmf always satisfies $f_X(x) \le 1$. Explain why. Does a pdf have to satisfy $f_Y(y) \le 1$? Prove it or give a counterexample.
