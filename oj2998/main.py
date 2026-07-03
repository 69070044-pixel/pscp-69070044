"""OJ2998"""
import math as m

q1 = float(input())
q2 = float(input())
p1 = float(input())
p2 = float(input())

result = (m.sqrt(m.pow(p1 - q1, 2) + m.pow(p2 - q2, 2)))
print(result)
