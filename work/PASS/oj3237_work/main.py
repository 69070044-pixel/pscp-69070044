"""[Recommend] สามเหลี่ยม"""
n = int(input())
for i in range(1, n + 1):
    if i in (1, 2, n):
        print("0"*i)
    else:
        print(f"0{"1"*(i - 2)}0")
