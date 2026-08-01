"""Ticket"""
age, day = input().split()
price = 0
if 5 <= int(age) <= 18:
    price = 100
elif int(age) > 18:
    price = 150

if day.casefold() == 'wed':
    price *= 0.5
print(int(price))
