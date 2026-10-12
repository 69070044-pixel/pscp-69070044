"""Kangaroo"""
l, c, r = int(input()), int(input()), int(input())
print(max(c - l, r - c) - 1)
