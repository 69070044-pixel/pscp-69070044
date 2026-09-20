"""Smart Trash Collector"""
n, items, result = int(input()), [], []
item_type = ["Plastic", "Can", "Glass"]
for i in range(n):
    items.append([float(x) for x in input().split()])

for i in items:
    result.append([])
    total = sum(i)
    result[-1].append(f"{total:.1f}")
    if total > 50.0:
        result[-1].append("Overloaded")
    for j, value in enumerate(i):
        if value > 20.0:
            result[-1].append(f"Check Type {item_type[j]}")
for i in result:
    print(", ".join(i))
