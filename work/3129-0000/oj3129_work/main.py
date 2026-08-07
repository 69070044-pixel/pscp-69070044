"""วิเคราะห์ยอดขายร้านกาแฟ"""
n = int(input())
data = []
while n:
    data.append(float(input()))
    n -= 1
print(int(sum(data)))
print(int(max(data)))
print(int(min(data)))
print(round(sum(data) / len(data), 1))
