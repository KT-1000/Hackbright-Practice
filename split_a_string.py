def split(astring, splitter):
    """Split astring by splitter and return list of splits.
    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']
    """
    out = []
    index = 0

    while index <= len(astring):

        curr_index = index
        index = astring.find(splitter, index)

        if index != -1:
            out.append(astring[curr_index:index])
            index += len(splitter)

        else:
            # couldn't find any more instances of splitter in astring
            out.append(astring[curr_index:])
            break

    return out
