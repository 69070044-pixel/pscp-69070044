"""OneTwo"""
n = int(input())
s_n = ["1", "2"]
if n > 1:
    for _ in range(2, n):
        s_n.append(f"{s_n[-1]+s_n[-2]}")
    print(s_n[-1])
else:
    print('1')
