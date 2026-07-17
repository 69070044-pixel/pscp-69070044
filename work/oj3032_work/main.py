"""OJ3032"""
n = int(input())
scores = []
i = 0
while i != n:
    scores.append(float(input()))
    i += 1
maximum = max(scores)
print(int(maximum))
print(scores.count(maximum))
