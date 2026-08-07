"""Ticket price"""
age, status = int(input()), input().casefold()
if age < 18 or status in ('s'):
    print(20)
else:
    print(50)
