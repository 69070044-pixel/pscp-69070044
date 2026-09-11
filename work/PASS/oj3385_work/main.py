"""Bus Stop I"""
p_max, station, data, bus_seat = int(input()), int(input()), {}, []
for _ in range(station):
    s = [int(x) for x in input().split()]
    data[s[0]] = s[1:]

count = 0
for i in sorted(data.keys()):
    count += bus_seat.count(i)
    bus_seat = [remain for remain in bus_seat if remain != i]

    for j in data[i]:
        if j > i and len(bus_seat) < p_max:
            bus_seat.append(j)
print(count)
