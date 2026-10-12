"""3nPlus1"""
def three_n_plus_one(num, c=0):
    """count จำนวนในลำดับ"""
    while num != 1:
        c += 1
        if not num % 2:
            num /= 2
        else:
            num = (num * 3) + 1
    return c + 1

def main():
    """main funcion"""
    result = []
    while True:
        n = int(input())
        if not n:
            break
        result.append(three_n_plus_one(n))
    print(*result, sep="\n")

main()
