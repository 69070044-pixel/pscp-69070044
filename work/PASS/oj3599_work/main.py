"""SumOfNumber"""
target, total = int(input()), 0
while target != total:
    num = int(input())
    if num == -1:
        break
    total += num
print(total)
