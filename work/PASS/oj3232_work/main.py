"""[LEARNING LOGS] กบน้อยกระโดด"""
x, y = [int(x) for x in input().split()]
goal, step = 0, 0
for i in range(0, x + 1, 2):
    goal += (x - i)
    step += 1
    if goal >= y:
        break

if goal >= y:
    print(step)
else:
    print(-1)
