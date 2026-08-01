"""Basic ATM"""

def atm(value, balance):
    """return balance // value , balance % value"""
    return balance // value, balance % value

def main():
    """main function to run module"""
    cash = int(input())
    if cash % 100 or not 100 <= cash <= 20000:
        print("ERROR")
        return # Stop working found error

    for v in [1000, 500, 100]:
        count, cash = atm(v, cash)
        if count:
            print(f"{v} = {count}")
main()
