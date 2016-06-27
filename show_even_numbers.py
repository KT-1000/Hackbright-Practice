def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.
    show_evens([1, 2, 3, 4, 6, 8])
    [1, 3, 4, 5]
    """
    indices = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            indices.append(i)
    return indices