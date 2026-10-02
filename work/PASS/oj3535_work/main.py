"""Classify"""
sid = {}
while True:
    input_id = input()
    if input_id == "END":
        break
    year = int(input_id[:2])
    classid = int(input_id[2:4])
    try:
        sid[year][classid] += 1
    except KeyError:
        if year not in sid:
            sid[year] = {}
        sid[year][classid] = 1

for y, v in sorted(sid.items()):
    y_switch = False
    for i, c in sorted(v.items()):
        x = y if not y_switch else "--"
        print(x, i, c)
        y_switch = True
