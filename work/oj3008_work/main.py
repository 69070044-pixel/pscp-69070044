"""OJ3008"""
import math as m

a = float(input())
b = float(input())
c = float(input())

s = sum([a, b, c])/2

area = m.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"{area:.3f}")
