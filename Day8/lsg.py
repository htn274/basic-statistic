"""
95 85
85 95
80 70
70 65
60 70
"""
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
n = len(x)
x_sum = sum(x)
y_sum = sum(y)
x_mean = x_sum / n
y_mean = y_sum / n
x_sum_square = 0
for i in x:
    x_sum_square += i**2
sum_product = 0
for i in range(n):
    sum_product += x[i] * y[i]

b = (n * sum_product - x_sum * y_sum) / (n * x_sum_square - x_sum ** 2)
a = y_mean - b * x_mean

x_test = 80
y_pred = a + b * x_test


print(round(y_pred, 3))

