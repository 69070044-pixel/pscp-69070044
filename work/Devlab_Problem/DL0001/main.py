"""On/Off switch grab item"""
switch1, switch2 = input() in ("On"), input() in ("On")
if switch1 and switch2:
    print("Hand me a glass of water")
elif switch1 and not switch2:
    print("Hand me a pair of glasses")
else:
    print("Hand me a towel to wipe my face" if switch2 else "Hand me a blanket")
