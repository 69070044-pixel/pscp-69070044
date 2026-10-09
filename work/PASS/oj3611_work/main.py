"""Coffee Shop"""
price = float(input())
promo1 = float(input())
promo2, c_promo2 = float(input()), float(input())
wanted = float(input())

def pro1(price_per_coffee, dist_percent, buy):
    """calculate promo1"""
    price_per_coffee_dist = price_per_coffee - (price_per_coffee * (dist_percent / 100))
    return (price_per_coffee_dist * (buy - 1)) + price_per_coffee

def pro2(price_per_coffee, condi_promo, dist_percent, buy):
    """calculate promo2"""
    total = price_per_coffee * buy
    if total >= condi_promo:
        return total - (total * (dist_percent / 100))
    return price_per_coffee * buy

p1 = pro1(price, promo1, wanted)
p2 = pro2(price, c_promo2, promo2, wanted)
if p2 <= p1:
    print(2, f"{p2:.2f}", sep="\n")
else:
    print(1, f"{p1:.2f}", sep="\n")
