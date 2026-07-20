"""OJ3014"""

milk_price = float(input()) # milk full price
cap_req = int(input()) # cap require for trade free milk
free = int(input()) # get free (n) milk
budget = float(input()) # customer budget

if not cap_req:
    # no free trade
    print(int(budget // milk_price))
else:
    milk = int(budget // milk_price)  #budget can buy n milk
    cap = milk # cap in inventory

    while cap >= cap_req: # if cap enough to trade
        cap -= cap_req # throw used cap
        milk += free # add free n milk for customer
        cap += free # get free milk mean have more cap

    print(milk)
