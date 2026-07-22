"""OJ3020"""
def main():
    """main"""
    full_price = int(input())
    cap_req = int(input())
    dis_price = int(input())
    wanted_item = int(input())
    if not cap_req or not wanted_item:
        # don't have discount price T_T and don't want to buy
        print(wanted_item * full_price)
        return
    get_free = (wanted_item - 1) // cap_req # หาจำนวนที่ได้ลดราคา
    # นำจำนวนที่ได้ฟรีมาหักกับที่ต้องการได้จำวนที่จ่ายเต็ม
    full_buy = wanted_item - get_free
    total = (full_buy * full_price) + (get_free * dis_price) # รวมค่าใช้จ่ายทั้งหมด
    print(total)
main()
