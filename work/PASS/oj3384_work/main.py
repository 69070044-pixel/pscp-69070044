"""PickThem"""
import json
num = [x for x in json.loads(input()) if not x % 2]
if num:
    print(*num, sep="\n")
else:
    print("Nope")
