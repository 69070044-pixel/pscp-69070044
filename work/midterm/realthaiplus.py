"""RealThaiPlus"""
from math import floor
wallet, days = int(input()), int(input())
credits = 1000
complete = 0
for _ in range(days):
    if credits >= 200:
        daycredits = 200
    else:
        daycredits = credits
    items = int(input())
    for _ in range(items):
        value = int(input())
        pay = floor(value * 0.4)
        gcredits = value - pay
        if wallet < pay:
            continue
        if gcredits <= daycredits and pay <= wallet and pay + gcredits >= value:
            complete += 1
            wallet -= pay
            daycredits -= gcredits
        elif (value - daycredits) <= wallet:
            complete += 1
            pay = value - daycredits
            wallet -= pay
            daycredits = 0
    if credits:
        credits -= (200 - daycredits)
print(complete, wallet, 1000 - credits, sep="\n")
