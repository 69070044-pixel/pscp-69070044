"""[LEARNING LOGS] หาจำนวนเฉพาะ"""
def is_prime(number: int) -> bool:
    """
    Check number it is prime or not
    return True or False
    """
    if number <= 1:
        return False

    # loop from 2 to root(number) + 1 if number % i แล้วลงตัวแปลว่า not prime
    for i in range(2, int(number**0.5) + 1):
        # ถ้าเจอว่าหารลงตัว แปลว่า number มีตัวประกอบอื่นนอกจาก 1 กับตัวมันเอง
        if not number % i:
            return False

    return True

# input().split() -> ["a", "b"] -> str () > int() in for loop -> give value to a, b
a, b = [int(x) for x in input().split()]
# loop from a, to b + 1 if is_prime(x) return True append to list
prime_num = [x for x in range(a, b + 1) if is_prime(x)]
# print all in list and len of member
if prime_num:
    print(*prime_num)
print(f"Total primes: {len(prime_num)}")
