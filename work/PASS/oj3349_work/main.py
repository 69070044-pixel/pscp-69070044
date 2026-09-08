"""กองชาม"""
n, bowl = int(input()), [[]]
for _ in range(n):
    size = int(input())
    for c in bowl:
        if size not in c:
            c.append(size)
            break
    else:
        bowl.append([size])
print(len(bowl))
