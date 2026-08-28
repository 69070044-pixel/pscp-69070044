"""triangle"""
a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("EQUILATERAL")
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 - c ** 2 == b ** 2:
        print("RIGHT TRIANGLE")
    elif a == b or b == c or c == a:
        print("ISOSCELES")
    else:
        print("SCALENE")
else:
    print("NOT A TRIANGLE")
