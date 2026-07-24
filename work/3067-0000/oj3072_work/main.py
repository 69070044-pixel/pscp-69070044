"""[LEARNING LOGS] A-E-I-O-U"""
text = input().casefold()
for i in ['a', 'e', 'i', 'o', 'u']:
    char_count = text.count(i)
    if char_count:
        print(f"{i} : {char_count}")
