def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def binomial(x, n, p):
    comb = factorial(n) / (factorial(x) * factorial(n - x))
    return comb * p ** x * (1 - p) ** (n - x)

values = list(map(float, input().split()))
p = values[0] / (values[0] + values[1])

n = 6

res = 1 - (binomial(0, n, p) + binomial(1, n, p) + binomial(2, n, p))
print(round(res, 3))
