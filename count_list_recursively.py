def count_recursively(lst):
    """ Return number of items in a list, using recursion.
    >>> count_recursively([])
    0

    >>> count_recursively([1, 2, 3])
    3
    """
    # base case: empty list
    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])
