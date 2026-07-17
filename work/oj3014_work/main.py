"""OJ3014"""

milk_price = float(input())
cap_req = int(input())
milk_free = int(input())
budget = float(input())

if not cap_req:
    print(int(budget // milk_price))
else:
    milk = int(budget // milk_price)
    cap = milk

    while cap >= cap_req:
        cap -= cap_req
        milk += milk_free
        cap += milk_free

    print(milk)
