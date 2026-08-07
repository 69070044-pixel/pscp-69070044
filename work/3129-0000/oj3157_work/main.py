"""[LEARNING LOGS] เกมสะสมแต้ม"""
n, total = int(input()), 0
while n:
    action = input() == "+"
    if action:
        total += 10
    else:
        total -= 5
    n -= 1
print(total)
