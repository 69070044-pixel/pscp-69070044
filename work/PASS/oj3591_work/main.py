"""Olympic"""
n, scoreboard = int(input()), []
for _ in range(n):
    scoreboard.append([int(x) if x.isdigit() else x for x in input().split()])

scoreboard.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))
medal_data = []
for i, v in enumerate(scoreboard):
    if v[1:] in medal_data:
        print(medal_data.index(v[1:]) + 1, *v, sum(x if isinstance(x, int) else 0 for x in v))
    else:
        print(i + 1, *v, sum(x if isinstance(x, int) else 0 for x in v))
    medal_data.append([v[1], v[2], v[3]])
