"""OJ3032"""
n = int(input())
scores = []
for _ in range(0, n):
    scores.append(float(input()))
maximum = max(scores)
print(int(maximum))
print(scores.count(maximum))
