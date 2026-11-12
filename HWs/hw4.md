---
layout: page
---

# STAT 201A Homework 4

Show all work and justify every step from definitions, axioms, or results proved in class. You may discuss the problems with classmates, but the solutions you submit must be written by you. Pdf files of typed or hand-written-and-scan answers are both acceptable.

---

**1. (C&B Exercise 3.3)** The flow of traffic at certain street corners can sometimes be modeled as a sequence of Bernoulli trials by assuming that the probability of a car passing during any given second is a constant $p$ and that there is no interaction between the passing of cars at different seconds. If we treat seconds as indivisible time units (trials), the Bernoulli model applies. Suppose a pedestrian can cross the street only if no car is to pass during the next 3 seconds. Find the probability that the pedestrian has to wait for exactly 4 seconds before starting to cross.

**2.** A commercial insecticide is advertised as being 99% effective. Suppose 2,000 insects infest a rose garden where the insecticide has been applied, and let $X$ = number of surviving insects.

- **(a)** What probability distribution might provide a reasonable model for this experiment? State your assumptions.
- **(b)** Write down, but do not evaluate, an expression for the probability that fewer than 15 insects survive, using the model in (a).
- **(c)** Evaluate a Poisson approximation to the probability in (b). Explain why the approximation is justified here.

**3. (C&B Exercise 3.10)** Shuster (1991) describes a number of probability calculations that he did for a court case involving the sale of cocaine. A Florida police department seized 496 *suspected* packets of cocaine, of which four were randomly selected and tested and found to actually be cocaine. The police then chose two more packets at random and, posing as drug dealers, sold the packets to the defendant. These last two packets were lost before they could be tested to verify that they were, indeed, cocaine.

- **(a)** If the original 496 packets were composed of $N$ packets of cocaine and $M = 496 - N$ noncocaine, show that the probability of selecting 4 cocaine packets and then 2 noncocaine packets, which is the probability that the defendant is innocent of buying cocaine, is

  $$
  \frac{\binom{N}{4} \binom{M}{2}}{\binom{N + M}{4} \binom{N + M - 4}{2}}.
  $$

- **(b)** Maximizing (in $M$ and $N$) the probability in (a) maximizes the defendant's "innocence probability." Show that this probability is .022, attained at $M = 165$ and $N = 331$. *(You may use software to search over $N$.)*

**4. (C&B Exercise 3.14)** A random variable $X$ has a *logarithmic series distribution* with parameter $p$ if

$$
P(X = x) = \frac{-(1 - p)^x}{x \log p}, \qquad x = 1, 2, \dots, \quad 0 < p < 1.
$$

- **(a)** Verify that this defines a legitimate probability function.
- **(b)** Find the mean and variance of $X$.

*Hint:* use the power series $-\log(1 - q) = \sum_{x=1}^{\infty} q^x / x$ for $\lvert q \rvert < 1$, and the geometric series and its derivative.

**5. (C&B Exercise 3.8)** Two movie theaters compete for the business of 1,000 customers. Assume that each customer chooses between the movie theaters independently and with "indifference." Let $N$ denote the number of seats in each theater.

- **(a)** Using a binomial model, find an expression for $N$ that will guarantee that the probability of turning away a customer (because of a full house) is less than 1%.
- **(b)** Use the normal approximation, with the continuity correction, to get a numerical value for $N$.

**6. (C&B Exercise 3.24(d))** If $X \sim$ gamma$(\frac{3}{2}, \beta)$, then $Y = (X/\beta)^{1/2}$ has the *Maxwell distribution*. Derive the pdf of $Y$, verify that it is a pdf, and calculate the mean and variance of $Y$. *Hint:* for the moments, write $\mathrm{E}Y^n = \mathrm{E}(X/\beta)^{n/2}$ and recognize a gamma kernel.

**7. Hazard functions.** Suppose the random variable $T$ is the length of life of an object (possibly the lifetime of an electrical component or of a subject given a particular treatment). The *hazard function* $h_T(t)$ associated with $T$ is defined by

$$
h_T(t) = \lim_{\delta \to 0} \frac{P(t \le T < t + \delta \mid T \ge t)}{\delta}.
$$

- **(a)** Show that if $T$ is a continuous random variable, then

  $$
  h_T(t) = \frac{f_T(t)}{1 - F_T(t)} = -\frac{d}{dt} \log \big( 1 - F_T(t) \big).
  $$

- **(b)** If $T \sim$ exponential($\beta$), show that $h_T(t) = 1/\beta$. Relate this to the memoryless property.
- **(c)** If $T \sim$ Weibull($\gamma$, $\beta$), with pdf $f_T(t) = \frac{\gamma}{\beta} t^{\gamma - 1} e^{-t^{\gamma}/\beta}$, $t > 0$, show that $h_T(t) = (\gamma/\beta) t^{\gamma - 1}$. For which $\gamma$ is the hazard increasing in $t$, and what does that say about aging?
