"""1-9 Roman"""
roman_num = [
    "I", "II", "III",
    "IV", "V", "VI",
    "VII", "VIII", "IX"
]

number = int(input())
if number < 0:
    print("Error : Please input positive number")
elif 1 <= number <= 9:
    print(roman_num[number - 1])
else:
    print("Error : Out of range")
