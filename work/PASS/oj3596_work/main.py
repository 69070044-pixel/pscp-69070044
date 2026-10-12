"""Ramen Bowl"""
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

def loadinglines(data_list):
    """Sort Bowl"""
    item_result = []
    while data_list:
        get_bowl = set(data_list)
        for i in get_bowl:
            data_list.remove(i)
        item_result.append(get_bowl)
    return item_result

print(len(loadinglines(data)))
