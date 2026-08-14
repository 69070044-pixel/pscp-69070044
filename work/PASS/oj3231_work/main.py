"""เกมทายลูกเต๋า"""
g, r = int(input()), int(input())
def is_dice(x):
    """if x not in range 1-6 is False"""
    return 1 <= x <= 6
if is_dice(g) and is_dice(r):
    print("Correct!" if g == r else "Wrong!")
else:
    print("Invalid")
