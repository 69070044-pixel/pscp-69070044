"""[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
a, b, d, r = int(input()), int(input()), int(input()), int(input())
total_count = 0
for i in range(a, b + 1):
    if i % d == r:
        total_count += 1
print(total_count)
