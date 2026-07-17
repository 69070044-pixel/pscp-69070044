"""OJ3040"""
credit_value = int(input())

def coin(v):
    """
    This function to count coin
    return coin10, coin5, coin2, coin1
    """
    c10 = v // 10
    c5 = (v - (10 * c10)) // 5
    c2 = (v - (10 * c10) - (5 * c5)) // 2
    c1 = (v - (10 * c10) - (5 * c5) - (2 * c2))
    return c10, c5, c2, c1

coin_10, coin_5, coin_2, coin_1 = coin(credit_value)
print("10 =", coin_10)
print("5 =", coin_5)
print("2 =", coin_2)
print("1 =", coin_1)
