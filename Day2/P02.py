cnt = 0
for i in range(6):
    for j in range(6):
        if i != j and i + j + 2 == 6:
            cnt += 1
print(cnt)
