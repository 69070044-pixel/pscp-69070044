"""find aeiou"""
n = int(input())
count = 0
while n:
    sara = input().casefold()
    if sara in ('a', 'e', 'i', 'o', 'u'):
        count += 1
    n -= 1
print(count)
