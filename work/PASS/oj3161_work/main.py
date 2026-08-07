"""OJ3161 พิมพ์สัญลักษณ์"""
n, i = int(input()), 1
while i != n + 1:
    print("*" if i % 5 else "X", end="")
    i += 1
