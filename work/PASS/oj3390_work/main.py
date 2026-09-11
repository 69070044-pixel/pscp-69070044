"""2d array"""
data = []
for _ in range(5):
    data.append([int(x) for x in input().split()])
incorrectXY = []
for i, v in enumerate(data):
    if sum(v) % 2:
        incorrectXY.append(i)
        break

if incorrectXY:
    data_tranpose = [[], [], [], [], []]
    for i, v in enumerate(data_tranpose):
        for j in data:
            v.append(j[i])

    for i, v in enumerate(data_tranpose):
        if sum(v) % 2:
            incorrectXY.append(i)
            break

if incorrectXY:
    print(*incorrectXY)
else:
    print(-1, -1)
