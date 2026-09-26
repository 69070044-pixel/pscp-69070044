"""HorizontalHistogram"""
txt = input()
charset = "abcdefghijklmnopqrstuvwxyz"
charset += charset.upper()

def convert_txt(text):
    """create count txt"""
    count = 0
    result = ''
    while result.count('-') != len(text):
        if count == 5:
            result += '|'
            count = 0
        result += '-'
        count += 1
    return result

for ch in charset:
    if ch in txt:
        c_len = txt.count(ch)
        output = '-' * c_len
        print(ch, ":", convert_txt(output))
