"""Kabata"""
n = int(input())
for _ in range(n):
    txt = input()
    kabata = ["bakka", "ba", "ka", "ta"]
    txt = txt.replace("baka", "XXXX")
    for word in kabata:
        txt = txt.replace(word, "#"*len(word))
    if txt.count("#") == len(txt):
        print("yes")
    else:
        print("no")
