# GEOMETRY BASICS: DISTANCE BETWEEN TWO POINTS IN 2D (8 KYU)
#
# This series of katas will introduce you to basics of doing geometry with computers.
# Point objects have x and y attributes (X and Y in C#) attributes.
# Write a function calculating distance between Point a and Point b.
# Tests round answers to 6 decimal places.

from math import sqrt

def distance_between_points(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
