"""OJ3031 [LEARNING LOGS]"""
S, n = [int(x) for x in input().split()]
position = []
PI = 3.1416
while n:
    position.append([int(x) for x in input().split()])
    n -= 1

for pos in position:
    x, y = pos
    r_pow2 = x ** 2 + y ** 2
    current_area = PI * r_pow2
    if not current_area % S:
        print(int(current_area / S))
    else:
        print(int(current_area / S) + 1)
