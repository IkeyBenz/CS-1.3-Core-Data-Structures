#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def remove_non_letters(text):
    stripped = ""
    for c in text:
        if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
            stripped += c
    return stripped


def is_palindrome_iterative(text):

    left, right = 0, len(text)-1

    while left < right:

        # Account for non-letters:
        if not text[left].isalpha():
            left += 1
            continue  # End this itteration here
        if not text[right].isalpha():
            right -= 1
            continue

        # If mirrored text doesn't match, not palindrome
        if text[left].lower() != text[right].lower():
            return False

        left += 1
        right -= 1

    return True


def is_palindrome_recursive(text, left=0, right=None):

    if not right:
        right = len(text)-1

    if left < right:

        # Account for non-letters
        if not text[left].isalpha():
            return is_palindrome_recursive(text, left+1, right)
        if not text[right].isalpha():
            return is_palindrome_recursive(text, left, right-1)

        # If mirrored letters don't match, not palindrome
        if text[left].lower() != text[right].lower():
            return False

        return is_palindrome_recursive(text, left+1, right-1)

    return True


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    print(is_palindrome_iterative('rac- ,ecar'))
