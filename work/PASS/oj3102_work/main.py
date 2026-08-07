"""car tax"""
year, cc = int(input()), int(input())
tax, idx = 0, 0
value = [
    [1250, 1400, 2000],
    [1100, 1300, 1700],
    [1000, 1200, 1500]
]

if year <= 1990:
    idx = 0
elif 1990 < year < 2000:
    idx = 1
elif year >= 2000:
    idx = 2

if cc <= 1500:
    tax = value[idx][0]
elif 1500 < cc <= 2000:
    tax = value[idx][1]
elif cc > 2000:
    tax = value[idx][2]

print(tax)
