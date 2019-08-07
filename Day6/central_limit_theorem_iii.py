import math 

n = 100
mean = 500
std = 80
p = 0.95
z = 1.96

# Problem: determine an interval [A, B]: P(A < avg <  B) = 0.95
# We have z score: the probability that you land in an interval of z std away from the mean

mean_sum = mean * n
std_sum = std * math.sqrt(n)

A = (mean_sum - z * std_sum) / n
B = (mean_sum + z * std_sum) / n

print(round(A, 2))
print(round(B, 2))