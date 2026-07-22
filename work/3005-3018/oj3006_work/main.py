"""OJ3006"""
avr_boxes = float(input()) # average weight of two gift boxes
box = float(input()) #  weight of the gift box
# avr = (box1 + box2) / 2 -> box1 = (avr * 2) - box2
result = (avr_boxes * 2) - box
print(result)
