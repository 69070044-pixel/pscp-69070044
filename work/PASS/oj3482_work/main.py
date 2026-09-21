"""Demon Slayer"""
demon_kill = {
    "Spider Demon": 1, "Swamp Demon": 2,
    "Arrow Demon": 1, "Hand Demon": 2,
    "Drum Demon": 3, "Mugen Train": 2,
    "Upper Moon": 3
}
demon_queue, atk, kill = list(demon_kill.keys()), 0, 0
while kill != 5:
    demon = demon_queue[0]
    stack = 0
    print(demon)
    while True:
        combo = int(input())
        atk += 1
        if combo == demon_kill[demon]:
            print("kill")
            kill += 1
            demon_queue.pop(0)
            break
        stack += 1

        if stack == 2:
            print("back")
            demon_queue.append(demon_queue.pop(0))
            break

print(atk)
