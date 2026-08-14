"""รหัสแฝดเทค"""
n = int(input())
a, b, count = input(), input(), 0
for i in range(0, n):
    if not int(a[i]) + int(b[i]) == 9:
        count += 1
if count:
    print("NO", count)
else:
    print("YES")
