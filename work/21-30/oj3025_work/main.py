"""OJ3025 [LEARNING LOGS]"""
month = int(input())
day = int(input())

if not month % 3 and day >= 21:
    # ฤดูกาลจะเปลี่ยนไปตั้งแต่วันที่ 21 ของเดือนที่ 3 หารลงตัว
    month += 1

# cycle is winter > spring > summer > fall > winter > ...
if month in [1, 2, 3, 13]: # 13 คือเดือน 12 ที่มากกว่าวันที่ 21
    print("winter")
elif month in [4, 5, 6]:
    print("spring")
elif month in [7, 8, 9]:
    print("summer")
elif month in [10, 11, 12]:
    print("fall")
