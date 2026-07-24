"""OJ3069"""
day, month = int(input()), int(input())
date = (month, day)
zodiac_list = [
    # ราศี, startdate in range, stop date in range
    ["aquarius", (1, 20), (2, 18)],
    ["pisces", (2, 19), (3, 20)],
    ["aries", (3, 21), (4, 19)],
    ["taurus", (4, 20), (5, 20)],
    ["gemini", (5, 21), (6, 21)],
    ["cancer", (6, 22), (7, 22)],
    ["leo", (7, 23), (8, 22)],
    ["virgo", (8, 23), (9, 22)],
    ["libra", (9, 23), (10, 23)],
    ["scorpio", (10, 24), (11, 21)],
    ["sagittarius", (11, 21), (12, 21)]
]

if (12, 22) <= date or date <= (1, 19):
    print("capricorn")
else:
    for z, start, stop in zodiac_list:
        # ราศี, startdate in range, stop date in range
        if start <= date <= stop: # compare date range
            print(z)
            break # stop if found already.
