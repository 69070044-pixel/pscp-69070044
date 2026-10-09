"""Heads and Legs"""
a, b = int(input()), int(input())
_2leg = b // 2
rabbit = int(_2leg - a)
bird = int(a - rabbit)
if not b % 2 and rabbit >= 0 and bird >= 0:
    print(rabbit, bird)
else:
    print("Impossible")
