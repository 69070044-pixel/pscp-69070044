"""rabbit virus"""
row, column = [int(x) for x in input().split()]
x1, y1 = [int(x) for x in input().split()]
n, city, risk = int(input()), [], 0
for i in range(row):
    city.append([])
    for j in range(column):
        city[-1].append([0])

for _ in range(n):
    i, j = [int(x) for x in input().split()]
    # loop โดยตัดขอบที่เกินทิ้ง
    for x in range(max(0, i - 2), min(row, i + 3)):
        for y in range(max(0, j - 2), min(column, j + 3)):
            dist = max(abs(x - i), abs(y - j))
            if not dist:
                risk = 100
            elif dist == 1:
                risk = 60
            elif dist == 2:
                risk = 20

            city[x][y].append(risk)
count = 0
for r in city:
    count += r.count([0])
print(count)
print(f"{max(city[x1][y1])}%")
