# Poisson Experiment

That is a statiscal experiment has some following   properties:

1. The outcome of each trials is either sucess or failure
2. The average number of sucess ($\lambda$) is known
3. The probability that a sucess will occur is proportinal to the size of the region. It is virtually zero in small region.

# Poisson Distribution

Poisson random variable is the number of sucesses that result from Poisson Experiment.

$$
P(k, \lambda) = \frac{\lambda ^ {k} e^{-\lambda}}{k!}
$$

with:

- $e = 2.71828$
- $\lambda$ is the average number of sucesses
- k is the actual number of sucesses
- $P(k, \lambda)$ the probability of getting exact $k$ sucesses when the average number of sucesses is $\lambda$

With $X$ is a poisson random variable.

- $E(X) = \lambda$
- $Var(X) = \lambda$
- $E(X^{2}) = \lambda + \lambda^{2}$
