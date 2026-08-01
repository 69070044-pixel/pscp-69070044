"""Bonus"""
position, years, salary = input().casefold().split()
bonus_data = {
    "m": [1500, [0.06, 0.08, 0.1]],
    "b": [1000, [0.05, 0.06, 0.07]],
    "g": [500, [0.04, 0.05, 0.06]]
}

def cal_bonus(data, year, sly):
    """return salary * bonus(%) + position_bonus"""
    pos_bonus = data[0]
    rate = data[1]
    if year < 5:
        return (sly * rate[0]) + pos_bonus
    if 5 <= year <= 10:
        return (sly * rate[1]) + pos_bonus
    return (sly * rate[2]) + pos_bonus

bonus = cal_bonus(bonus_data[position], int(years), int(salary))
print(int(bonus))
