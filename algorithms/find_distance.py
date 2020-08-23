"""
Calculate the distance from one point to another.
"""

from math import sqrt


def find_distance(start_point, end_point, round_output=False):
    """
    Calculate the distance using Pythagoras.

    Example:

    start, end = [2, 5], [5, 10]
    print(find_distance(start, end))

    """
    cathete_a = abs(end_point[0] - start_point[0])
    cathete_b = abs(end_point[1] - start_point[1])

    hypotenuse = sqrt((cathete_a) ** 2 + (cathete_b) ** 2)

    return hypotenuse if not round_output else round(hypotenuse, 3)


start, end = [0, 0], [5, 5]
print(find_distance(start, end, True))
