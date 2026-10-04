"""[LEARNING LOGS] B - Fully pair?"""
txt = input()
result = txt
for c in 'abcdefghijklmnopqrstuvwxyz':
    countchr = txt.count(c)
    if not countchr % 2:
        result = result.replace(c, '')
    else:
        result = result[::-1].replace(c, '', countchr - 1)[::-1]
print(result if result else "fully paired")
