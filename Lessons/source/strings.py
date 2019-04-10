#!python


def contains(text, pattern):
    """Returns a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) == 0:
        return True
    if len(pattern) > len(text):
        return False

    for i in range(len(text) - len(pattern)+1):

        if text[i] == pattern[0]:
            if text[i: i+len(pattern)] == pattern:
                return True

    return False  # return pattern in text :/


# "abcdef" "efg"

def find_index(text, pattern):
    """Returns the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) == 0:
        return 0
    if len(pattern) > len(text):
        return None

    for i in range(len(text) - len(pattern)+1):
        if text[i] == pattern[0]:
            if text[i: i+len(pattern)] == pattern:
                return i

    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) == 0:
        return [index for index in range(len(text))]
    if len(pattern) > len(text):
        return [0]

    indices = []

    for i in range(len(text) - len(pattern)+1):
        if text[i] == pattern[0]:
            if text[i: i+len(pattern)] == pattern:
                indices.append(i)

    return indices


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    print(contains("abcdef", "efg"))
