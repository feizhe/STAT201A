---
layout: page
title: Week 1 Discussion
---

## Russell's paradox (1901)

In Week 1 we used sets freely: sample spaces, events, unions, complements. But **what is a set**, and can we form a set out of any description we like? At the turn of the 20th century, the answer was thought to be yes. Bertrand Russell showed it cannot be.

### The paradox

"Naive" set theory (Cantor, Frege) allowed a set to be formed from **any** property $\varphi$:

$$
\lbrace x : \varphi(x) \rbrace.
$$


Russell took the property "$x$ is not a member of itself" and formed

$$
R = \lbrace x : x \notin x \rbrace.
$$

> A popular version of the paradox: a barber shaves exactly those people who do not shave themselves. Who shaves the barber?

Now ask: **is $R \in R$?**


- If $R \in R$, then $R$ does not satisfy the defining property, so $R \notin R$.
- If $R \notin R$, then $R$ satisfies the defining property, so $R \in R$.

Both answers lead to their opposite, so naive set theory is **inconsistent**. 
### How modern set theory avoids it

Modern mathematics, including probability, rests on the axioms of **ZFC** (Zermelo–Fraenkel set theory with the Axiom of Choice). In ZFC, "set" is not defined; it is a primitive notion governed by axioms. Two of them rule out Russell's construction.

1. **Separation (Specification).** You cannot form $\lbrace x : \varphi(x) \rbrace$ out of nothing. You can only carve a subset out of a set $A$ you already have:

   $$
   \lbrace x \in A : \varphi(x) \rbrace.
   $$

   Russell's set becomes $R_A = \lbrace x \in A : x \notin x \rbrace$. This is a perfectly good set. Asking whether $R_A \in R_A$ now leads only to the conclusion that $R_A \notin A$, not to a contradiction. One consequence: **there is no "set of all sets."**

2. **Foundation (Regularity).** Every nonempty set $A$ has an element disjoint from $A$. It follows that **no set is a member of itself**: $x \in x$ is impossible (apply the axiom to $\lbrace x \rbrace$).



**Bottom line.** Because we always fix $S$ first and build events, complements, and sigma algebras from it, every set we use in this course is legitimate, and Russell's paradox cannot arise. The set-theoretic subtlety that *does* matter in probability is a different one, **non-measurable sets**. Using the Axiom of Choice, one can construct subsets of $[0, 1]$ that cannot be assigned any sensible length (Vitali, 1905). That is why we restrict $P$ to a sigma algebra instead of all subsets of $S$.

### Discussion questions

1. Let $S = \lbrace 1, 2, 3 \rbrace$ and let $A = \lbrace x \in S : x \notin x \rbrace$. What is $A$? Why is there no paradox here?
2. Why must a complement always be taken relative to a sample space $S$? What would go wrong if $A^c$ meant "everything not in $A$"?

---

### Problem 1 (From words to sets)

Let $A$, $B$, and $C$ be events in a sample space $S$.

**(a)** Write each event below using only $\cup$, $\cap$, and complements of $A$, $B$, $C$:

1. at least one of $A$, $B$, $C$ occurs;
2. none of them occurs;
3. exactly one of them occurs;
4. at most two of them occur.

**(b)** Use DeMorgan's laws to show that your answers to (1) and (2) are complements of each other, and rewrite (4) as the complement of a simpler event.

**(c)** Check your answers on a die: $S = \lbrace 1, \dots, 6 \rbrace$, $A = \lbrace 1, 2, 3 \rbrace$, $B = \lbrace 2, 4, 6 \rbrace$, $C = \lbrace 2, 3, 4 \rbrace$. List the outcomes in each of the four events.

*Hint for (3):* "exactly one" is a union of three pieces, one for each event that occurs alone. Are the three pieces disjoint?

### Problem 2 (Proof by double containment)

**(a)** Prove that $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$. Then give a one-line proof using $A \setminus B = A \cap B^c$ and DeMorgan's laws.

**(b)** True or false: $(A \cup B) \setminus B = A$. Prove it, or give a counterexample and state the correct identity.


### Problem 3 (Infinite unions and intersections)

**(a)** Compute each set, and justify your answer with the "for some $n$" / "for all $n$" definitions:

$$
\bigcup_{n=1}^{\infty} \left[ \frac{1}{n},\, 1 - \frac{1}{n} \right], \qquad
\bigcap_{n=1}^{\infty} \left( -\frac{1}{n},\, \frac{1}{n} \right), \qquad
\bigcap_{n=1}^{\infty} \left[ 0,\, 1 + \frac{1}{n} \right).
$$

**(b)** Let $A_1, A_2, A_3, \dots$ be any events. Define

$$
B_1 = A_1, \qquad B_n = A_n \cap A_1^c \cap \cdots \cap A_{n-1}^c, \quad n \ge 2.
$$

In words, $B_n$ is "$A_n$ occurs, but none of the earlier $A_i$ do."

1. Show that the $B_n$ are pairwise disjoint.
2. Show that $\bigcup_{n=1}^{\infty} B_n = \bigcup_{n=1}^{\infty} A_n$.
3. Find the $B_n$ for $A_n = [0, n]$ with $n = 1, 2, \dots$. Do they form a partition of $[0, \infty)$?

**(c)** *(Challenge)* Interpret the event $\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_n$ in words. (Consider an outcome $x$: for which $k$ does $x$ belong to $\bigcup_{n \ge k} A_n$?)

*Why this matters:* part (b) is the "disjointification" step we will use in Thursday's lecture to prove Boole's inequality.
