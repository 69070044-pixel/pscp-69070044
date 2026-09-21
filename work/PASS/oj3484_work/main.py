"""[LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง"""
rawinput = input().split()
n, price = int(rawinput[0]), float(rawinput[1])
tile_map, not_perfect_column, sum_of_point_column = [], [0] * n, [0] * n
for _ in range(int(n)):
    data = [int(x) for x in input().split()]
    not_perfect_row = len(data) - data.count(0)
    sum_of_point_row = sum(data)
    for i in range(int(n)):
        if data[i]:
            not_perfect_column[i] += 1
            sum_of_point_column[i] += data[i]
    tile_map.append(data + [not_perfect_row, sum_of_point_row])

total_not_perfect = sum(not_perfect_column)
total_of_point = sum(sum_of_point_column)
for row in tile_map:
    print(*row)
print(*not_perfect_column)
print(*sum_of_point_column)
print(total_not_perfect, total_of_point, format(total_of_point * price, '.2f'))
