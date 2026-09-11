"""shorten"""
temp, storage, result = 0, [], []
while True:
    num = int(input())
    if num == -1:
        break

    if not storage:
        storage.append([num])
        temp = num
    elif num - 1 == temp:
        storage[-1].append(num)
        temp = num
    else:
        storage.append([num])
        temp = num

for r in storage:
    if len(r) > 1:
        result.append(f"{r[0]}-{r[-1]}")
    else:
        result.append(r[0])
print(*result, sep=", ")
