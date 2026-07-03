"""OJ3015"""
come = int(input())
pay = int(input())
price_per_person = int(input())
members = int(input())

if members >= come:
    pro_time = members // come
    must_pay = (pro_time * pay) + (members % come)
    total = must_pay * price_per_person
    print(total)
else:
    print(members  * price_per_person)
