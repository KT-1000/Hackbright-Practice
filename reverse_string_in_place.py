def rev_string(s):
    """ Reverse a string s in place without using any builtins, like reverse()"""
    new_string = ""
    for i in range(len(s), 0, -1):
        new_string += s[i - 1]

    return new_string

print rev_string("porcupine")
