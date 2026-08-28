"""Code Cleaner"""
text = input().casefold()
code, letters, digits = "-", 0, 0
for ch in text:
    if ch in '0123456789':
        digits += 1
        code += ch
    elif ch in 'abcdefghijklmnopqrstuvwxyz':
        letters += 1
        code += ch.upper()
    elif code[-1] != "-":
        code += "-"
code = code.replace("-", " ").strip()
if not code:
    code = "NONE"
print(f"CODE = {code.replace(" ", "-")}")
print(f"LETTERS = {letters}")
print(f"DIGITS = {digits}")
