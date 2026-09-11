"""Rabit"""
castword = input()
lowword = castword.casefold()
pure_blood = False
def bloodline(w):
    for c in range(len(w)):
        # if c not in (0, len(w) - 1):
        prev, current, nxt = w[c - 1], w[c], w[c + 1]
        print(w[c - 1], w[c], w[c + 1], sep="-")
        if current == "r" and nxt == "a":
            return True
        elif current == 'a' and prev != 'r':
            return False
        elif current == 'b' and nxt in ('i', 't'):
            return True

        # else:
        #     print(f"0-{w[c]}-{w[c + 1]}" if c == 0 else f"{w[c - c]}-{w[c]}-0")
x = bloodline(lowword)
print(x)
