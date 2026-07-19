"""OJ3005"""
quantity = [int(x) for x in input().split()]
price = [10, 25, 3]
total = 0
for i, q in enumerate(quantity):
    total += (q*price[i])
print(total)
