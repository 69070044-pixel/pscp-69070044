"""Fat Rabbit"""
n = int(input())
rabbits, maximum, count = {}, 0, 0
while n:
    rabbit, weight = input().split()
    weight = int(weight)
    if weight > 15:
        count += 1
    if maximum:
        if weight > maximum:
            maximum = weight
    else:
        maximum = weight
    rabbits[weight] = rabbit
    n -= 1
print(count, rabbits[maximum], sep="\n")
