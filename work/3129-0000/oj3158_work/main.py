"""OJ3158 ^2 sum"""
n = int(input())
numset = [int(x) ** 2 for x in range(1, n + 1)]
print(sum(numset))
