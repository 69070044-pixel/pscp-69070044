"""OJ3014"""

milk_price = float(input())
cap_req = int(input())
milk_promo = int(input())
budget = float(input())

if not cap_req:
    print(budget // milk_price)
else:
    get_milk = budget // milk_price
    promo = get_milk // cap_req
    print(int(get_milk + (promo * milk_promo)))
