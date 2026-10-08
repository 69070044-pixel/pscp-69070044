"""GCD V2"""
def gcd(a, b):
    """gcd calculate"""
    num1, num2 = max(a, b), min(a, b)
    return gcd(num2, num1 % num2) if num2 else int(num1)

n1, n2 = float(input()), float(input())
print(gcd(n1, n2))
