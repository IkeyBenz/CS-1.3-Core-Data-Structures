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

    def test_init_with_list_duplicates(self):
        mySet = Set(
            "hello there my name is ikey hello there my name is ikey".split())

        assert len(mySet) == 6
        assert mySet.size == 6

    def test_add(self):
        mySet = Set()

        mySet.set("yooo")
        assert len(mySet) == 1

    def test_delete(self):
        mySet = Set(["hello", "there"])

        assert len(mySet) == 2

        mySet.delete("hello")

        assert len(mySet) == 1

    def test_union(self):
        mySet = Set(["hello", "there", "ikey"])
        otherSet = Set(["other", "my", "hello", "there"])

        union = mySet | otherSet

        assert len(union) == 5
        for word in ["hello", "there", "ikey", "other", "my"]:
            assert word in union

    def test_intersection(self):
        mySet = Set(["hello", "there", "ikey"])
        otherSet = Set(["other", "my", "hello", "there"])

        intersection = mySet & otherSet

        assert len(intersection) == 2
        assert "hello" in intersection
        assert "there" in intersection

    def test_difference(self):
        mySet = Set(["hello", "there", "ikey"])
        otherSet = Set(["other", "my", "hello", "there"])

        difference = mySet - otherSet
        assert len(difference) == 1
        assert "ikey" in difference

        reverse_difference = otherSet - mySet
        assert len(reverse_difference) == 2
        assert "my" in reverse_difference
        assert "other" in reverse_difference

    # No test for add becasue its the same as union...
