---
layout: page
title: "Midterm Review: Chapters 1–2"
---

# Midterm Review: Chapters 1–2

**The midterm (Thu. Nov. 5)** covers C&B Chapter 1 and §§2.1–2.3: the lecture notes for Weeks 1–5, and Homeworks 1–3. **Differentiating under an integral sign (§2.4) is not on the midterm.** The exam is closed book; you may bring one page of notes (a cheat sheet) and a calculator.

<!-- This review lists the main topics, the definitions and results you should be able to state and use, and the **way of thinking** behind the standard problems: the questions to ask yourself when you start a problem, and the moves that usually work. It is a map, not a replacement for the notes. Theorem and definition numbers follow C&B. -->

---

# Part I. Probability Theory (Chapter 1, Weeks 1–3)

## 1. Sets and events (§1.1)

**Key definitions.**

- **Sample space** $S$: the set of all possible outcomes (Definition 1.1.1). An **event** is a subset of $S$ (Definition 1.1.2).
- **Set operations:** union $A \cup B$, intersection $A \cap B$, complement $A^c$; commutative, associative, and distributive laws; **DeMorgan's laws** $(A \cup B)^c = A^c \cap B^c$ and $(A \cap B)^c = A^c \cup B^c$ (Theorem 1.1.4). They extend to finite and countable collections.
- **Countable unions and intersections:** $x \in \bigcup_{n} A_n$ if $x \in A_n$ **for some** $n$; $x \in \bigcap_{n} A_n$ if $x \in A_n$ **for all** $n$.
- **Disjoint** (mutually exclusive): $A \cap B = \emptyset$. **Partition:** pairwise disjoint sets whose union is $S$ (Definitions 1.1.5–1.1.6).

## 2. Sigma algebras and the axioms (§1.2.1)

**Key definitions.**

- **Sigma algebra** $\mathcal{B}$ (Definition 1.2.1): contains $\emptyset$; closed under complements; closed under countable unions. Consequences: $S \in \mathcal{B}$, and $\mathcal{B}$ is closed under countable intersections (by DeMorgan).
- **Kolmogorov axioms** (Definition 1.2.4): $P(A) \ge 0$; $P(S) = 1$; if $A_1, A_2, \dots$ are pairwise disjoint, $P\big( \bigcup_i A_i \big) = \sum_i P(A_i)$.
- **Finite $S$** (Theorem 1.2.6): assigning $p_i \ge 0$ with $\sum p_i = 1$ to the outcomes and adding defines a probability function.

## 3. The calculus of probabilities (§1.2.2)

**Key results.**

- $P(\emptyset) = 0$, $P(A) \le 1$, $P(A^c) = 1 - P(A)$ (Theorem 1.2.8).
- $P(B \cap A^c) = P(B) - P(A \cap B)$; $P(A \cup B) = P(A) + P(B) - P(A \cap B)$; if $A \subset B$ then $P(A) \le P(B)$ (Theorem 1.2.9).
- **Partition formula:** $P(A) = \sum_i P(A \cap C_i)$ for a partition $C_1, C_2, \dots$ (Theorem 1.2.11(a)).
- **Boole's inequality:** $P\big( \bigcup_i A_i \big) \le \sum_i P(A_i)$ (Theorem 1.2.11(b)). **Bonferroni's inequality:** $P(A \cap B) \ge P(A) + P(B) - 1$ (1.2.9), and its $n$-event form (1.2.10).

## 4. Counting and equally likely outcomes (§1.2.3)

**Key results.**

- **Fundamental theorem of counting** (Theorem 1.2.14): a job of $k$ tasks done in $n_1, \dots, n_k$ ways can be done in $n_1 \times \cdots \times n_k$ ways.
- **Table 1.2.1** (choose $r$ from $n$):

  | | Without replacement | With replacement |
  |---|---|---|
  | **Ordered** | $\dfrac{n!}{(n-r)!}$ | $n^r$ |
  | **Unordered** | $\dbinom{n}{r}$ | $\dbinom{n+r-1}{r}$ |

- **Multinomial coefficient:** $\dfrac{k!}{k_1! \cdots k_m!}$ arrangements of $k$ objects with $k_j$ identical objects of type $j$.
- **Equally likely outcomes:** $P(A) = N(A)/N(S)$.

## 5. Conditional probability and Bayes' rule (§1.3)

**Key definitions and results.**

- **Conditional probability** (Definition 1.3.2): $P(A \mid B) = P(A \cap B)/P(B)$ for $P(B) > 0$. For fixed $B$, $P(\cdot \mid B)$ satisfies the axioms, so every Week 1 rule holds conditionally, e.g. $P(A^c \mid B) = 1 - P(A \mid B)$.
- **Multiplication (chain) rule:** $P(A_1 \cap \cdots \cap A_n) = P(A_1) P(A_2 \mid A_1) \cdots P(A_n \mid A_1 \cap \cdots \cap A_{n-1})$.
- **Law of total probability:** $P(B) = \sum_i P(B \mid A_i) P(A_i)$ for a partition $A_1, A_2, \dots$
- **Bayes' rule** (Theorem 1.3.5):

  $$
  P(A_i \mid B) = \frac{P(B \mid A_i)\, P(A_i)}{\sum_j P(B \mid A_j)\, P(A_j)}.
  $$

  Prior $P(A_i)$, likelihood $P(B \mid A_i)$, posterior $P(A_i \mid B)$.

## 6. Independence (§1.3)

**Key definitions and results.**

- $A$ and $B$ are **independent** if $P(A \cap B) = P(A) P(B)$ (Definition 1.3.7). Then $A$ and $B^c$, $A^c$ and $B$, and $A^c$ and $B^c$ are also independent (Theorem 1.3.9).
- **Mutual independence** of $A_1, \dots, A_n$ (Definition 1.3.12): the product rule holds for **every** subcollection.

## 7. Random variables and cdfs (§§1.4–1.5)

**Key definitions and results.**

- A **random variable** is a function $X : S \to \mathbb{R}$ (Definition 1.4.1). It induces a probability on its range: $P(X \in A) = P\big( \lbrace s \in S : X(s) \in A \rbrace \big)$.
- **Cdf:** $F_X(x) = P(X \le x)$ for **all** real $x$ (Definition 1.5.1).
- **Theorem 1.5.3:** $F$ is a cdf if and only if (a) $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to \infty} F(x) = 1$; (b) $F$ is nondecreasing; (c) $F$ is right-continuous.
- **Continuous** if $F_X$ is continuous; **discrete** if $F_X$ is a step function (Definition 1.5.7). A cdf can be **neither** (a mix of jumps and continuous increase).
- **Identically distributed** (Definition 1.5.8) if and only if $F_X = F_Y$ everywhere (Theorem 1.5.10). Identically distributed does not mean $X = Y$.
- **Reading probabilities from a cdf:**

  $$
  P(a < X \le b) = F_X(b) - F_X(a), \qquad P(X = a) = F_X(a) - F_X(a^-), \qquad F_X(a^-) = \lim_{x \uparrow a} F_X(x).
  $$

## 8. Pmfs and pdfs (§1.6)

**Key definitions and results.**

- **Pmf:** $f_X(x) = P(X = x)$ (Definition 1.6.1). **Pdf:** $F_X(x) = \int_{-\infty}^x f_X(t)\, dt$ for all $x$ (Definition 1.6.3), so $f_X = F_X'$ where $f_X$ is continuous.
- **Theorem 1.6.5:** $f_X$ is a pmf or pdf if and only if $f_X \ge 0$ and it sums or integrates to 1.
- For continuous $X$, $P(X = x) = 0$, so endpoints don't matter: $P(a < X < b) = P(a \le X \le b) = \int_a^b f_X(x)\, dx$.

---

# Part II. Transformations and Expectations (Chapter 2, Weeks 4–5)

## 9. Distributions of functions of a random variable (§2.1)

**Key definitions and results.**

- **Supports** (2.1.7): $\mathcal{X} = \lbrace x : f_X(x) > 0 \rbrace$ and $\mathcal{Y} = \lbrace g(x) : x \in \mathcal{X} \rbrace$.
- **Discrete $X$:** $f_Y(y) = \sum_{x \in g^{-1}(y)} f_X(x)$.
- **Cdf method** (2.1.4): $F_Y(y) = P(g(X) \le y) = \int_{\lbrace x \in \mathcal{X} : g(x) \le y \rbrace} f_X(x)\, dx$.
- **Monotone $g$** (Theorem 2.1.3): $F_Y(y) = F_X(g^{-1}(y))$ if $g$ is increasing; $F_Y(y) = 1 - F_X(g^{-1}(y))$ if $g$ is decreasing and $X$ is continuous.
- **Change of variables** (Theorem 2.1.5): for monotone $g$,

  $$
  f_Y(y) = f_X\big( g^{-1}(y) \big) \left\lvert \frac{d}{dy} g^{-1}(y) \right\rvert, \qquad y \in \mathcal{Y}.
  $$

- **Piecewise monotone $g$** (Theorem 2.1.8): split $\mathcal{X}$ into pieces $A_1, \dots, A_k$ on which $g$ is monotone with the same image $\mathcal{Y}$, and add the contributions $f_X(g_i^{-1}(y)) \left\lvert \frac{d}{dy} g_i^{-1}(y) \right\rvert$. Example: $Y = X^2$ gives $f_Y(y) = \frac{1}{2\sqrt{y}} \big[ f_X(\sqrt{y}) + f_X(-\sqrt{y}) \big]$ (Example 2.1.7).

## 10. The probability integral transformation (§2.1)

**Key results.**

- **Theorem 2.1.10:** if $F_X$ is continuous, then $F_X(X) \sim$ uniform(0, 1).
- **Inverse cdf** (2.1.13): $F_X^{-1}(y) = \inf \lbrace x : F_X(x) \ge y \rbrace$. If $V \sim$ uniform(0, 1), then $F_X^{-1}(V)$ has cdf $F_X$.

## 11. Expected values (§2.2)

**Key definitions and results.**

- **Definition 2.2.1:** $\mathrm{E}\,g(X) = \int g(x) f_X(x)\, dx$ or $\sum g(x) f_X(x)$, **provided** $\mathrm{E}\lvert g(X) \rvert < \infty$. Otherwise the expectation does not exist (Cauchy, Example 2.2.4).
- **Linearity** (Theorem 2.2.5): $\mathrm{E}\big( a g_1(X) + b g_2(X) + c \big) = a\,\mathrm{E}\,g_1(X) + b\,\mathrm{E}\,g_2(X) + c$; expectation preserves inequalities.
- **But** $\mathrm{E}\,g(X) \ne g(\mathrm{E}X)$ in general.
- **Minimizing distance** (Example 2.2.6): $b = \mathrm{E}X$ minimizes $\mathrm{E}(X - b)^2$.
- **Tail formula** (Exercise 2.14, HW3): for nonnegative continuous $X$, $\mathrm{E}X = \int_0^{\infty} \big[ 1 - F_X(x) \big]\, dx$.

## 12. Moments and variance (§2.3)

**Key definitions and results.**

- **Moments:** $\mu'_n = \mathrm{E}X^n$; **central moments:** $\mu_n = \mathrm{E}(X - \mu)^n$ (Definition 2.3.1).
- **Variance** (Definition 2.3.2): $\mathrm{Var}\, X = \mathrm{E}(X - \mathrm{E}X)^2 = \mathrm{E}X^2 - (\mathrm{E}X)^2$.
- $\mathrm{Var}(aX + b) = a^2 \mathrm{Var}\, X$ (Theorem 2.3.4).
- **Examples to know:** exponential($\lambda$): mean $\lambda$, variance $\lambda^2$; binomial($n$, $p$): mean $np$, variance $np(1 - p)$; Poisson($\lambda$): mean and variance $\lambda$.

## 13. Moment generating functions (§2.3)

**Key definitions and results.**

- **Mgf** (Definition 2.3.6): $M_X(t) = \mathrm{E}e^{tX}$, which must be finite for all $t$ in a **neighborhood of 0**, $-h < t < h$.
- **Moments from the mgf** (Theorem 2.3.7): $\mathrm{E}X^n = M_X^{(n)}(0)$.
- **Linear transformations** (Theorem 2.3.15): $M_{aX + b}(t) = e^{bt} M_X(at)$.
- **Mgfs to know:** binomial $[pe^t + (1 - p)]^n$; Poisson $e^{\lambda(e^t - 1)}$; gamma $(1 - \beta t)^{-\alpha}$ for $t < 1/\beta$, with exponential($\lambda$) $= (1 - \lambda t)^{-1}$ for $t < 1/\lambda$.
- **Uniqueness** (Theorem 2.3.11): if two mgfs exist and agree near 0, the distributions are the same. Moments alone may **not** determine a distribution (Example 2.3.10, lognormal).
- **Convergence** (Theorem 2.3.12): if $M_{X_i}(t) \to M_X(t)$ near 0 and $M_X$ is an mgf, then $F_{X_i}(x) \to F_X(x)$ at continuity points of $F_X$. With Lemma 2.3.14, $\left( 1 + \frac{a_n}{n} \right)^n \to e^a$ when $a_n \to a$; this gives the Poisson approximation to the binomial (Example 2.3.13).
- **Existence hierarchy:** mgf exists $\Rightarrow$ all moments finite $\Rightarrow$ $\mathrm{Var}\, X < \infty$ $\Rightarrow$ $\mathrm{E}X$ exists, and no arrow reverses (Cauchy; $2/y^3$ on $y > 1$; lognormal).

---

# Part III. Ways of Thinking for Problem Solving


**1. Always start from definitions.** When you are stuck, examine the precise definition of every term in the question. The definition usually tells you what to check.

- *In this course:* "$A = B$" means $A \subset B$ and $B \subset A$. "Independent" means $P(A \cap B) = P(A) P(B)$. "Cdf" means $P(X \le x)$ for **every** real $x$. "$\mathrm{E}\,g(X)$ exists" means $\mathrm{E}\lvert g(X) \rvert < \infty$.

**2. Build from a few rules.** All of probability follows from three axioms. A proof is a chain of steps, each one justified by a definition, an axiom, or an earlier result.

- *In this course:* $P(A^c) = 1 - P(A)$, inclusion–exclusion, and Boole's inequality all come from the axioms. Cite the result you use at each step.
- *Beyond:* know which assumptions a conclusion rests on. If an assumption fails, so may the conclusion.

**3. Translation between words and formulas.** Name the events and random variables, write down what is given and what is asked, and only then compute.

- *In this course:* "given that" becomes a conditional probability; "at least one" becomes a union; a statement about $X$ is a statement about an event $\lbrace s : X(s) \in A \rbrace$ in $S$.
- *Beyond:* most of the work in a real problem is stating it clearly. A well-posed question is half answered.

**4. Draw a picture.** Pictures show what to compute, even though they are not proofs.

- *In this course:* Venn diagrams for set identities; trees for conditional probabilities; a sketch of the cdf to see jumps and flat pieces; a graph of $g$ on the support for transformations.
- *Beyond:* plot the data before modeling it.

**5. Divide and conquer.** Break a hard problem into pieces that do not overlap and together cover everything, solve each piece, then put them back together.

- *In this course:* write a set as a disjoint union and add (Axiom 3); the partition formula and total probability; counting task by task; piecewise-monotone transformations.
- *Beyond:* split a project into parts with clear boundaries, so nothing is done twice and nothing is missed.

**6. Turn the problem around.** If the direct route is hard, try the opposite question.

- *In this course:* the complement for "at least one"; Bayes' rule to turn $P(B \mid A)$ into $P(A \mid B)$; transform the *event*, not the density, in the cdf method; the inverse cdf to go from a uniform to any distribution.
- *Beyond:* "What would have to be true for this to fail?" is often easier to answer than "Why does this work?"

**7. Know where things live.** Every formula comes with a domain, and every result comes with conditions.

- *In this course:* supports in transformations; the pieces of a cdf outside the support; $P(B) > 0$ for conditioning; for which $t$ an mgf is finite; whether an expectation exists; the hypotheses of each theorem (continuity in Theorem 2.1.10, monotonicity in Theorem 2.1.5).
- *Beyond:* a model fit on one population may not apply to another.

**8. Recognize patterns.** Most new problems are old problems in disguise. Ask, "Have I seen something like this before?"

- *In this course:* recognize a known series or a pdf kernel inside a sum or integral; match an mgf to a known one, then use uniqueness; reduce to a standard case by a shift and scale.
- *Beyond:* build a toolbox of solved problems, and look for the one that fits.

**9. Back and forth between intuition and formalization.** Intuition suggests what to try, but only a proof or a calculation settles it. 

- *In this course:* disjoint events are not independent; pairwise independence is not mutual independence; $\mathrm{E}\,g(X) \ne g(\mathrm{E}X)$; a pdf can exceed 1; moments alone may not determine a distribution; the three prisoners.
- *Beyond:* correlation is not causation; one example does not prove a rule, but one counterexample disproves it.

---

# Part IV. Before You Hand In

**A short checklist for every problem.**

- Did I define my events or random variables in words?
- Did I state supports and give cdfs and pdfs for **every** real $x$?
- Does every probability lie in $[0, 1]$? Does my pmf sum, or my pdf integrate, to 1?
- Did I cite the definition, axiom, or theorem behind each step?
- For an mgf, did I say where it is finite? Is $M(0) = 1$?
- Is $\mathrm{Var}\, X \ge 0$? Does a quick special case (e.g., $n = 1$, $p = \frac{1}{2}$) give a sensible answer?

**Common mistakes.**

- Using a Venn diagram as a proof of set equality.
- Treating disjoint events as independent, or assuming independence that is not given.
- Confusing $P(A \mid B)$ with $P(B \mid A)$.
- Counting the numerator and denominator in different ways (ordered vs. unordered).
- Forgetting the support, or the pieces of a cdf outside the support.
- Writing $\mathrm{E}\,g(X) = g(\mathrm{E}X)$ for nonlinear $g$.
- Computing $\mathrm{E}X$ for a distribution whose mean does not exist.
- Forgetting the absolute value $\left\lvert \frac{d}{dy} g^{-1}(y) \right\rvert$ for a decreasing $g$.

**How to study.** Rework Homeworks 1–3 and the Week 1–5 discussion problems without looking at the solutions, then redo the "Check your understanding" questions in the notes. For more practice, use the C&B exercises listed at the end of each week's notes (skip the §2.4 ones: 2.39 and 2.40).
