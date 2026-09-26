"""ระบบจัดการคลังสินค้า"""
STOCK = {}

def add(name, amount):
    """add item"""
    try:
        STOCK[name] += int(amount)
    except KeyError:
        STOCK[name] = int(amount)

def remove(name, amount):
    """remove item"""
    try:
        current_amount = STOCK[name]
        if current_amount >= int(amount):
            STOCK[name] -= int(amount)
            return
        STOCK[name] = 0
    except KeyError:
        STOCK[name] = 0
    print(f"Not enough stock for {name}")

def check():
    """check stock"""
    items = list(x[0] for x in STOCK.items() if x[1] < 5)
    if items:
        items.sort()
        print(*items, sep="\n")
    else:
        print("All stocks are sufficient")

def report():
    """report stock"""
    items = list(STOCK.items())
    items.sort(key=lambda x: (x[0]))
    for name, value in items:
        print(f"{name}: {value}")

def main():
    """main function for control system"""
    while True:
        cmd = input().split()
        match cmd[0]:
            case "ADD":
                add(cmd[1], cmd[2])
            case "REMOVE":
                remove(cmd[1], cmd[2])
            case "CHECK":
                check()
            case "REPORT":
                report()
            case "END":
                break
main()
