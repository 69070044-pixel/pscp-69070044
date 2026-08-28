"""PM2.5"""
n = int(input())
over, peak, streak, start = 0, 0, 0, 0
max_streak, start_day = -1, 0
for i in range(n):
    pm_value = int(input())
    if pm_value > 50:
        over += 1
        if not streak:
            start = i + 1
        streak += 1
    else:
        if streak >= max_streak:
            max_streak = streak
            start_day = start
        streak = 0

    if pm_value > peak:
        peak = pm_value
if streak >= max_streak:
    max_streak = streak
    start_day = start

print("OVER =", over)
print("PEAK =", peak)
print("STREAK =", max_streak)
print("START =", start_day)
