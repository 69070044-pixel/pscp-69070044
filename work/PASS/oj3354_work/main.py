"""Hint"""
ones_place, tens_place, hundreds_place = input(), input(), input()
ones_place_num, tens_place_num, hundreds_place_num = [], [], []

def num_hint_gen(hint):
    """generate num in range"""
    condi, num = hint.split()
    condi, num = condi.strip(), num.strip()
    if condi == "==":
        return [num]
    if condi == ">":
        return [str(x) for x in range(int(num) + 1, 10)]
    if condi == ">=":
        return [str(x) for x in range(int(num), 10)]
    if condi == "<":
        return [str(x) for x in range(int(num) - 1, -1, -1)][::-1]
    if condi == "<=":
        return [str(x) for x in range(int(num), -1, -1)][::-1]
    return [str(x) for x in range(0, 10) if x != int(num)]

ones_place_num = num_hint_gen(ones_place)
tens_place_num = num_hint_gen(tens_place)
hundreds_place_num = num_hint_gen(hundreds_place)
for hundred in hundreds_place_num:
    for ten in tens_place_num:
        for one in ones_place_num:
            print(hundred + ten + one)
