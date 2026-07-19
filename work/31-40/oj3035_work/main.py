"""OJ3035"""
r, x, y = [int(x) for x in input().split()]

value = x ** 2 + y ** 2

if value == r ** 2:
    print("ON")
elif value < r ** 2:
    print("IN")
else:
    print("OUT")
