"""OJ3024 [LEARNING LOGS]"""
sum_score = float(input())
max_score = float(input())
min_score = sum_score - (max_score * 2)

if min_score < 0:
    min_score = 0

if (max_score - min_score) > 2:
    print("Surprising")
else:
    print("Not surprising")
