"""OJ3038"""
min_value = int(input())
i = 0
while i != 2:
    x = int(input())
    if min_value > x:
        min_value = x
    i += 1
print(min_value)
