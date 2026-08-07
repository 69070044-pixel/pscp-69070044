"""OJ3027"""
width, height, floor = [int(x) for x in input().split()]
price = int(input())
length = (width + height) * 2

use_length = length * floor
total = use_length * price
print(use_length)
print(total)
