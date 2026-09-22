"""ลอดสะพาน"""
road_len, n = [int(x) for x in input().split()]
data = []
for _ in range(n):
    data.append([int(x) for x in input().split()])

i, max_pass = 0.5, 0
while i < road_len:
    passcount = 0
    for pair in data:
        if pair[0] < i < pair[1]:
            passcount += 1
    max_pass = max(max_pass, passcount)
    i += 0.5
print(max_pass)
