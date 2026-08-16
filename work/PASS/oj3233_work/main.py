"""[LEARNING LOGS] สลากกินแบ่ง"""
jackpot = input().split()
lottery = input().split()
if lottery == jackpot:
    print(1000000)
elif lottery[1] == jackpot[1]:
    print(100000)
elif lottery[1][-3:] == jackpot[1][-3:]:
    if lottery[0] == jackpot[0]:
        print(2000)
    else:
        print(200)
elif lottery[1][-2:] == jackpot[1][-2:]:
    if lottery[0] == jackpot[0]:
        print(1000)
    else:
        print(100)
elif lottery[0] == jackpot[0]:
    print(20)
else:
    print(0)
