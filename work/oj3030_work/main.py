"""OJ3030"""
wit = float(input())
sit = float(input())
stand = float(input())
run = float(input())
wit_p = float(input())
sit_p = float(input())
run_p = float(input())
stand_p = float(input())

def slove(a, b):
    """
    หารปัดเศษ
    """
    if not a % b:
        return a / b
    return (a / b) + 1

wit_day = slove(wit, wit_p)
sit_day = slove(sit, sit_p)
stand_day = slove(stand, stand_p)
run_day = slove(run, run_p)

print(int(max([wit_day, sit_day, stand_day, run_day])))
