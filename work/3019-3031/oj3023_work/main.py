"""OJ3023"""
n = int(input())
if n == 1:
    print(1)
else:
    LEN_OF_NUM = len(str(n)) + 1
    constant = 0
    if LEN_OF_NUM == 3:
        constant = -9
    elif LEN_OF_NUM == 4:
        constant = -108
    elif LEN_OF_NUM == 5:
        constant = -1107
    elif LEN_OF_NUM == 6:
        constant = -11106
    elif LEN_OF_NUM == 7:
        constant = -111105
    print((LEN_OF_NUM*n) + constant)
