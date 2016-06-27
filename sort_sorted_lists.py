def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both without using sorted() or sort().
    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
    """
    i = 0
    j = 0
    sorted_list = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    sorted_list.extend(b[j:])
    sorted_list.extend(a[i:])

    return sorted_list
