"""[LEARNING LOGS] ของขวัญและขโมย"""
n, k, t = [int(x) for x in input().split()]
numbers, looked, local_num = list(range(1, n + 1)), {1}, 1
while t != 1:
    index = (local_num + k - 1) % len(numbers)
    local_num = numbers[index]
    looked.add(local_num)

    if local_num in (1, t):
        break
print(len(looked))
