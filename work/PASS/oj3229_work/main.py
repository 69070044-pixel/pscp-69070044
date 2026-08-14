"""game score"""
base_score, bonus_score, play_stack = int(input()), int(input()), int(input())
multiple_score = 1 if play_stack <= 3 else 1.5
sumscore = int((base_score + bonus_score) * multiple_score)
rank, status_id = 0, 0
if sumscore >= 1500:
    rank = 5
    if play_stack >= 7:
        status_id = 99
elif sumscore >= 1000:
    rank = 4
    if bonus_score > 300:
        status_id = 88
elif sumscore >= 500:
    rank = 3
elif sumscore >= 200:
    rank = 2
else:
    rank = 1
print(sumscore,rank,status_id, sep="\n")
