import math

def normal_distribution(mean, std, x):
    res = 1 + math.erf((x - mean) / (std * 2**0.5))
    return res/2

e = 70 
std = 10 

higher_80 = 1 - normal_distribution(e, std, 80)
passed = normal_distribution(e, std, 60)
failed = 1 - passed

print(round(higher_80 * 100, 2))
print(round(failed * 100, 2))
print(round(passed * 100, 2))

