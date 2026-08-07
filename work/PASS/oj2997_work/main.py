"""OJ2997"""
import math as m

Rating_A = int(input())
Rating_B = int(input())
side = input()

if side.casefold() == 'a':
    result = 1 / (1 + m.pow(10, ((Rating_B - Rating_A) / 400)))
else:
    result = 1 / (1 + m.pow(10, ((Rating_A - Rating_B) / 400)))
print(f"{result:.2f}")
