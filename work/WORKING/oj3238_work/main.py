"""Elon Musk (X-shape)"""
n, ch = input().split()
n = int(n)
ascii_id, current_id = ord(ch), 0
if n % 2:
    current_id = ascii_id + n // 2
else:
    current_id = (ascii_id + n // 2) - 1
for i in range(n):
    text = ""
    for j in range(n):
        if i == j or i + j == n - 1:
            if ch == "#":
                text += "#"
            elif i == n / 2 or i == (n / 2) - 1:
                text = "-"*(int(n/2)-1) + f"{ch}"*2
                continue
            elif i <= n // 2:
                text += chr(current_id - i)
            elif i > n // 2:
                text += chr(current_id - (n - i - 1))
        else:
            text += "-"
    print(text)
