"""คำนวณราคาสินค้าโปรโมชั่น"""
from math import floor
item_quantity = [int(x) for x in input().split()]
price_data = [25, 40, 55]
total = 0
for index, price in enumerate(price_data):
    total += item_quantity[index] * price

if sum(item_quantity) >= 3:
    total -= total * 0.1

print(int(floor(total)))
