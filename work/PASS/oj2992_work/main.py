"""OJ2992"""
number = input()
if len(number) == 2:
    x = int(number)
    y = int(number[-1]+number[0])
    sign = input()
    if sign == "+":
        print(f"{x} + {y} = {x + y}")
    elif sign == "*":
        print(f"{x} * {y} = {x * y}")
