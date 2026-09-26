"""MissingNumber"""
n = int(input())
numset, numinputset = set(range(1, n + 1)), set()
while True:
    value = int(input())
    if not value:
        break
    numinputset.add(value)
print(*sorted(list(numset - numinputset)), sep="\n")
