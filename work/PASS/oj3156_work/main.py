"""conan"""
text, k = input(), int(input())
charset, newtext = 'abcdefghijklmnopqrstuvwxyz', ''
for char in text:
    decoded_index = (charset.index(char) + k) % len(charset)
    newtext += charset[decoded_index]
print(newtext)
