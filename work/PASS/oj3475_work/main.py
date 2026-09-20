"""Muddled Menu"""

menu = []
while True:
    action = input()
    if action == "DONE":
        break
    if action == "CLOSED":
        menu.clear()
        break
    if "Can't do:" in action:
        _, name = action.split(":")
        menu.remove(name.strip())
        continue
    if action == "SOMETHING'S WRONG":
        menu.clear()
        continue

    name, index = action.split('#')
    if index == "N":
        menu.append(name.strip())
    else:
        menu.insert(int(index) - 1,name.strip())
print(f"Full Course: {menu} Reversed: {menu[::-1]}")
