"""bird"""
n = int(input())
h = [int(x) for x in input().split()]
count = 0
for i in range(n):
    if i == 0:
        l, r = 0, h[i + 1]
    elif i == n - 1:
        l, r = h[i - 1], 0
    else:
        l, r = h[i - 1], h[i + 1]
    if abs(h[i] - l) > 1 and abs(h[i] - r) > 1:
        count += 1
print(count)
