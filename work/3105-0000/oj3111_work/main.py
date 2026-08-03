"""[LEARNING LOGS] สหกรณ์โรงเรียน"""
from math import floor
is_member = input() == "Y"
n, total = int(input()), 0

while n:
    total += float(input())
    n -= 1

def round_half_up(x):
    """ปัดเศษมาตรฐาน"""
    return floor(x * 100 + 0.6) / 100

if is_member:
    result = round_half_up(total - (total * 0.05))
elif total >= 500:
    result = round_half_up(total - (total * 0.03))
else:
    result = total
print(f"{result:.2f}")
