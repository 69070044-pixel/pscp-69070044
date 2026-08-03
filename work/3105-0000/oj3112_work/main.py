"""ชานมไข่มุก"""
additional = input().split()
tea, sweet, volumn = input().split()
menu = {
    "R": [12, 18, 25],
    "T": [15, 20, 30],
    "M": [10, 15, 20],
    "H": 5, "O": 3, "J": 2
}

cal = (menu[tea][int(sweet) - 1] * float(volumn)) + menu[additional[0]] * float(additional[1])

if cal - int(cal): # ex. 1.01 - 1 = 0.1 mean cal is float and if 1.00 - 1 = 0 mean is int
    print(float(cal))
else:
    print(int(cal))
