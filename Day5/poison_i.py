import sys

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def poison(k, lamda):
    eps = 2.71828 
    fk = factorial(k)

    return (lamda**k * eps**(-lamda)) / fk

lamda  = 2.5
k = 5
res = poison(k, lamda)
print(round(res, 3))
