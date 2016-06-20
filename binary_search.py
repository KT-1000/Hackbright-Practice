def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.
    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
    """

    assert 0 < val < 101, "Val must be between 1-100"
    min_val = 1
    max_val = 100
    num_guesses = 0
    # assign the current val to the input so we don't have to change initial input val
    cur_val = val

    if cur_val > (max_val/2):
        min_val = max_val/2
        cur_val = (max_val - min_val)/2
        num_guesses += 1

    elif cur_val < (max_val/2):
        max_val = max_val/2
        cur_val = (max_val - min_val)/2
        num_guesses += 1

    elif cur_val == max_val/2:
        num_guesses += 1

    else:
        num_guesses += 1

    return num_guesses

print binary_search(50)