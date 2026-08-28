"""Teaching schedule"""
teaching_class, time = int(input()), int(input())
if not teaching_class or not time:
    print("No teaching")
else:
    all_m = teaching_class * time
    h = all_m // 60
    m = all_m - (h * 60)
    if h:
        print(f"{h} hours", end=" ")
    if m:
        print(f"{m} minute")
