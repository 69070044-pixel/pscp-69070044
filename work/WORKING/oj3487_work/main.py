"""Light"""
n, h = int(input()), []

for _ in range(n):
    h.append(int(input()))

h.sort()
total, prev = 0, 0
for v in h:
    total += (v + prev) * 2
    prev += v
print(total)
