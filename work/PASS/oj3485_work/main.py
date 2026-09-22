"""รหัสต้องไม่ซ้ำกัน"""
_ = int(input())
code_id = sorted([int(x) for x in input().split()])
print(*list(x for x in code_id if code_id.count(x) == 1))
