"""OJ2995"""
student_id = input()
pair_is_16 = [student_id[2], student_id[3]] == ['1', '6']
print("yes" if pair_is_16 else "no")
