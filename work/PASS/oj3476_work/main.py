"""[LEARNING LOGS] CuteCat CuteFox"""
import json
n, data, cat, fox = int(input()), {}, 0, 0
for _ in range(n):
    e = input()
    try:
        data.update(json.loads(e))
    except json.decoder.JSONDecodeError:
        data.update(json.loads(e.replace("'", '"')))

def call(key, value):
    """find data in dict and add if not found"""
    if value not in data.values() and key not in data:
        data.update({key: value})

call('Garfield', 'Cat01')
call('Fubuki', 'Fox01')

for v in data.values():
    if v.startswith("Cat"):
        cat += 1
    else:
        fox += 1

result = list(data.items())
result.sort(key=lambda x: (x[1][0] ,int(x[1][3:])))
# sort ด้วยอักษรตัว c และตามด้วย หมายเลข
print(f"Cat : {cat}")
print(f"Fox : {fox}")
for i in result:
    print(i[0], ":", i[1])
