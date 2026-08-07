"""factorial"""
n = int(input())
total = n
for i in range(n - 1, 0, -1):
    total *= i
print(total)
