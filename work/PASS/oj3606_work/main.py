"""Ball"""
h = float(input())

def reflex_cal(const, high, c=-1):
    """calculate function"""
    if high in (0, 1):
        return 0
    if high > 1:
        return reflex_cal(const, high * (const), c + 1)
    return c

print(reflex_cal(3/5, h * 100))
