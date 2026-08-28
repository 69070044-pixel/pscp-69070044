"""Arrow"""
arrow_side, n = input(), int(input())
def right_arrow(x):
    """print right arrow"""
    space = 0
    for i in range(x, 0, -1):
        print(f"{" "*space}{"*"*i}")
        space += 2
    space -= 4
    for i in range(2, n + 1):
        print(f"{" "*space}{"*"*i}")
        space -= 2
    print()

def left_arrow(x):
    """print left arrow"""
    space = x - 1
    for i in range(x, 0, -1):
        print(f"{" "*space}{"*"*i}")
        space -= 1
    space += 2
    for i in range(2, x + 1):
        print(f"{" "*space}{"*"*i}")
        space += 1
    print()

for ch in arrow_side:
    if ch == "R":
        right_arrow(n)
    else:
        left_arrow(n)
