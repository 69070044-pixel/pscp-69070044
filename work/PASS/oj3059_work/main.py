"""OJ3059"""
work_score = int(input())
mid_score = int(input())
final_score = int(input())

work_score_percent = (work_score / 10) * 100
mid_score_percent = (mid_score / 40) * 100
final_score_percent = (final_score / 50) * 100

work_pass = work_score_percent > 50
mid_pass = mid_score_percent > 50
final_pass = final_score_percent > 50

if work_pass and mid_pass and final_pass:
    print("pass")
else:
    print("fail")
