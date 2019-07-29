def get_mean(arr):
    mean = 0
    for x in arr:
        mean += x
    return mean / len(arr)

def get_std(arr):
    mean = get_mean(arr)
    std = 0
    for x in arr:
        std += (x - mean) ** 2

    return (std / len(arr)) ** 0.5

n = int(input()) 
arr = list(map(int, input().split()))
std = get_std(arr)
print("{:.1f}".format(std))
