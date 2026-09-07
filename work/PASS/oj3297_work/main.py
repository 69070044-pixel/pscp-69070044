"""Movie Ticket"""
seat_remain = int(input())
while seat_remain:
    try:
        age, seat = [int(x) for x in input().split()]
    except EOFError:
        break
    if age < 15:
        print(-1)
    elif seat_remain < seat:
        print(-2)
    else:
        seat_remain -= seat
        if 15 <= age <= 22:
            price = (seat * 150) * 0.8
        elif age >= 60:
            price = (seat * 150) * 0.5
        else:
            price = seat * 150
        print(int(price), seat_remain)
