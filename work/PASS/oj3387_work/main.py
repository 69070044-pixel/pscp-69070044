"""Tuple's Sad life"""
data = tuple(input().split())
find = input()
idx, count = data.index(find), data.count(find)
for _ in range(count):
    print(*([idx] * count))
