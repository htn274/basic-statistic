def g(n, p):
    return (1 -p) ** (n - 1) * p

p = 1 / 3
n = 5

print(round(g(n, p), 3))
