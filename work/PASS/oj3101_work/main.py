"""Liquid Status"""
temp, unit = int(input()), input()

if unit in ('F', 'f'):
    temp = (temp - 32) * 5/9

if temp >= 100:
    print("gas")
elif 0 < temp < 100:
    print("liquid")
elif temp <= 0:
    print("solid")
