"""Resistor"""
resistor = {
    "black": ["0", "0", 1, None],
    "brown": ["1", "1", 10, 1],
    "red": ["2", "2", 100, 2],
    "orange": ["3", "3", 1000, None],
    "yellow": ["4", "4", 10000, None],
    "green": ["5", "5", 100000, 0.5],
    "blue": ["6", "6", 1000000, 0.25],
    "purple": ["7", "7", 10000000, 0.10],
    "grey": ["8", "8", None, 0.05],
    "white": ["9", "9", None, None],
    "gold": [None, None, 0.1, 5],
    "silver": [None, None, 0.01, 10]
}
try:
    band1 = resistor[input().lower()][0]
    band2 = resistor[input().lower()][1]
    mul = resistor[input().lower()][2]
    tol = resistor[input().lower()][3]
    result = float(band1 + band2) * float(mul)
    percent = result * (tol/100)
    print(f"{result - percent:.4f}")
    print(f"{result + percent:.4f}")
except (KeyError, TypeError):
    print("Error")
