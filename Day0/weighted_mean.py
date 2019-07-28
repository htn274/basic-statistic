#import numpy as np

n= int(input())
value = list(map(int, input().split()))
weight = list(map(int, input().split()))

#weighted_mean = np.average(value, weights=weight)
weighted_mean = 0

for i in range(n):
    weighted_mean += value[i] * weight[i]

weighted_mean /= sum(weight)
print(weighted_mean)
