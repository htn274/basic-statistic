def g(n, p):
    return (1 -p) ** (n - 1) * p

p = 1/3
n = 5

res = 0
for i in range(1, n + 1):
    res += g(i, p)

print(round(res, 3))
