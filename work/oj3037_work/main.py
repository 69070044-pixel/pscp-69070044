"""OJ3037"""
max_value = int(input())
i = 0
while i != 2:
    x = int(input())
    if max_value < x:
        max_value = x
    i += 1
print(max_value)
