"""OJ3032"""
n = int(input())
scores = []
while n:
    scores.append(float(input()))
    n -= 1
maximum = max(scores)
print(int(maximum))
print(scores.count(maximum))
