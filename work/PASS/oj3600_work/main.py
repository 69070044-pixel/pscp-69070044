"""calories"""
calories, total = {1: 100, 2: 120, 3: 200, 4: 60}, 0
while True:
    order = int(input())
    if order == 5:
        break
    total += calories[order]
print("Bye Bye")
print(f"Total Calories: {total}")
