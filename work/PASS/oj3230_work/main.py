"""โรงแรมกลางกรุง ไม่มีชั้น 13"""
def is_palindrome(x):
    """IF input is palindrome return True"""
    return x == x[::-1]

secret_number, room_number = input(), []
# หลักที่ 1
first_condition = ["9", "10", "11", "12", "14"]
for index in range(5):
    if int(secret_number[index]) > 5:
        room_number.append(first_condition[index])
        break
else:
    room_number.append("13")

# หลักที่ 2
if is_palindrome(secret_number):
    if int(secret_number[0]) + int(secret_number[4]) > 5:
        room_number.append("1")
    elif int(secret_number[1]) + int(secret_number[2]) > 5:
        room_number.append("2")
    else:
        room_number.append("0")
else:
    if int(secret_number[4]) and int(secret_number[0]) // int(secret_number[4]) > 5:
        room_number.append("1")
    elif int(secret_number[1]) - int(secret_number[2]) > 5:
        room_number.append("2")
    else:
        room_number.append("0")

# prepare for หลักที่ 3
secret_number_integer = [int(x) for x in secret_number]
sum_of_total, sum_of_multi = sum(secret_number_integer), 1
for num in secret_number_integer:
    sum_of_multi *= num

# หลักที่ 3
if sum_of_total > 25:
    room_number.append("1")
elif sum_of_multi > 55:
    room_number.append("2")
else:
    room_number.append("0")

print("".join(room_number))
