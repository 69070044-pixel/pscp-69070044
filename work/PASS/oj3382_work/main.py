"""Backward"""
data = []
while True:
    value = input()
    if value == "NULL":
        break
    data.append(value)
print(*reversed(data), sep="\n")
