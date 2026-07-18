"""OJ3018"""
rectangle_a = [int(x) for x in input().split()]
rectangle_b = [int(x) for x in input().split()]

x1, y1, width1, heigth1 = rectangle_a
x2, y2, width2, heigth2 = rectangle_b

ovl_left = max(x1, x2)
ovl_right = min(x1 + width1, x2 + width2)
ovl_top = max(y1, y2)
ovl_bottom = min(y1 + heigth1, y2 + heigth2)

ovl_width = max(0, ovl_right - ovl_left)
ovl_heigth = max(0, ovl_bottom - ovl_top)

ovl_area = ovl_heigth * ovl_width
if ovl_width:
    print(ovl_area)
else:
    print("no overlapping")
