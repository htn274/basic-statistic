import math

def mean(arr):
    """
    Get mean of a random variable
    arr: list
    return an float
    """
    return sum(arr) / len(arr)

def std(arr):
    """
    Get standard derivation of a random variable
    arr: list
    return: float
    """
    m = mean(arr)
    std = 0
    for x in arr:
        std += math.pow(x-m, 2)
    return std ** 0.5

def p(x, y, n):
    """
    Get Pearson Correlation Coefficient of two random variables
    x, y: list
    n: int
    return: float
    """
    res = 0
    mx = mean(x)
    my = mean(y)
    for i in range(n):
        res += (x[i] - mx)*(y[i] - my)

    res /= (std(x) * std(y))
    return res

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

print(round(p(x, y, n), 3))

