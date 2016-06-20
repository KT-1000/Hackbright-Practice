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
    min_val = 0
    max_val = 101
    assert min_val < val < max_val, "Val must be between 1-100"
    num_guesses = 0
    # assign the current val to the input so we don't have to change initial input val
    guess = None

    while guess != val:
        num_guesses += 1
        guess = (max_val - min_val) / 2 + min_val

        if val > guess:
            min_val = guess

        elif val < guess:
            max_val = guess

    return num_guesses