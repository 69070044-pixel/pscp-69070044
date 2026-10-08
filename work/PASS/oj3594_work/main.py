"""1132-Median"""
data = sorted([float(x) for x in input().split(',')])
def median(n):
    """median calculate"""
    mid = len(n) // 2
    if len(n) % 2:
        return n[mid]
    return (n[mid - 1] + n[mid]) / 2

print(f"{median(data):.2f}")
