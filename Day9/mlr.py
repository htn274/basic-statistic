from sklearn import linear_model 
import math

m, n = map(int, input().split(' '))
X = []
Y = []

for i in range(n):
    arr = list(map(float, input().split()))
    X.append(arr[0:m])
    Y.append(arr[m])

lm = linear_model.LinearRegression()
lm.fit(X, Y)

q = int(input())
X_test = []
for i in range(q):
    x = list(map(float, input().split()))
    X_test.append(x)

Y_hat = lm.predict(X_test)

for x in Y_hat:
    print(math.ceil(x * 100)/100)


