"""PIZZA!"""
from math import ceil
party_member, k, m = int(input()), int(input()), int(input())
need_pizza = party_member * k
buy_pizza = ceil(need_pizza / m)
print(need_pizza, buy_pizza, (buy_pizza * m) - need_pizza, sep="\n")
