"""come with team"""
n, m = [int(x) for x in input().split()]
score_sheet, total_of_all = [], 0
if 1 <= n <= 10 and 1 <= m <= 20:
    for _ in range(n):

        score_sheet.append([int(x) for x in input().split()])

    for t, s in enumerate(score_sheet):
        total_of_all += sum(s)
        print(f"Team {t + 1}: Average = {sum(s) / len(s):.2f}, Max = {max(s)}")
    print(f"Total Score of All Teams = {total_of_all}")
else:
    print("Data Incorrect")
