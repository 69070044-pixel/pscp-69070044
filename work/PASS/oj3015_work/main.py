"""OJ3015"""
come = int(input())
pay_person = int(input()) # มา come คนจ่าย pay_person คน
price_per_person = int(input()) # ราคาต่อหัว
customer = int(input()) # ลูกค้าที่มา

# ได้กี่โต๊ะ (โต๊ะละ come คน)
table = customer // come
remainning = customer % come #คนที่เหลือที่ต้องจ่ายเพราะคนไม่ครบโปร

paid = table * (pay_person * price_per_person) + remainning * price_per_person
print(paid)
