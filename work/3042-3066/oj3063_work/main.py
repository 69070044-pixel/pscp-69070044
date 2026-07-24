"""Password"""
char_pass = input()
digit_pass = input()

if (char_pass, digit_pass) == ("H", "4567"):
    print("safe unlocked")
elif char_pass == "H":
    print("safe locked - change digit")
elif digit_pass == "4567":
    print("safe locked - change char")
else:
    print("safe locked")
