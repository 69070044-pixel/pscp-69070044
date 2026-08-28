"""Electric_Using"""
def ft_cal(unit):
    """FT rate 0.50 per unit calculate"""
    return 0.50 * unit

def vat_cat(x):
    """VAT 7% calculate"""
    return x * 0.07

used_unit = int(input())
total, cal_unit = 0, used_unit
# Unit 1 – 10 = 5 Baht Per Unit
# Unit 11 – 50 = 7 Baht Per Unit
# Unit 51 – 100 = 10 Baht Per Unit
# Unit 101 – 200 = 12 Baht Per Unit
# Unit 201 เป็นต้นไป = 15 Baht Per Unit
if used_unit > 200:
    total += (15 * (used_unit - 200))
    cal_unit = 200
if 101 <= cal_unit <= 200:
    total += (12 * (cal_unit - 100))
    cal_unit = 100
if 51 <= cal_unit <= 100:
    total += (10 * (cal_unit - 50))
    cal_unit = 50
if 11 <= cal_unit <= 50:
    total += (7 * (cal_unit - 10))
    cal_unit = 10
if 1 <= cal_unit <= 10:
    total += (5 * cal_unit)

print(f"{(total + ft_cal(used_unit) + vat_cat(total)):.1f}")
