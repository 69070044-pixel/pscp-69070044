"""ตำบลกระสุนตก"""
n = int(input())
pos = []
for _ in range(n):
    pos.append([int(x) for x in input().split()])
pos.sort(key=lambda x: x[-1])

