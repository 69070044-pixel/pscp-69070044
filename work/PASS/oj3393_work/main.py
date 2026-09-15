"""Cave Explorer"""
n, cave_map = int(input()), input().split()
gold = cave_map.index("2")
move = input()

def cave_render(new, old):
    """render cave from action"""
    cave_map[new] = "1"
    if old == gold:
        cave_map[old] = "2"
    else:
        cave_map[old] = "0"

for action in move:
    explorer_pos = cave_map.index('1')
    if action == "L" and explorer_pos:
        cave_render(explorer_pos - 1, explorer_pos)
    elif action == "R" and explorer_pos != n - 1:
        cave_render(explorer_pos + 1, explorer_pos)

print(*cave_map)
