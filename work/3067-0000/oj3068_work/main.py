"""OJ3068"""
year = int(input())
if year < 1582:
    print("yes" if not year % 4 else "no")
elif not year % 4:
    if not year % 100 and not year % 400:
        print("yes")
    elif year % 100:
        print("yes")
    else:
        print("no")
else:
    print("no")
