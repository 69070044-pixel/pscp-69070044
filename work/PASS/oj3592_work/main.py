"""Align"""
size, align, text = int(input()), input(), input()

match align:
    case "left":
        print(text.ljust(size))
    case "right":
        print(text.rjust(size))
    case "center":
        space = size - len(text)
        if not space % 2:
            print(f"{" " * (space // 2)}{text}{" " * (space // 2)}")
        else:
            print(f"{" " * ((space // 2) + 1)}{text}{" " * (space // 2)}")
