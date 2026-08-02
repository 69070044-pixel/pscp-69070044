"""OJ3113 Rabbit and Ramen"""
menu = {
    "s": {"r":60, "t":80},
    "m": {"r":80, "t":100},
    "l": {"r":100, "t":120}
}

size, soup = input().casefold().split()
total = menu[size][soup]
topping = input().split()
if "N" in topping:
    print(total)
else:
    option, quantity = topping
    if option == "P":
        total += int(quantity) * 15
    elif option == "E":
        total += int(quantity) * 10
    print(total)
