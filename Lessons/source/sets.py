from hashtable import HashTable


class Set(HashTable):
    def __init__(self, iterable=None):
        """Initializes new set object"""

        super().__init__()

        if iterable is not None:
            for elem in iterable:
                self.set(elem)

    def __str__(self):
        """Return a formatted string representation of this set."""
        return '{' + ', '.join(self.keys()) + '}'

    def __repr__(self):
        """Return a string representation of this set."""
        return f"Set({self})"

    def __iter__(self):
        for key, _ in self.items():
            yield key

    def __or__(self, other):
        """Returns the Union of two sets"""
        union = Set()
        for item in self:
            union.set(item)
        for item in other:
            union.set(item)

        return union

    def __and__(self, other):
        """Returns the Intersection of two sets"""
        intersection = Set()
        for item in self:
            if item in other:
                intersection.set(item)

        return intersection

    def __sub__(self, other):
        """Returns the difference between two sets."""
        difference = Set()
        for item in self:
            if item not in other:
                difference.set(item)

        return difference

    def __add__(self, other):
        return self | other

    def set(self, item: object) -> None:
        """Overrides the HashTable set() method, setting value to None."""

        super().set(item, None)
