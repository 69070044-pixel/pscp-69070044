"""light"""
color = ["Red", "Green", "Blue"]
start, light = input().split()
result, begin_index = [], 0
light = int(light)
if start == "R":
    begin_index = 0
elif start == "G":
    begin_index = 1
elif start == "B":
    begin_index = 2

while light:
    result.append(color[begin_index])
    begin_index = (begin_index + 1) % 3
    light -= 1
print(*result)
