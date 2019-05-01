import unittest
from sets import Set


class RedactTest(unittest.TestCase):

    def test_ssome_banned_words(self):
        words = ["are", "these", "words", "going", "to", "go", "through"]
        banned = ["these", "are", "the", "invalid", "words"]

        assert redact_words(words, banned) == ["going", "to", "go", "through"]

    def test_all_band_words(self):
        words = ["bad", "word"]
        banned = ["bad", "word"]

        assert redact_words(words, banned) == []

    def test_no_banned_words(self):
        words = ["hello", "world"]
        banned = ["bad", "word"]

        assert redact_words(words, banned) == words


def redact_words(sentence: list, prohibited: list) -> list:

    prohibited = set(word.lower() for word in prohibited)

    return list(filter(lambda word: word.lower() not in prohibited, sentence))
