"""OJ3022 [LEARNING LOGS]"""
temp = float(input())
unit = input()
wanted_unit = input()
cel = 0
if unit == "C":
    cel = temp
elif unit == "K":
    cel = temp - 273.15
elif unit == "F":
    cel = (temp - 32) * 5 / 9
elif unit == "R":
    cel = (temp * (5 / 9)) - 273.15
result = 0
if wanted_unit == "C":
    result = cel
elif wanted_unit == "K":
    result = cel + 273.15
elif wanted_unit == "F":
    result = (cel * 9 / 5) + 32
elif wanted_unit == "R":
    result = (cel + 273.15) * 9 / 5
print(format(result, ".2f"))
