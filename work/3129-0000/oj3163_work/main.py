"""OJ3163"""
n, total, even, odd = int(input()), 0, 0, 0
while n:
    value = int(input())
    total += value
    if value % 2:
        odd += 1
    else:
        even += 1
    n -= 1
print("SUM", total)
print("EVEN", even)
print("ODD", odd)
