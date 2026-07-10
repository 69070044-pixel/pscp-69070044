"""OJ3025 [LEARNING LOGS]"""
month = int(input())
day = int(input())

if not month % 3:
    if day >= 21:
        month += 1
        if month == 13:
            month = 1

if month in [1, 2, 3]:
    print("winter")
elif month in [4, 5, 6]:
    print("spring")
elif month in [7, 8, 9]:
    print("summer")
elif month in [10, 11, 12]:
    print("fall")
