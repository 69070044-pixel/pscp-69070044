"""[LEARNING LOGS] BrickBridge"""
small_brick = int(input())
big_brick = int(input())
goal = int(input())

big_use = goal // 5 # หาจำนวนก้อนให้ที่มาที่สุดที่ต้องใช้
if big_use <= big_brick:
    # จำนวนที่ต้องการก้อนใหญ่ที่ใช้มีพอ
    small_use = goal - (big_use * 5) # เอาก้อนใหญ่แค่ที่ใช้ไป * 5 เพื่อหาระยะที่ต่อได้
else:
    # ก้อนใหญ่ใช้หมดแล้วไม่พอต้องต่อก้อนเล็กเพิ่ม
    small_use = goal - (big_brick * 5) # เอาก้อนใหญ่ทั้งหมดใช้ไป * 5 เพื่อหาระยะที่ต่อได้

#  check ว่าก่อนเล็กมีพอมั้ย ถ้าไม่พอ print -1
print(small_use if small_brick >= small_use else -1)
