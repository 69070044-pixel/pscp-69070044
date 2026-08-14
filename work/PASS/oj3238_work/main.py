"""Elon Musk (X-shape)"""
n, ch = input().split()
n, ascii_id, current_id = int(n), ord(ch), 0
current_id = ascii_id + n // 2
for i in range(n):
    text = ""
    for j in range(n):
        if i == j or i + j == n - 1: # crossline position
            if ch == "#":
                text += "#"
            elif i <= n // 2: # upside before middle
                text += chr(current_id - i)
            elif i > n // 2: # bottomside after middle
                if not n % 2:
                    text += chr(current_id - (n - i)) # center is square
                else:
                    text += chr(current_id - (n - i - 1)) # center is one char
        else:
            text += "-" # not crossline
    print(text)
