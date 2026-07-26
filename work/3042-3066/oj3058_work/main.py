"""[LEARNING LOGS] BrickBridge"""
small_brick = int(input())
big_brick = int(input())
goal = int(input())

need_big_brick = goal // 5 # หาจำนวนก้อนให้ที่มาที่สุดที่ต้องใช้
if need_big_brick <= big_brick:
    # จำนวนที่ต้องการก้อนใหญ่ที่ใช้มีพอ
    small_brick_use = goal - (need_big_brick * 5) # เอาก้อนใหญ่แค่ที่ใช้ไป * 5 เพื่อหาระยะที่ต่อได้
else:
    # ก้อนใหญ่ใช้หมดแล้วไม่พอต้องต่อก้อนเล็กเพิ่ม
    small_brick_use = goal - (big_brick * 5) # เอาก้อนใหญ่ทั้งหมดใช้ไป * 5 เพื่อหาระยะที่ต่อได้

if small_brick >= small_brick_use:
    #  check ว่าก่อนเล็กมีพอมั้ย
    print(small_brick_use)
else:
    # ไม่พอต่อไม่ได้
    print(-1)
