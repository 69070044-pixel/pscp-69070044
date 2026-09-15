"""member"""
m, n = int(input()), int(input())
A, B = set(), set()
for _ in range(m):
    A.add(input())
for _ in range(n):
    B.add(input())
result = sorted([int(x) for x in A.intersection(B)], reverse=True)
if result:
    print(*result, sep="\n")
else:
    print("Nope")
