from sets import Set
import unittest


class SetsTest(unittest.TestCase):

    def test_init(self):
        mySet = Set()

        assert len(mySet) == 0
        assert mySet.size == 0

    def test_init_with_list(self):
        mySet = Set(["hello", "there", "my", "name", "is", "ikey"])

        assert len(mySet) == 6
        assert mySet.size == 6

    def test_add(self):
        mySet = Set()

        mySet.set("yooo")
        assert len(mySet) == 1

        with self.assertRaises(ValueError):
            mySet.set("yooo")

    def test_delete(self):
        mySet = Set(["hello", "there"])

        assert len(mySet) == 2

        mySet.delete("hello")

        assert len(mySet) == 1
