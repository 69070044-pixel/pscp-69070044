"""ไพ่ 44"""
card = input().casefold()
cardtype, group = card[:-1], card[-1]
fullname = {
    "s": "spades", "d": "diamonds",
    "h": "hearts", "c": "clubs",
    "a": "ace", "j": "jack",
    "q": "queen", "k": "king"
}
if cardtype in fullname:
    print(f"{fullname[cardtype]} of {fullname[group]}")
else:
    print(f"{cardtype} of {fullname[group]}")
