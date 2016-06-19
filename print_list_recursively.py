def print_recursively(lst):
    """ Print items in the list using recursion.
    >>> print_recursively([1, 2, 3])
    1
    2
    3

    >>> print_recursively([])

    """
    # base case: return nothing
    if not lst:
        return

    print lst[0]
    print_recursively(lst[1::])
