"""OJ3070"""
n = 3
numbers = []
even, odd = 0, 0

while n:
    # input loop
    numbers.append(int(input()))
    n -= 1

for i in numbers:
    if i % 2:
        odd += 1
    else:
        even += 1

print(even)
print(odd)
