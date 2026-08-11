"""รวมประโยคภาษาอังกฤษ"""
n = int(input())
text, first = [input().strip() for _ in range(n)], ""
result = []

def overlap(a: str, b: str) -> int:
    """Find overlapping len return integer value"""
    minlen = min(len(a), len(b))
    for i in range(minlen):
        if a[-i:] == b[:i]:
            return i
    return 0

z = 0
while not first:
    t = text[z]
    if t[0] == t[0].upper():
        first = t
        text.remove(t)
        z = 0
        continue
    z += 1

result.append(first)

index = 0
while text:
    overlappinglen = overlap(result[-1], text[index])
    if overlappinglen:
        result.append(text[index][overlappinglen:])
        text.remove(text[index])
        index = 0
        continue
    else:
        index += 1

print("".join(result))

...
# Problem : https://www.borntodev.com/devlab/task/307