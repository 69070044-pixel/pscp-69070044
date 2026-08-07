"""เดินเล่นในงานเทศกาล"""
move = input()
x = move.count("E") - move.count("W")
y = move.count("N") - move.count("S")
print(x, y, abs(x) + abs(y))
