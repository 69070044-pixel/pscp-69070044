"""set"""
n, m = int(input()), int(input())
A, B = set(), set()
for _ in range(n):
    A.add(int(input()))

for _ in range(m):
    B.add(int(input()))

print(*sorted(A.difference(B)))
