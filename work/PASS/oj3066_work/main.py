"""OJ3066"""
num1, num2, num3 = float(input()), float(input()), float(input())
if num1 == num2 == num3:
    print("all the same")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("neither")
else:
    print("all different")
