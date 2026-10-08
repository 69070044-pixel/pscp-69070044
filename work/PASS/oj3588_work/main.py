"""GCD_N"""
num_list = [int(input()) for _ in range(int(input()))]

def gcd(a, b):
    """gcd calculate"""
    num1, num2 = max(a, b), min(a, b)
    return gcd(num2, num1 % num2) if num2 else int(num1)

def gcd_n(nums: list):
    """gcd n numbers"""
    while True:
        if len(nums) >= 2:
            a, b = nums.pop(0), nums.pop(0)
            result = gcd(a, b)
            nums.insert(0, result)
        else:
            return nums[0]

print(gcd_n(num_list))
