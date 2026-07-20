"""OJ3031 [LEARNING LOGS]"""
S, n = [int(x) for x in input().split()]
position = []
PI = 3.1416
while n:
    position.append([int(x) for x in input().split()])
    n -= 1

for pos in position:
    x, y = pos #แจกพิกัดให้ x, y
    r_pow2 = x ** 2 + y ** 2 # หาค่า r^2
    current_area = PI * r_pow2 # พื้นที่ของ Ink เมื่อขยายไปถึงพิกัด x, y
    if not current_area % S:
        # ไม่มีเศษ
        print(int(current_area / S)) # area / rate = time
    else:
        # มีเศษ
        print(int(current_area / S) + 1)
