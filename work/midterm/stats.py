"""stats"""
n = int(input())
first = int(input())
big, small, total = first, first, first
for _ in range(n - 1):
    value = int(input())
    total += value
    if value > big:
        big = value
    if value < small:
        small = value

print(f"MIN: {small:.3f}")
print(f"MAX: {big:.3f}")
print(f"AVG: {(total / n):.3f}")
