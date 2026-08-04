"""[LEARNING LOGS] Arcade of Time: Store Check"""
store, time = [int(x) for x in input().split()]
storetime = []
while store:
    storetime.append([int(x) for x in input().split()])
    store -= 1
checktime = [int(x) for x in input().split()]

for time in checktime:
    count = 0
    for i in storetime:
        if i[0] <= time < i[1]:
            count += 1
    print(count, end=" ")
