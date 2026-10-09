"""how many people"""
male, female = 0, 0
while True:
    cid = int(input())
    if cid < 0:
        break
    if cid % 2:
        male += 1
    else:
        female += 1
print(male, female, male + female)
