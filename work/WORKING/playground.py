"""This is CODE Playground"""
txt = input()
charset = "abcdefghtiklmnopqrstuvwxyz"
sorttxt = "".join(sorted(ch for ch in txt))
for c in charset:
    sorttxt = sorttxt.replace(c*2, "")
for c in txt:
    if c in sorttxt:
        print(c, end="")
