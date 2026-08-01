"""Taxi_Price"""
dist = int(input())
fare = 0
if 0 < dist <= 1:
    fare = 35
elif 1 < dist <= 10:
    fare = 35 + (dist - 1) * 5
elif dist > 10:
    fare = 35 + (9 * 5) + (dist - 10) * 8

print(fare)
