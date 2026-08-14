"""Fat Rabbit"""
n, rabbit, maximum, count = int(input()), "", 0, 0
for _ in range(n):
    name, weight = input().split()
    weight = int(weight)
    if weight > 15:
        count += 1
    if weight > maximum:
        maximum = weight
        rabbit = name
print(count, rabbit, sep="\n")
