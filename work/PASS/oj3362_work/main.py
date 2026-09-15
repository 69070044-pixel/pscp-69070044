"""บุพเพสันนิวาส"""
name1, name2 = input().lower(), input().lower()
s1, s2 = len(name1), len(name2)
if s1 < s2:
    name1 += (name1 * s2)[:(s2 - s1)]
elif s2 < s1:
    name2 += (name2 * s1)[:(s1 - s2)]

output, w_count = "", 0
for i in range(max(s1, s2)):
    ch1, ch2 = name1[i], name2[i]
    love = ('l', 'o', 'v', 'e')
    if ch1 in love or ch2 in love:
        output += "w"
        w_count += 1
    else:
        output += "$"

longest_w = len(max(output.split("$")))
if w_count % 2:
    output += str(longest_w)
elif longest_w < 2:
    output += "#"

print(output)
