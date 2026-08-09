"""N6_ตรวจสอบพหุนามแซลม่อน"""
salmon = input().split("+")
notcorrect, correct = [], []
for i in salmon:
    a, b = i.split("x^")
    if a != b:
        correct.append(f"{b}x^{b}")
        notcorrect.append(f"x^{b}")
    else:
        correct.append(i)
print(len(notcorrect))
if notcorrect:
    print(*notcorrect, sep="\n")
else:
    print("None")
print("+".join(correct).replace("1x^1", "x^1"))
