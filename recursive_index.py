def recursive_index(needle, haystack, index=0):
    """ Given a list, haystack, return index of needle in list.
    Return None if needle is not in haystack.
    DO NOT use a for or while loop!

    >>> recursive_index('kitten', ["mitten", "kitten", "smitten"])
    1

    >>> recursive_index('kitten', ["bobcat", "cool cat", "tiger"])

    """
    if needle not in haystack:
        return

    elif haystack[index] == needle:
        return index

    else:
        1 + recursive_index(needle, haystack[index])
