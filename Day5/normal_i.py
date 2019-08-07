import math

def normal_distribution(mean, std, x):
    res = 1 + math.erf((x - mean) / (std * 2**0.5))
    return res/2

e = 20
std = 2

res1 = normal_distribution(e, std, 19.5)
res2 = normal_distribution(e, std, 22) - normal_distribution(e, std, 20)

print(round(res1, 3))
print(round(res2, 3))
