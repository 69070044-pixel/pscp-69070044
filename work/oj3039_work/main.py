"""OJ3039"""
n = int(input())
i = 0
min_value = int(input())
while i != n - 1:
    x = int(input())
    if x < min_value:
        min_value = x
    i += 1
print(min_value)
