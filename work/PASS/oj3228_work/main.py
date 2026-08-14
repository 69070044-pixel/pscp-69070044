"""aeiou"""
vowels, count = "aeiou", 0
word = input().casefold()
for ch in vowels:
    count += word.count(ch)
print(count)
