"""List Prime"""
def is_prime(x):
    """check is prime number"""
    if x == 1:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if not x % i:
            return False
    return True

n = int(input())
if is_prime(n):
    prime_memo = list(n for n in range(2, n + 1) if is_prime(n))
    print("Yes")
    print(*prime_memo)
else:
    print("No")
