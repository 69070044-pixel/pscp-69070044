"""ใส่กล่อง"""
W, L, M, N = [int(x) for x in input().split()]
result = []
for i in range(M, N + 1):
    area = W * L
    box = i * L
    w, l = L, (W - ((W // i) * i))
    # area ทั้งหมด - พื้นที่ๆ ใช้ในแนวนอน - พื้นที่ๆ ใช้ในแนวตั้ง
    empty = area - (box * (W // i)) - ((i * l) * (w // i))
    result.append(empty)
print(min(result))
