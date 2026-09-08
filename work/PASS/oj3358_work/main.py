"""Pig"""
n, w, result = int(input()), [int(x) for x in input().split()], []
for _ in range(n):
    result.append(max(w[0], w[1]))
    del w[0:2]
if len(result) > 1:
    print(f"{" + ".join([str(r) for r in result])} = {sum(result)}")
else:
    print(sum(result))
