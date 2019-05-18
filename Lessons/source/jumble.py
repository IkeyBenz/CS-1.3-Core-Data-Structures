from itertools import permutations
from sets import Set
import sys

words = set(open('/usr/share/dict/words', 'r').read().split('\n'))


def get_proper_word(scrabled_chars: str) -> str:
    perms = set(permutations(scrabled_chars))
    return perms & words


if __name__ == '__main__':
    scramble = sys.argv[1]
    print(scramble)
    # print(get_proper_word(scramble))

# get_proper_word(list("tefon"))
