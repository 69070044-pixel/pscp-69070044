"""Flatten"""
num_list = input().replace("[", "").replace("]", "").split(',')
print(sorted(list(int(x) for x in num_list), reverse=True))
