"""Units"""
lenght, wanted_unit, current_unit = float(input()), input(), input()
if current_unit == "KUEP":
    lenght = lenght * 12
elif current_unit == "SOK":
    lenght = (lenght * 12) * 2
elif current_unit == "WA":
    lenght = ((lenght * 12) * 2) * 4
elif current_unit == "SEN":
    lenght = (((lenght * 12) * 2) * 4) * 20

result = 0
if wanted_unit == "NIU":
    result = lenght
elif wanted_unit == "KUEP":
    result = lenght / 12
elif wanted_unit == "SOK":
    result = (lenght / 12) / 2
elif wanted_unit == "WA":
    result = ((lenght / 12) / 2) / 4
elif wanted_unit == "SEN":
    result = (((lenght / 12) / 2) / 4) / 20
print(f"{result:.4f}")
