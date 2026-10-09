"""star"""
n = int(input())

def showstar(num):
    """sp print"""
    if num >= 1:
        print("*"*num)

showstar(n)
showstar(n - 2)
showstar(n - 4)
