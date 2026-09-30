"""Sorry"""
items = []
while True:
    added = input()
    if added == "End":
        break
    if added == "Sorry":
        items.pop(-1)
    else:
        items.append(added)
print(*items, sep=", ")
