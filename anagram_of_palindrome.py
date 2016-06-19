def anagram_of_palindrome(word):
    """ Takes in a string, which is a palindrome.
        Returns True if the string is an anagram of a palindrome.
        Returns False if the string is not an anagram of a palindrome.
    """
    is_odd = (len(word) % 2 != 0)
    letters = {}
    for letter in word:
        letters[letter] = letters.get(letter, 1) + 1
    if is_odd == False:
        for letter in letters:
            if letters[letter] % 2 != 0:
                return False
            return True
    else:
        for letter in letters:
            if letters[letter] % 2 != 0:
                letters.pop(letter)
                for letter in letters:
                    if letters[letter] % 2 != 0:
                        return False
                    else:
                        return True

print anagram_of_palindrome("glad")