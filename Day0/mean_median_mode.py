import numpy as np
from scipy import stats

x = int(input())
arr = list(map(int, input().split()))

print(np.mean(arr))
print(np.median(arr))
mode = stats.mode(arr)

print(mode[0][0])
