"""Filter"""
import json

data = json.loads(input().replace("'", '"'))
filter_score = float(input())
result = []
for sid, score in sorted(data.items(), key=lambda id: int(id[0])):
    if score >= filter_score:
        result.append([sid, f"{score:.2f}"])
if result:
    for s in result:
        print(*s, sep="\t")
else:
    print("Nope")
