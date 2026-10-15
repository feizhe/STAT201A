---
layout: page
title: Week 3 Discussion
---

**Covers:** conditional probability, Bayes' rule, independence and random variables. Problems 1 and 3 are adapted from C&B §1.7.

---

### Problem 1 (Noisy telegraph: Bayes' rule and independence; C&B Exercise 1.41)

As in Example 1.3.6, telegraph signals "dot" and "dash" are sent in the proportion $3 : 4$. Erratic transmissions cause a dot to become a dash with probability $\frac{1}{4}$ and a dash to become a dot with probability $\frac{1}{3}$.

Useful tools: the law of total probability, $P(B) = \sum_i P(B \mid A_i) P(A_i)$, and Bayes' rule (Theorem 1.3.5), $P(A_i \mid B) = P(B \mid A_i) P(A_i) / P(B)$.

**(a)** Write down $P(\text{dot sent})$, $P(\text{dash sent})$, and the four conditional probabilities $P(\text{received} \mid \text{sent})$.

**(b)** Find $P(\text{dash received})$. Which partition of $S$ are you using?

**(c)** If a dash is received, what is the probability that a dash was sent?

**(d)** Now suppose a two-symbol message is sent. Assume the two symbols are chosen independently, each with the $3 : 4$ proportions, and that transmission errors happen independently for the two symbols. If the message dot-dot is received, what is the probability distribution of the four possible messages (dot-dot, dot-dash, dash-dot, dash-dash) that could have been sent?

*Hint for (d):* first find $P(\text{dot sent} \mid \text{dot received})$ and $P(\text{dash sent} \mid \text{dot received})$ for a single symbol. Then explain why independence lets you multiply.

<details markdown="1">
<summary>Show answer</summary>

**(a)** $P(\text{dot sent}) = \frac{3}{7}$ and $P(\text{dash sent}) = \frac{4}{7}$.

| Sent | Received dot | Received dash |
|---|---|---|
| dot | $3/4$ | $1/4$ |
| dash | $1/3$ | $2/3$ |

**(b)** Partition by what was sent, $\lbrace \text{dot sent}, \text{dash sent} \rbrace$:

$$
P(\text{dash rec.}) = \tfrac{1}{4} \cdot \tfrac{3}{7} + \tfrac{2}{3} \cdot \tfrac{4}{7} = \tfrac{9}{84} + \tfrac{32}{84} = \tfrac{41}{84}.
$$

**(c)**

$$
P(\text{dash sent} \mid \text{dash rec.}) = \frac{(2/3)(4/7)}{41/84} = \frac{32/84}{41/84} = \frac{32}{41} \approx 0.780.
$$

**(d)** For one symbol, $P(\text{dot rec.}) = 1 - \frac{41}{84} = \frac{43}{84}$, so

$$
P(\text{dot sent} \mid \text{dot rec.}) = \frac{(3/4)(3/7)}{43/84} = \frac{27}{43}, \qquad P(\text{dash sent} \mid \text{dot rec.}) = \frac{16}{43}.
$$

The pairs (symbol sent, symbol received) for the two positions are independent, so the posteriors multiply:

| Sent | Probability given dot-dot received |
|---|---|
| dot-dot | $(27/43)^2 = 729/1849 \approx 0.394$ |
| dot-dash | $(27 \cdot 16)/43^2 = 432/1849 \approx 0.234$ |
| dash-dot | $432/1849 \approx 0.234$ |
| dash-dash | $(16/43)^2 = 256/1849 \approx 0.138$ |

The four probabilities sum to $1849/1849 = 1$. Even though dot-dot was received, there is about a 61% chance that at least one symbol was actually a dash.

</details>

---

### Problem 2 (Pairwise vs. mutual independence)

Recall Definition 1.3.12: $A_1, \dots, A_n$ are **mutually independent** if the product rule holds for *every* subcollection, not just for pairs.

**(a)** Roll two fair dice, with all 36 ordered outcomes equally likely. Let $A$ = "the first die is odd," $B$ = "the second die is odd," and $C$ = "the sum is odd." 

Find $P(A)$, $P(B)$, $P(C)$, and check whether each of the pairs $(A, B)$, $(A, C)$, $(B, C)$ is independent.

**(b)** Are $A$, $B$, $C$ mutually independent? Compute $P(A \cap B \cap C)$ and $P(C \mid A \cap B)$, and explain in words why learning $A$ alone tells you nothing about $C$, while learning $A$ and $B$ together tells you everything.

**(c)** How many equations must be checked to show that four events $A_1, A_2, A_3, A_4$ are mutually independent? List them by size of the subcollection.

**(d)** A system has three components. Components 1 and 2 are in **parallel** (the pair works if at least one of them works), and that pair is in **series** with component 3 (the system works only if the pair works *and* component 3 works). Let $A_i$ = "component $i$ works," with $A_1, A_2, A_3$ mutually independent and $P(A_i) = p$.

1. Write the event "the system works" in terms of $A_1, A_2, A_3$.
2. Show that $P\big( A_3 \cap (A_1 \cup A_2) \big) = P(A_3)\, P(A_1 \cup A_2)$. *Hint:* distribute, then use Theorem 1.2.9(b). Which of your equations needs the **triple** product rule, so that pairwise independence would not be enough?
3. Find $P(\text{system works})$ as a function of $p$, and evaluate it at $p = 0.9$.

<details markdown="1">
<summary>Show answer</summary>

**(a)** $P(A) = P(B) = \frac{18}{36} = \frac{1}{2}$. The sum is odd exactly when one die is odd and the other is even, so $P(C) = \frac{9 + 9}{36} = \frac{1}{2}$.

- $A \cap B$: both odd, $\frac{9}{36} = \frac{1}{4} = P(A) P(B)$.
- $A \cap C$: first odd and second even, $\frac{9}{36} = \frac{1}{4} = P(A) P(C)$.
- $B \cap C$: first even and second odd, $\frac{9}{36} = \frac{1}{4} = P(B) P(C)$.

So the three events are **pairwise independent**.

**(b)** If both dice are odd, the sum is even, so $A \cap B \cap C = \emptyset$ and

$$
P(A \cap B \cap C) = 0 \ne \tfrac{1}{8} = P(A) P(B) P(C).
$$

They are **not** mutually independent. Also $P(C \mid A \cap B) = 0 \ne P(C)$. Knowing only the first die is odd leaves the sum odd or even with probability $\frac{1}{2}$ each, because it depends on the unknown second die. Knowing the parity of both dice determines the parity of the sum. (Compare Example 1.3.11.)

**(c)** One equation for every subcollection of size at least 2: $\binom{4}{2} = 6$ pairs, $\binom{4}{3} = 4$ triples, and $\binom{4}{4} = 1$ quadruple, so $6 + 4 + 1 = 11 = 2^4 - 4 - 1$ equations.

**(d)**

1. $\lbrace \text{system works} \rbrace = A_3 \cap (A_1 \cup A_2)$.
2. By the distributive law, $A_3 \cap (A_1 \cup A_2) = (A_3 \cap A_1) \cup (A_3 \cap A_2)$, and the intersection of these two pieces is $A_1 \cap A_2 \cap A_3$. By Theorem 1.2.9(b),

   $$
   P\big( A_3 \cap (A_1 \cup A_2) \big) = P(A_1 \cap A_3) + P(A_2 \cap A_3) - P(A_1 \cap A_2 \cap A_3) = p^2 + p^2 - p^3 = p\,(2p - p^2).
   $$

   Since $P(A_1 \cup A_2) = p + p - p^2 = 2p - p^2$, this equals $P(A_3) P(A_1 \cup A_2)$. The term $P(A_1 \cap A_2 \cap A_3) = p^3$ uses the triple product rule. With only pairwise independence it could be anything (in part (b) it was 0).
3. $P(\text{system works}) = p\,(2p - p^2) = p\,\big( 1 - (1 - p)^2 \big)$. At $p = 0.9$: $0.9 \times 0.99 = 0.891$.

**Takeaway:** "independent components" in reliability, or "independent tosses" in Example 1.3.13, always means **mutual** independence. That is what lets us treat combinations of some events, like $A_1 \cup A_2$, as independent of the others.

</details>

---

### Problem 3 (Guessing on a standardized test: a random variable; C&B Exercise 1.44)

A test has 20 multiple-choice questions, each with 4 possible answers. A student guesses on every question, so the taking of the exam can be modeled as 20 independent events, each "correct" with probability $\frac{1}{4}$.

**(a)** Describe the sample space $S$. How many outcomes does it have? Are they equally likely? *Hint:* record each answer as correct (C) or wrong (W).

**(b)** Let $X$ = the number of questions answered correctly. Explain why $X$ is a random variable in the sense of Definition 1.4.1. What is its range $\mathcal{X}$?

**(c)** Fix one outcome $s$ with exactly $k$ correct answers, for example $s = \text{CC}\cdots\text{C}\,\text{WW}\cdots\text{W}$. Use independence to find $P(\lbrace s \rbrace)$.

**(d)** Use the induced probability function (1.4.1), $P(X = k) = P(\lbrace s \in S : X(s) = k \rbrace)$, together with counting, to show that

$$
P(X = k) = \binom{20}{k} \left( \frac{1}{4} \right)^{k} \left( \frac{3}{4} \right)^{20 - k}, \qquad k = 0, 1, \dots, 20.
$$

**(e)** Find the probability that the student gets at least 10 questions correct. Also find $P(X \ge 1)$ using the complement.

<details markdown="1">
<summary>Show answer</summary>

**(a)** $S$ = all strings of length 20 over $\lbrace \text{C}, \text{W} \rbrace$, so $N(S) = 2^{20}$. The outcomes are **not** equally likely, because C has probability $\frac{1}{4}$ and W has probability $\frac{3}{4}$. (We could use the $4^{20}$ equally likely answer sheets instead, but then we would have to count the ones with $k$ correct answers as $\binom{20}{k} 3^{20-k}$, which gives the same result.)

**(b)** $X$ assigns to each outcome $s \in S$ the real number of Cs in $s$, so $X$ is a function from $S$ into the real numbers. $\mathcal{X} = \lbrace 0, 1, \dots, 20 \rbrace$.

**(c)** By mutual independence (Definition 1.3.12) and Theorem 1.3.9 for the complements, $P(\lbrace s \rbrace) = \left( \frac{1}{4} \right)^{k} \left( \frac{3}{4} \right)^{20-k}$. Every outcome with exactly $k$ Cs has this same probability, no matter where the Cs are.

**(d)** $\lbrace X = k \rbrace$ consists of the $\binom{20}{k}$ strings with C in exactly $k$ positions (choose the positions, unordered, without replacement). Each has the probability in (c), and the outcomes are disjoint, so their probabilities add. This is the **binomial distribution**, which we will meet again in Chapter 3.

**(e)**

$$
P(X \ge 10) = \sum_{k=10}^{20} \binom{20}{k} \left( \frac{1}{4} \right)^{k} \left( \frac{3}{4} \right)^{20 - k} \approx 0.0139.
$$

Guessing passes a "50%" bar only about 1.4% of the time. On the other hand, $P(X \ge 1) = 1 - P(X = 0) = 1 - (3/4)^{20} \approx 0.997$.

</details>
