"""thaiplus"""
name, age, salary, = input(), int(input()), int(input())
g_card = input() == "Y"
family_member = int(input())
rank, cost = "", 0
if age >= 18:
    if g_card or salary <= 15000:
        rank, cost = "GOLD", 3000
    elif salary <= 30000:
        rank, cost = "SILVER", 1500
    else:
        rank, cost = "NOT", "ELIGIBLE"

    if family_member >= 3 and rank != "NOT":
        cost += 500
else:
    rank, cost = "NOT", "ELIGIBLE"
print(name, rank, cost)
