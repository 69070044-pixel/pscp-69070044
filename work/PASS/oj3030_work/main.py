"""OJ3030"""
wit = float(input())
sit = float(input())
stand = float(input())
run = float(input())
wit_p = float(input())
sit_p = float(input())
run_p = float(input())
stand_p = float(input())

def celi(a, b):
    """
    หารปัดเศษขึ้น
    return a / b
    """
    if not a % b:
        return int(a / b)
    return int((a / b) + 1)

wit_day = celi(wit, wit_p)
sit_day = celi(sit, sit_p)
stand_day = celi(stand, stand_p)
run_day = celi(run, run_p)

print(max([wit_day, sit_day, stand_day, run_day]))
