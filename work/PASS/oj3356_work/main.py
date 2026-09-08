"""Bus Seat"""
r, c, seat = int(input()), int(input()), int(input())
textid = ""
for i in range(1, (r * c) + 1):
    if not i % r:
        textid += f"{i:>02}," if i != seat else "XX,"
    else:
        textid += f"{i:>02} " if i != seat else "XX "

seat_id = textid.strip(",").split(",")
row = [c.split()[::-1] for c in seat_id]

y = 1
for s in range(r):
    bus = ""
    for e in row:
        bus += f"{e[s]} "
    print(bus.strip())
    if y == 2 and s != r - 1:
        print()
        y = 0
    y += 1
