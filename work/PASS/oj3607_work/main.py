"""RuleofThree"""
n = int(input())
items, mx_p = [], 0
for _ in range(n):
    p, w = float(input()), float(input())
    mx_p = max(mx_p, p)
    items.append([p, w])

best = sorted(items, key=lambda x: (x[1] * (mx_p/x[0]), -x[0]), reverse=True)[0]
print(f"{best[0]:.2f} {best[1]:.2f}")
