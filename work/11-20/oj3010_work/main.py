"""OJ3010"""
x, y = int(input()), int(input())

if (x, y) == (0, 0):
    print("O")
elif not x or not y:
    print("Y" if not x else "X")
elif x > 0:
    if y > 0:
        print("Q1")
    else:
        print("Q4")
elif x < 0:
    if y > 0:
        print("Q2")
    else:
        print("Q3")
