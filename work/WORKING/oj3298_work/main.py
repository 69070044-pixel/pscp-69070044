"""BUU"""
text = input().casefold()

buutext = "".join(ch for ch in text if ch in ('b', 'u'))
if buutext and "u" in buutext:
    u_count = [len(x) for x in buutext.split("b")]
    print(f"Yes {max(u_count)}")
elif buutext:
    new_bu = ' '
    for ch in text:
        if ch == "b":
            new_bu += "b"
        elif new_bu[-1] in ("b", "u"):
            new_bu += "u"
        else:
            new_bu += ch
    print(new_bu.upper().strip())
