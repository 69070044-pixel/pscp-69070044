"""FizzBuzz"""
n = int(input())
for i in range(1, n + 1):
    three, five = i % 3, i % 5
    if not three and not five:
        print("FizzBuzz")
    elif not three:
        print("Fizz")
    elif not five:
        print("Buzz")
    else:
        print(i)
