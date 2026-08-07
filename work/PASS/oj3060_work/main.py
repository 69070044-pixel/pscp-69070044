"""check is a e i o u"""
char = input().casefold()
print('yes' if char in ('a', 'e', 'i', 'o', 'u') else 'no')
