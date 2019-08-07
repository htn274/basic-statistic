- [Binominal Experiment](#Binominal-Experiment)
- [Binomial Distribution](#Binomial-Distribution)
- [Negative Binominal Experiment](#Negative-Binominal-Experiment)
- [Geomatric Distribution](#Geomatric-Distribution)

# Binominal Experiment

Binominal experiment is a statiscal experiment has the following properties:

1. The experiment consists of **n** repeated trials (n is fixed)
2. The trial is **independent**
3. The outcome of each trial is either sucessful (s) or failure (f).
4. The probability for sucessful trial is **p**

# Binomial Distribution

$$
b(x, n, p) = \binom{n}{x} \times p^{x} \times q^{n - x}
$$

with:

- x: the number of sucesses
- n: the number of trials
- p: the probability for sucess
- q = 1 - p

# Negative Binominal Experiment

A negative binomial experiment is a statistical experiment that has the following properties:

- The experiment consists of n repeated trials.
- The trials are independent.
- The outcome of each trial is either success (s) or failure (f).
- P(s) is the same for every trial.

**Important:** **The experiment continues until  successes are observed.**

**Binominal Distribution**

$$
b^{*}(n, x, p) = \binom{n - 1}{x - 1} p^{x} q^{n - x}
$$

with:

- x: the number of sucesses
- n: the number of trials
- p: the probability of sucess
- $b^{*}(n, x, p)$: is the negative binomial probability, meaning the probability of having x - 1 successes after  n - 1trials and having x successes after n trials. 
  
# Geomatric Distribution

The geometric distribution is a **special case of the negative binomial distribution** that deals with the number of Bernoulli trials required to get a success (i.e., counting the number of failures before the first success).

**Do until get a first sucess**

$$
g(n, p) = q^{n-1}p
$$