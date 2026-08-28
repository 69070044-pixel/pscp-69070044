"""Right Arrow"""
k, n = int(input()), int(input())
center = (n // 2) + 1 # find center line number
for row in range(0, center):
    print(" "*(row), end="*"*k)
    print()
for row in range(center - 1, 0, -1):
    print(" "*(row - 1), end="*"*k)
    print()
