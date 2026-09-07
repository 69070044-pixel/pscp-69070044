"""BUU"""
def main():
    """Main function"""
    text = input()
    if "buu" in text.casefold():
        maxu = 0
        utext = [x for x in text.casefold().split("b") if x.startswith("u")]
        for u in utext:
            maxu = max(maxu, u.count("u"))
        print("Yes", maxu)
    elif "b" in text.lower():
        whereis_b = text.lower().find('b')
        newtext = text[:whereis_b + 1]
        print(newtext + "U"*(len(text) - len(newtext)))
    else:
        print(("BUU" * len(text))[:len(text)])
main()
