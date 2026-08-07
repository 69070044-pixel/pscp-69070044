"""ผ่านหรือไม่ ค่าเฉลี่ยรายวิชา"""
n, score = int(input()), []
while n:
    value = int(input())
    score.append(value)
    n -= 1

avr, compare_list = sum(score) / len(score), [50] * len(score)
print(f"{avr:.1f}")
if avr >= 60.0 and score >= compare_list:
    print("PASS")
else:
    print("FAIL")
