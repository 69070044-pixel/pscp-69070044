"""RealThaiPlus"""
from math import floor
wallet, days = int(input()), int(input())
monthcredits = 1000
complete, usage = 0, 0

def my_min(a, b):
    """my min function"""
    return a if a < b else b

for _ in range(days):
    daycredits = 200
    items = int(input())
    for _ in range(items):
        value = int(input())
        pay = floor(value * 0.4)
        gov_help = value - pay
        gov_help = my_min(gov_help, daycredits)
        gov_help = my_min(gov_help, monthcredits)
        real_pay = value - gov_help
        if wallet >= real_pay:
            wallet -= real_pay
            daycredits -= gov_help
            monthcredits -= gov_help
            usage += gov_help
            complete += 1
print(complete, wallet, usage, sep="\n")
