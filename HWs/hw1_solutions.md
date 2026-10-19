---
layout: page
---

# STAT 201A Homework 1 Solutions

Theorem numbers refer to Casella & Berger (C&B). The two results used most often are

- **Theorem 1.2.9.** If $P$ is a probability function and $A$ and $B$ are any sets in $\mathcal{B}$, then
  - **a.** $P(B \cap A^c) = P(B) - P(A \cap B)$;
  - **b.** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$;
  - **c.** If $A \subset B$, then $P(A) \le P(B)$.
- **Double containment:** to show $E = F$, show $E \subset F$ and $F \subset E$, i.e., $x \in E \Rightarrow x \in F$ and $x \in F \Rightarrow x \in E$.

---

**1. (Exercise 1.10)** *Formulate and prove a version of DeMorgan's Laws that applies to a finite collection of sets $A_1, \dots, A_n$.*

**Statement.** For any sets $A_1, \dots, A_n$,

$$
\text{(a)} \ \left( \bigcup_{i=1}^{n} A_i \right)^c = \bigcap_{i=1}^{n} A_i^c, \qquad
\text{(b)} \ \left( \bigcap_{i=1}^{n} A_i \right)^c = \bigcup_{i=1}^{n} A_i^c.
$$

**Proof of (a).** Each step below is an "if and only if," so it proves both containments at once:

$$
\begin{aligned}
x \in \left( \textstyle\bigcup_{i=1}^{n} A_i \right)^c
&\iff x \notin \textstyle\bigcup_{i=1}^{n} A_i \\
&\iff \text{it is not true that } x \in A_i \text{ for some } i \\
&\iff x \notin A_i \text{ for every } i = 1, \dots, n \\
&\iff x \in A_i^c \text{ for every } i \\
&\iff x \in \textstyle\bigcap_{i=1}^{n} A_i^c.
\end{aligned}
$$

**Proof of (b).** Apply (a) to the sets $A_1^c, \dots, A_n^c$ and use $(A^c)^c = A$:

$$
\left( \bigcup_{i=1}^{n} A_i^c \right)^c = \bigcap_{i=1}^{n} A_i .
$$

Taking complements of both sides gives $\bigcup_{i=1}^{n} A_i^c = \left( \bigcap_{i=1}^{n} A_i \right)^c$. $\square$

*Alternative:* induction on $n$, using the two-set laws (Theorem 1.1.4(d)) for the base case and the step $\bigcup_{i=1}^{n+1} A_i = \left( \bigcup_{i=1}^{n} A_i \right) \cup A_{n+1}$.

---

**2. (Exercise 1.11(c), extended)**

**(a)** Let $\mathcal{B}_1$ and $\mathcal{B}_2$ be sigma algebras on $S$, and let $\mathcal{B} = \mathcal{B}_1 \cap \mathcal{B}_2$, the collection of sets that belong to **both**. We check the three properties of Definition 1.2.1.

1. $\emptyset \in \mathcal{B}_1$ and $\emptyset \in \mathcal{B}_2$, so $\emptyset \in \mathcal{B}$.
2. If $A \in \mathcal{B}$, then $A \in \mathcal{B}_1$, so $A^c \in \mathcal{B}_1$; likewise $A^c \in \mathcal{B}_2$. Hence $A^c \in \mathcal{B}$.
3. If $A_1, A_2, \dots \in \mathcal{B}$, then all $A_i \in \mathcal{B}_1$, so $\bigcup_{i=1}^{\infty} A_i \in \mathcal{B}_1$; likewise for $\mathcal{B}_2$. Hence $\bigcup_{i=1}^{\infty} A_i \in \mathcal{B}$.

So $\mathcal{B}_1 \cap \mathcal{B}_2$ is a sigma algebra. $\square$ (The same argument works for the intersection of any collection of sigma algebras.)

**(b)** **No.** Let $S = \lbrace 1, 2, 3 \rbrace$ and

$$
\mathcal{B}_1 = \lbrace \emptyset, \lbrace 1 \rbrace, \lbrace 2, 3 \rbrace, S \rbrace, \qquad
\mathcal{B}_2 = \lbrace \emptyset, \lbrace 2 \rbrace, \lbrace 1, 3 \rbrace, S \rbrace .
$$

Each is a sigma algebra (it is closed under complements and unions). But $\mathcal{B}_1 \cup \mathcal{B}_2$ contains $\lbrace 1 \rbrace$ and $\lbrace 2 \rbrace$ and not their union $\lbrace 1, 2 \rbrace$, so it is not closed under unions and is not a sigma algebra.

---

**3. (Exercise 1.13)** *If $P(A) = \frac{1}{3}$ and $P(B^c) = \frac{1}{4}$, can $A$ and $B$ be disjoint?*

**No.** By Theorem 1.2.8(c), $P(B) = 1 - P(B^c) = \frac{3}{4}$. If $A$ and $B$ were disjoint, then by Axiom 3

$$
P(A \cup B) = P(A) + P(B) = \frac{1}{3} + \frac{3}{4} = \frac{13}{12} > 1,
$$

which contradicts $P(A \cup B) \le 1$ (Theorem 1.2.8(b)). Indeed, Theorem 1.2.9(b) gives $P(A \cap B) = P(A) + P(B) - P(A \cup B) \ge \frac{13}{12} - 1 = \frac{1}{12} > 0$.

---

**4. (Exercise 1.14)** *If $S$ has $n$ elements, the number of subsets of $S$ is $2^n$.*

Write $S = \lbrace s_1, \dots, s_n \rbrace$. A subset $A \subset S$ is determined by answering, for each $i = 1, \dots, n$, the yes/no question "is $s_i \in A$?" Different subsets give different answer sequences, and every sequence of $n$ answers gives a subset. So subsets correspond one-to-one to sequences in $\lbrace \text{yes}, \text{no} \rbrace^n$. By the Fundamental Theorem of Counting (Theorem 1.2.14), there are $2 \times 2 \times \cdots \times 2 = 2^n$ such sequences. $\square$

*Alternative:* there are $\binom{n}{k}$ subsets of size $k$, so the total is $\sum_{k=0}^{n} \binom{n}{k} = (1 + 1)^n = 2^n$ by the binomial theorem. *Or* induction: adding an element $s_{n+1}$ doubles the count, since every subset of $\lbrace s_1, \dots, s_{n+1} \rbrace$ either omits $s_{n+1}$ or is a subset of $\lbrace s_1, \dots, s_n \rbrace$ with $s_{n+1}$ added.

---

**5.** *Prove that $P(A \cap B) \le \min\lbrace P(A), P(B) \rbrace \le \max\lbrace P(A), P(B) \rbrace \le P(A \cup B)$.*

- **First inequality.** $A \cap B \subset A$ and $A \cap B \subset B$, so by Theorem 1.2.9(c), $P(A \cap B) \le P(A)$ and $P(A \cap B) \le P(B)$. A number below both $P(A)$ and $P(B)$ is below the smaller of the two.
- **Middle inequality.** The minimum of two numbers is at most their maximum.
- **Last inequality.** $A \subset A \cup B$ and $B \subset A \cup B$, so $P(A) \le P(A \cup B)$ and $P(B) \le P(A \cup B)$ by Theorem 1.2.9(c). A number above both is above the larger. $\square$

---

**6.** *Show that $P(A \triangle B) = P(A) + P(B) - 2P(A \cap B)$.*

The sets $A \cap B^c$ and $A^c \cap B$ are disjoint: a point in both would be in $B^c \cap B = \emptyset$. So by Axiom 3,

$$
P(A \triangle B) = P(A \cap B^c) + P(A^c \cap B).
$$

By Theorem 1.2.9(a), $P(A \cap B^c) = P(A) - P(A \cap B)$ and $P(B \cap A^c) = P(B) - P(A \cap B)$. Adding,

$$
P(A \triangle B) = P(A) + P(B) - 2P(A \cap B). \quad \square
$$

*Check:* $P(A \triangle B) = P(A \cup B) - P(A \cap B)$, which is Theorem 1.2.9(b) minus $P(A \cap B)$. Compared with $P(A \cup B)$, the overlap is removed twice instead of once.

---

**7.** *Let $S = \lbrace 1, 2, 3, 4 \rbrace$. List the smallest sigma algebra that contains $\lbrace 1 \rbrace$ and $\lbrace 2 \rbrace$.*

Any sigma algebra containing $\lbrace 1 \rbrace$ and $\lbrace 2 \rbrace$ must contain $\lbrace 1, 2 \rbrace$ (unions) and therefore $\lbrace 1, 2 \rbrace^c = \lbrace 3, 4 \rbrace$ (complements). The three sets $\lbrace 1 \rbrace$, $\lbrace 2 \rbrace$, $\lbrace 3, 4 \rbrace$ partition $S$, and the sigma algebra must contain all $2^3 = 8$ unions of them:

$$
\mathcal{B} = \Big\lbrace \emptyset,\ \lbrace 1 \rbrace,\ \lbrace 2 \rbrace,\ \lbrace 3, 4 \rbrace,\ \lbrace 1, 2 \rbrace,\ \lbrace 1, 3, 4 \rbrace,\ \lbrace 2, 3, 4 \rbrace,\ S \Big\rbrace .
$$

This collection is closed under complements (e.g., $\lbrace 1 \rbrace^c = \lbrace 2, 3, 4 \rbrace$) and under unions (a union of unions of the three blocks is again such a union), so it is a sigma algebra. It is the smallest because every one of its sets was forced. Note that $\lbrace 3 \rbrace \notin \mathcal{B}$: this sigma algebra cannot tell 3 from 4.

---

**8. Infinite unions and intersections**

**(a)**

1. $\displaystyle \bigcup_{n=1}^{\infty} \left[ \frac{1}{n}, 1 - \frac{1}{n} \right] = (0, 1)$. (The interval is empty for $n = 1$ and equals $\lbrace \frac{1}{2} \rbrace$ for $n = 2$.)
   - $\subset$: if $x$ is in the union, then $\frac{1}{n} \le x \le 1 - \frac{1}{n}$ for **some** $n$, so $0 < x < 1$.
   - $\supset$: if $0 < x < 1$, choose $n$ with $\frac{1}{n} \le \min\lbrace x, 1 - x \rbrace$. Then $x \in \left[ \frac{1}{n}, 1 - \frac{1}{n} \right]$ for that $n$.
   - The endpoints 0 and 1 are in none of the intervals.
2. $\displaystyle \bigcap_{n=1}^{\infty} \left( -\frac{1}{n}, \frac{1}{n} \right) = \lbrace 0 \rbrace$.
   - $0$ is in every interval.
   - If $x \ne 0$, choose $n$ with $\frac{1}{n} \le \lvert x \rvert$. Then $x \notin \left( -\frac{1}{n}, \frac{1}{n} \right)$, so $x$ is not in **all** of them.
3. $\displaystyle \bigcap_{n=1}^{\infty} \left[ 0, 1 + \frac{1}{n} \right) = [0, 1]$.
   - If $0 \le x \le 1$, then $x < 1 + \frac{1}{n}$ for every $n$.
   - If $x > 1$, choose $n$ with $\frac{1}{n} \le x - 1$. Then $x \notin \left[ 0, 1 + \frac{1}{n} \right)$.
   - If $x < 0$, $x$ is in none of the intervals.
   - Note that the intervals are half-open but the intersection is closed: the point $1$ is in every interval.

**(b)** Fix an outcome $x$. Then $x \in \bigcup_{n \ge k} A_n$ means "$x$ is in some $A_n$ with $n \ge k$," i.e., $x$ is in at least one set **at or after** stage $k$. The intersection over $k$ requires this for **every** $k$: no matter how far out we go, $x$ belongs to some later $A_n$. That happens exactly when $x$ belongs to **infinitely many** of the $A_n$.

So $\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_n$ is the event "**$A_n$ occurs infinitely often**," also called $\limsup_{n} A_n$. (If $x$ were in only finitely many $A_n$, with the last one at $n = N$, then $x \notin \bigcup_{n \ge N+1} A_n$, so $x$ fails at $k = N + 1$.)
