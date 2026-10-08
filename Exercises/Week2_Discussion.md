---
layout: page
title: Week 2 Discussion
---

**Covers:** the axioms and calculus of probabilities (Week 1, Lecture 1.2) and counting (Week 2, Lecture 2.1).

---

### Problem 1 (Working with the probability rules)

In a class, a student is chosen at random. Let $R$ be the event that the student uses R and $Y$ the event that the student uses Python, with

$$
P(R) = 0.60, \qquad P(Y) = 0.45, \qquad P(R \cap Y) = 0.25.
$$

For each answer below, name the rule you used. The relevant rules, for any events $A$ and $B$:

- **Theorem 1.2.8 (complement rule):** $P(A^c) = 1 - P(A)$; also $P(\emptyset) = 0$ and $P(A) \le 1$.
- **Theorem 1.2.9:**
  - **(a)** $P(B \cap A^c) = P(B) - P(A \cap B)$;
  - **(b)** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$;
  - **(c)** if $A \subset B$, then $P(A) \le P(B)$ (monotonicity).
- **Bonferroni's inequality (1.2.9):** $P(A \cap B) \ge P(A) + P(B) - 1$.

**(a)** Find the probability that the student uses

1. at least one of the two languages;
2. neither language;
3. R but not Python;
4. exactly one of the two languages.

*Hint:* write each event in set notation first, for example "R but not Python" is $R \cap Y^c$.

**(b)** Now suppose you are told only $P(R) = 0.60$ and $P(Y) = 0.45$, but not $P(R \cap Y)$. What are the smallest and largest possible values of $P(R \cap Y)$? Could $R$ and $Y$ be disjoint?

*Hint:* one bound comes from Bonferroni's inequality, the other from monotonicity ($R \cap Y \subset Y$).

**(c)** Show that both bounds in (b) can actually be attained. Take a class of 100 students, each equally likely to be chosen, and describe which students use each language.

<details markdown="1">
<summary>Show answer</summary>

**(a)**

1. $P(R \cup Y) = P(R) + P(Y) - P(R \cap Y) = 0.60 + 0.45 - 0.25 = 0.80$ (Theorem 1.2.9(b)).
2. $P(R^c \cap Y^c) = P\big( (R \cup Y)^c \big) = 1 - 0.80 = 0.20$ (DeMorgan, then the complement rule).
3. $P(R \cap Y^c) = P(R) - P(R \cap Y) = 0.60 - 0.25 = 0.35$ (Theorem 1.2.9(a)).
4. "Exactly one" is the disjoint union $(R \cap Y^c) \cup (R^c \cap Y)$, so its probability is $0.35 + (0.45 - 0.25) = 0.55$. Equivalently, $P(R \cup Y) - P(R \cap Y) = 0.80 - 0.25 = 0.55$.

**(b)** By Bonferroni, $P(R \cap Y) \ge 0.60 + 0.45 - 1 = 0.05$. By monotonicity, $P(R \cap Y) \le P(Y) = 0.45$. So $0.05 \le P(R \cap Y) \le 0.45$. In particular $P(R \cap Y) > 0$, so $R$ and $Y$ cannot be disjoint.

**(c)** Number the students $1, \dots, 100$ and let $R = \lbrace 1, \dots, 60 \rbrace$.

- Lower bound: $Y = \lbrace 56, \dots, 100 \rbrace$ gives $R \cap Y = \lbrace 56, \dots, 60 \rbrace$, probability $0.05$. Here every student uses at least one language.
- Upper bound: $Y = \lbrace 1, \dots, 45 \rbrace \subset R$ gives $R \cap Y = Y$, probability $0.45$. Here every Python user also uses R.

</details>

---

### Problem 2 (The matching problem)

Each of $n$ letters is placed at random into one of $n$ addressed envelopes, one letter per envelope, so all $n!$ arrangements are equally likely. What is the probability that **at least one** letter goes into its correct envelope?

Let $A_i$ be the event that letter $i$ is in its correct envelope. We want $P\left( \bigcup_{i=1}^{n} A_i \right)$. The events overlap, so we use the general **inclusion–exclusion** formula, which extends the two- and three-set versions from lecture:

$$
P\left( \bigcup_{i=1}^{n} A_i \right) = \sum_{i} P(A_i) - \sum_{i < j} P(A_i \cap A_j) + \sum_{i < j < k} P(A_i \cap A_j \cap A_k) - \cdots + (-1)^{n+1} P(A_1 \cap \cdots \cap A_n).
$$

**(a)** Find $P(A_i)$. *Hint:* if letter $i$ is fixed in its envelope, how many ways can the other $n - 1$ letters be arranged?

**(b)** Find $P(A_i \cap A_j)$ for $i \ne j$, and more generally $P(A_{i_1} \cap \cdots \cap A_{i_k})$ for any $k$ distinct letters.

**(c)** How many terms are in the $k$th sum $\sum_{i_1 < \cdots < i_k}$? Show that the whole $k$th sum equals $1/k!$.

**(d)** Conclude that

$$
P(\text{at least one match}) = 1 - \frac{1}{2!} + \frac{1}{3!} - \cdots + (-1)^{n+1} \frac{1}{n!}.
$$

**(e)** Evaluate for $n = 3$ and $n = 4$. Check $n = 3$ by listing all $3! = 6$ arrangements. What happens as $n \to \infty$? *Hint:* recall $e^{x} = \sum_{k=0}^{\infty} x^k / k!$.

<details markdown="1">
<summary>Show answer for (e)</summary>

For $n = 3$: $1 - \frac{1}{2} + \frac{1}{6} = \frac{2}{3}$. (Of the 6 arrangements, only the two cyclic ones, $231$ and $312$, have no match.) For $n = 4$: $1 - \frac{1}{2} + \frac{1}{6} - \frac{1}{24} = \frac{15}{24} = 0.625$.

As $n \to \infty$, the sum converges to $1 - e^{-1} \approx 0.632$. Surprisingly, the answer barely depends on $n$: with 10 letters or 10 million, the chance of at least one match is about 63%.

</details>

---

### Problem 3 (Galileo's dice problem)

Around 1620, gamblers asked Galileo a puzzle: when three dice are rolled, a sum of **9** and a sum of **10** can each be made in six ways, yet experience showed that 10 comes up more often. Why?

**(a)** List the six unordered ways to write 9 as a sum of three dice values (for example $\lbrace 1, 2, 6 \rbrace$), and do the same for 10.

**(b)** The gamblers' reasoning treats the unordered outcomes as equally likely. Which sample space *is* equally likely for three fair dice, and how many outcomes does it have?

**(c)** For each unordered outcome in (a), count the ordered outcomes that produce it. *Hint:* use the multinomial coefficient. For example, $\lbrace 1, 4, 4 \rbrace$ corresponds to $\frac{3!}{1!\,2!} = 3$ ordered rolls.

**(d)** Compute $P(\text{sum} = 9)$ and $P(\text{sum} = 10)$.

**(e)** How many distinct *unordered* outcomes are there for three dice? Use the unordered-with-replacement formula from Table 1.2.1, and explain why this number cannot be used as $N(S)$ in $P(A) = N(A)/N(S)$.

<details markdown="1">
<summary>Show answer for (d) and (e)</summary>

| Sum = 9 | Orderings | Sum = 10 | Orderings |
|---|---|---|---|
| $\lbrace 1,2,6 \rbrace$ | 6 | $\lbrace 1,3,6 \rbrace$ | 6 |
| $\lbrace 1,3,5 \rbrace$ | 6 | $\lbrace 1,4,5 \rbrace$ | 6 |
| $\lbrace 1,4,4 \rbrace$ | 3 | $\lbrace 2,2,6 \rbrace$ | 3 |
| $\lbrace 2,2,5 \rbrace$ | 3 | $\lbrace 2,3,5 \rbrace$ | 6 |
| $\lbrace 2,3,4 \rbrace$ | 6 | $\lbrace 2,4,4 \rbrace$ | 3 |
| $\lbrace 3,3,3 \rbrace$ | 1 | $\lbrace 3,3,4 \rbrace$ | 3 |
| **Total** | **25** | **Total** | **27** |

With $6^3 = 216$ equally likely ordered outcomes, $P(\text{sum} = 9) = 25/216 \approx 0.116$ and $P(\text{sum} = 10) = 27/216 = 0.125$.

There are $\binom{6 + 3 - 1}{3} = \binom{8}{3} = 56$ unordered outcomes, but they are not equally likely: $\lbrace 3,3,3 \rbrace$ has probability $1/216$, while $\lbrace 1,2,6 \rbrace$ has probability $6/216$. This is Example 1.2.19 again: with replacement, count ordered outcomes.

</details>
