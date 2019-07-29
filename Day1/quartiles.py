def cal_median(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[int(n/2) - 1] + arr[int(n/2)]) / 2
    return arr[int(n/ 2)]

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

q1 = cal_median(arr[0:int(n/2)])
q2 = cal_median(arr)
if n % 2 == 1:
    q3 = cal_median(arr[int(n/2) + 1 : n])
else:
    q3 = cal_median(arr[int(n/2): n])

print(q1, q2, q3, end = "\n")
