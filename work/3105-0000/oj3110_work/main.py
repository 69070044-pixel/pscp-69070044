"""[LEARNING LOGS] สงคราม...ส่งด่วน"""
rate = {
    "BKKCNX":[10, 30],
    "CNXUBP":[15, 40],
    "UBPBKK":[20, 40],
    "BKKPKT":[25, 50],
    "PKTCNX":[30, 60],
    "UBPPKT":[40, 70]
}

way = input().replace(" ", "")
weight = float(input())
try:
    fee, perweight = rate[way]
    fee += perweight * weight
    print(f"{fee:.2f}")
except KeyError:
    print("Error")
