---
layout: page
---

# STAT 201A Homework 1

Show all work and justify every step from definitions, axioms, or results proved in class. You may discuss the problems with classmates, but the solutions you submit must be written by you. Pdf files of typed or hand-written-and-scan answers are both acceptable.

---

**1. (Exercise 1.10)** Formulate and prove a version of DeMorgan's Laws that applies to a finite collection of sets $A_1, \dots, A_n$.

**2. (Exercise 1.11(c), extended)** Let $S$ be a sample space.

- **(a)** Show that the intersection of two sigma algebras on $S$ is a sigma algebra.
- **(b)** Is the *union* of two sigma algebras on $S$ always a sigma algebra? Prove it, or give a counterexample.

**3. (Exercise 1.13)** If $P(A) = \frac{1}{3}$ and $P(B^c) = \frac{1}{4}$, can $A$ and $B$ be disjoint? Explain.

**4. (Exercise 1.14)** Suppose that a sample space $S$ has $n$ elements. Prove that the number of subsets that can be formed from the elements of $S$ is $2^n$.


**5.** Prove that $P(A \cap B) \le \min\lbrace P(A), P(B) \rbrace \le \max\lbrace P(A), P(B) \rbrace \le P(A \cup B)$.

**6.** Let $A \triangle B = (A \cap B^c) \cup (A^c \cap B)$ be the event that exactly one of $A$ and $B$ occurs. Show that $P(A \triangle B) = P(A) + P(B) - 2P(A \cap B)$.

**7.** Let $S = \lbrace 1, 2, 3, 4 \rbrace$. List the smallest sigma algebra that contains $\lbrace 1 \rbrace$ and $\lbrace 2 \rbrace$.

**8.** Infinite unions and intersections

- **(a)** Compute each set, and justify your answer with the "for some $n$" / "for all $n$" definitions:

  $$
  \bigcup_{n=1}^{\infty} \left[ \frac{1}{n},\, 1 - \frac{1}{n} \right], \qquad
  \bigcap_{n=1}^{\infty} \left( -\frac{1}{n},\, \frac{1}{n} \right), \qquad
  \bigcap_{n=1}^{\infty} \left[ 0,\, 1 + \frac{1}{n} \right).
  $$

- **(b)** Interpret the event $\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_n$ in words. (Consider an outcome $x$: for which $k$ does $x$ belong to $\bigcup_{n \ge k} A_n$?)
