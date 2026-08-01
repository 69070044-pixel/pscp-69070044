"""Suvarnabhumi Airport Parking"""
from math import ceil

price_rate = {
    1 :	25, 2 :	50,
    3 :	80, 4 :	110,
    5 :	145, 6 : 180,
    7 :	250
}

h1, m1 = [int(x) for x in input().split(".")]
h2, m2 = [int(x) for x in input().split(".")]

starttime, endtime = m1 + (h1 * 60), m2 + (h2 * 60)
diff_m = endtime - starttime
diff_h = ceil(diff_m / 60)

hour_check = h1 > 23 or h2 > 23
minute_check = m1 >= 60 or m2 >= 60

if  hour_check or minute_check or diff_m < 0 or diff_m > 1440:
    print("ERROR")
elif 0 <= diff_m <= 15:
    print("FREE")
else:
    try:
        print(price_rate[diff_h])
    except KeyError:
        print(price_rate[7])
