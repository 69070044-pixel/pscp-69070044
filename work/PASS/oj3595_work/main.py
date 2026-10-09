"""Meteorite"""
a, b, c = float(input()), float(input()), float(input())

def meteorite_split(w, n, split_b, safe_w, count):
    """calculate function"""
    if w < safe_w:
        return count
    new_w = w / split_b
    return meteorite_split(new_w, n * split_b, split_b, safe_w, count + n)

print(int(meteorite_split(a, 1, b, c, 0)))
