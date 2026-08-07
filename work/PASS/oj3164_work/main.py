"""ผลรวมของค่าที่มากกว่า"""
n, numbox = int(input()), []
while n:
    a, b = int(input()), int(input())
    numbox.append(max([a, b]))
    n -= 1
if len(numbox) == 1:
    print(numbox[0])
else:
    print(" + ".join([str(x) for x in numbox]), f"= {sum(numbox)}")
