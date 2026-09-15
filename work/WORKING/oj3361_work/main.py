"""sell car"""
n, data = int(input()), []
for _ in range(n):
    data.append([int(x) for x in input().split()])
v_max, cantsell = -1, 0
data.sort(key=lambda x: x[0])
for v in data:
    # ประสิทธิภาพของรถคันปัจจุบันน้อยกว่าประสิทธิภาพสูงสุดของรถรุ่นที่ราคาถูกกว่า (v_max) หรือไม่
    if v[1] < v_max:
        cantsell += 1
    else:
        v_max = v[1]
print(cantsell)
