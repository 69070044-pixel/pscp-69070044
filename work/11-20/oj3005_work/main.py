"""OJ3005"""
quantity = [int(x) for x in input().split()]
# จำนวนหัวแครอท จำนวนกะหล่ำปลี และ จำนวนมะเขือเทศที่กระต่ายน้อยซื้อ
price = [10, 25, 3] # ราคาของตามลำดับ
total = 0
for i, q in enumerate(quantity):
    # enumerate เพื่อเอาค่า index and value ใน List
    total += (q * price[i]) # จำวนที่ต้องการ * ราคาต่อชิ้น
print(total)
