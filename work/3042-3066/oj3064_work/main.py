"""Birthdate"""
import datetime

y1, m1, d1 = int(input()), int(input()), int(input())
y2, m2, d2 = int(input()), int(input()), int(input())

person1 = datetime.datetime(y1, m1, d1)
person2 = datetime.datetime(y2, m2, d2)
diff_days = (person1 - person2).days
if -7 <= diff_days <= 7:
    print(0)
else:
    print(1 if diff_days < 0 else 2)
