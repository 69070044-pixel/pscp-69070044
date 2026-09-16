"""[LEARNING LOGS] หั่นขนมปัง"""
w, h, m, n = [int(p) for p in input().split()]
x_axis = [int(x) for x in input().split()] + [w]
y_axis = [int(y) for y in input().split()] + [h]
x_adjust, y_adjust = 0, 0
square = []
for i in range(m + 1):
    x_len = x_axis[i] - x_adjust
    for j in range(n + 1):
        y_len = y_axis[j] - y_adjust
        y_adjust = y_axis[j]
        area = x_len * y_len
        square.append(area)
    x_adjust = x_axis[i]
    y_adjust = 0
square.sort(reverse=True)
print(square[0], square[1])
