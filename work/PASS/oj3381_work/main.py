"""[LEARNING LOGS] Point Sorting"""
testset = int(input())
result = []
for _ in range(testset):
    point, tc = int(input()), []
    for _ in range(point):
        x, y = [int(e) for e in input().split()]
        tc.append([x, y])
    tc.sort(key=lambda x: (x[0] + x[1], x[0]))
    result += tc

for r in result:
    print(*r)
