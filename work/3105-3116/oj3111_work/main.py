"""[LEARNING LOGS] สหกรณ์โรงเรียน"""
from math import ceil
is_member = input() == "Y"
n, total = int(input()), 0

while n:
    total += float(input())
    n -= 1

def round_half_up(x):
    """ปัดเศษมาตรฐาน"""
    return ceil(x * 100) / 100

if is_member:
    total *= 0.95
elif total >= 500:
    total *= 0.97

print(f"{round_half_up(total):.2f}")
