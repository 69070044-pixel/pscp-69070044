"""[LEARNING LOGS] Impostor"""
import json
players, died = {}, []
while True:
    add_player = input()
    if add_player == "Start":
        break
    players.update(json.loads(add_player))

while True:
    name = input()
    if name == "End":
        break
    died.append(name)

alive, dead, impos_remain = {}, {}, 0
for ply, role in players.items():
    if ply not in died:
        alive.update({ply : role})
        if role == "Impostor":
            impos_remain += 1
    else:
        dead.update({ply : role})

def playerlist(data):
    """Print List format"""
    for p, r in sorted(data.items()):
        print(p, ":", r)

print(impos_remain, "Impostor Remains")
print("***Alive***")
playerlist(alive)
print("***Dead***")
playerlist(dead)
