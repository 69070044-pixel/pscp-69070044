"""Array HaHea"""
array = []
for i in range(3):
    array.append(int(input()))
    print(f"Input number {i + 1} stored.")

while True:
    action = int(input())
    match action:
        case 1:
            print("Original order:", *array)
        case 2:
            print("Descending order:", *sorted(array, reverse=True))
        case 3:
            print("Ascending order:", *sorted(array))
        case _:
            break
