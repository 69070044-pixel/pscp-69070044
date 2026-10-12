"""ProgressiveTax_Midterm2014"""
sumincome = int(input())
def tax_f(income, rate, celi):
    """tax calculate"""
    return (income - celi) * (rate / 100)

def calculate_tax(income):
    """check to get taxceli and rate"""
    result = 0
    data_rate = [
        (0, 0), (150000, 5), (300000, 10), (500000, 15),
        (750000, 20), (1000000, 25), (2000000, 30), (4000000, 35)
    ]
    for low, rate in data_rate[::-1]:
        if income > low:
            result += tax_f(income, rate, low)
            income -= (income - low)
    return int(result)

print(calculate_tax(sumincome))
