e_x = 0.88
e_y = 1.55

e_x2 = e_x + e_x ** 2
e_y2 = e_y + e_y ** 2

res_x = 160 + 40 * e_x2
res_y = 128 + 40 * e_y2

print(round(res_x, 3))
print(round(res_y, 3))
