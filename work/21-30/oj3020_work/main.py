"""OJ3020"""
def main():
    """main"""
    price = int(input())
    item_req = int(input())
    dis_price = int(input())
    wanted_items = int(input())
    if not item_req:
        print(wanted_items * price)
        return

    current_items = 0
    collect_items = 0
    total = 0
    while current_items < wanted_items:
        if collect_items == item_req:
            total += dis_price
            current_items += 1
            collect_items = 1
        else:
            total += price
            current_items += 1
            collect_items += 1
    print(total)
main()
