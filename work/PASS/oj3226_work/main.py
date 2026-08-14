"""[Recommend] Inflation"""
total, years = int(float(input()) * 100), int(input()) # แปลงหน่วยเป็น satang
while years:
    total = (total * 10381) // 10000  # คูณเงินเฟ้อ + ตัดเศษ
    years -= 1
baht = total // 100
satang = total % 100
print(f"{baht}.{satang:02d}")
