"""OJ3011 [LEARNING LOGS]"""

def main():
    """main function"""
    color_0 = input()
    color_1 = input()

    color_set = {'Red':0, 'Yellow':1, 'Blue':2}
    primary_c = color_set.keys()
    if color_0 not in primary_c or color_1 not in primary_c:
        print("Error")
        return
    
    color = (color_set[color_0], color_set[color_1])
    if color == (0, 1) or color == (1, 0):
        print("Orange")
    elif color == (0, 2) or color == (2, 0):
        print("Violet")
    elif color == (1, 2) or color == (2, 1):
        print("Green")
    else:
        print("Error")
main()
