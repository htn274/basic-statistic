import math

def normal_distribution(mean, std, x):
    res = 1 + math.erf((x - mean) / (std * 2**0.5))
    return res/2

n = 49
x = 9800
mean = 205
std = 15
mean_sum = mean * n
std_sum = std * math.sqrt(n)
res = normal_distribution(mean_sum, std_sum, x)
print(round(res, 4))
