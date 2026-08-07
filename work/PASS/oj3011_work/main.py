"""OJ3011 [LEARNING LOGS]"""

def main():
    """main function"""
    color_0 = input().casefold()
    color_1 = input().casefold()

    color = (color_0, color_1)
    if color_0 == color_1 and color_0 in ("red", "yellow", "blue"):
        print(color_1.capitalize())
    elif color in (("red", "yellow"), ("yellow", "red")):
        print("Orange")
    elif color in (("red", "blue"), ("blue", "red")):
        print("Violet")
    elif color in (("yellow", "blue"), ("blue", "yellow")):
        print("Green")
    else:
        print("Error")
main()
