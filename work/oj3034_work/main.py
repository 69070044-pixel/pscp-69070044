"""OJ3034"""
n, k,  = [int(x) for x in input().split()]
queue = [[]] * k
line_is_full = False
while n:
    row = int(input()) - 1
    queue[row].append(row + 1)
    for q in queue:
        if q:
            line_is_full = True
        else:
            line_is_full = False
            break
    if line_is_full:
        for q in range(k):
            queue[q].pop(0)
    n -= 1
result = 0
for q in queue:
    result += len(q)
print(result)
