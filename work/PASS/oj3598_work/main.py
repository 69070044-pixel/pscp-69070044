"""สถิติคลื่นความร้อน"""
n = int(input())
data = [float(x) for x in input().split()]
data.sort()

def median(num_list, l):
    """median calculate"""
    pos = int((n + 1) / 2)
    if l % 2:
        return num_list[pos - 1]
    return (num_list[pos - 1] + num_list[pos]) / 2

alert = 0
for d in data:
    if d >= 37.00:
        alert += 1

sorted_data = list(format(x, '.2f') for x in data)

print(f"SUM={sum(data):.2f}")
print(f"AVG={(sum(data) / len(data)):.2f}")
print(f"MEDIAN={median(data, n):.2f}")
print(f"MAX={max(data):.2f}")
print(f"MIN={min(data):.2f}")
print(f"ALERT={alert}")
print("SORTED=", end="")
print(*sorted_data)
