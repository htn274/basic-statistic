def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def binomial(x, n, p):
    comb = factorial(n) / (factorial(x) * factorial(n - x))
    return comb * p ** x * (1 - p) ** (n - x)

p = 0.12
n = 10

no_more_than_2 = binomial(0, n, p) + binomial(1, n, p) + binomial(2, n, p)
at_least_2 = 1 - no_more_than_2 + binomial(2, n, p) 

print(round(no_more_than_2, 3))
print(round(at_least_2, 3))
