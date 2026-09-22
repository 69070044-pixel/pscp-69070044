"""Easy Histogram No Dict"""
def main():
    """Main function"""
    text = input()
    charset = "abcdefghijklmnopqrstuvwxyz"
    for c in charset:
        if c in text:
            print(f"{c} = {text.count(c)}")
        if c.upper() in text:
            print(f"{c.upper()} = {text.count(c.upper())}")
main()
