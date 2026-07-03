"""OJ3017 [LEARNING LOGS]"""
bill = int(input())
service = bill * 0.1
if service < 50:
    service = 50
elif service > 1000:
    service = 1000
vat = (bill + service) * 0.07
total = bill + service + vat
print(f"{total:.2f}")
