"""OJ3067"""
num1, num2, num3 = float(input()), float(input()), float(input())
if num1 < num2 < num3:
    print("increasing")
elif num1 > num2 > num3:
    print("decreasing")
else:
    print("neither")
