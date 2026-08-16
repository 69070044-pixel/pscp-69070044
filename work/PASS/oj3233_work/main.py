"""[LEARNING LOGS] สลากกินแบ่ง"""
jackpot = input().split()
lottery = input().split()
if lottery == jackpot:
    print(1000000)
elif lottery[1] == jackpot[1]:
    print(100000)
elif lottery[1][-3:] == jackpot[1][-3:]:
    print(2000 if lottery[0] == jackpot[0] else 200)
elif lottery[1][-2:] == jackpot[1][-2:]:
    print(1000 if lottery[0] == jackpot[0] else 100)
elif lottery[0] == jackpot[0]:
    print(20)
else:
    print(0)
