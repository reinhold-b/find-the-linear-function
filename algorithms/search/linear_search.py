"""
Python linear search algorithm
"""


def linear_search(search_array, search_key):
    """
    Iterate through the whole array until the search_key is found.
    If not found return -1.
    """
    for index, element in enumerate(search_array):
        if element == search_key:
            return index
    return -1
