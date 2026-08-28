"""Left Arrow"""
k, n = int(input()), int(input())
center = (n // 2) + 1 # find center line number
for row in range(center - 1, 0, -1):
    print(" "*(row), end="*"*k)
    print()
print("*"*k)
for row in range(1, center):
    print(" "*(row), end="*"*k)
    print()
