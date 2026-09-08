"""PickThemAgain"""
def add_to_list_condition(x):
    """
    use for filter input before add to list
    return true if x หาร 3 or 5 ลงตัว
    """
    return not int(x) % 3 or not int(x) % 5

num = [int(x) for x in input().split() if add_to_list_condition(x)]
if num:
    print(*num[::-1], sep='\n')
else:
    print("Nope")
