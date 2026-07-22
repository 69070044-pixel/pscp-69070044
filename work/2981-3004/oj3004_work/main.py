"""OJ3004"""
import math
x1, y1, z1 = [int(x) for x in input().split()]
x2, y2, z2 = [int(x) for x in input().split()]

result = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))
print(format(result, ".2f"))
