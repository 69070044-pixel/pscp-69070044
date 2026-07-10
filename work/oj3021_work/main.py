"""OJ3021"""
import math

x1, y1, r1 = int(input()), int(input()), int(input())
x2, y2, r2 = int(input()), int(input()), int(input())

distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

sum_radius = r1 + r2

if distance <= sum_radius:
    print("overlapping")
else:
    print("no overlapping")
