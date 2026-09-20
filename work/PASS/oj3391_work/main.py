"""magic coin"""
n, inv = int(input()), {"fire":0, "water":0, "earth":0}
for _ in range(n):
    data = [int(x) for x in input().split()]
    inv["fire"] += max(data[0], data[3])
    inv["water"] += max(data[1], data[4])
    inv["earth"] += max(data[2], data[5])
BONUS = inv["fire"] > inv["water"] + inv["earth"]
print("Total:", sum(inv.values()))
for i, v in inv.items():
    print(f"{i.capitalize()}:", v)
print("Bonus: YES" if BONUS else "Bonus: NO")
