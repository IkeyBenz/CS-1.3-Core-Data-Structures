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

    def set(self, item: object) -> None:
        """Overrides the HashTable set() method to ensure no duplicate keys."""
        if item in self:
            raise ValueError(f"{item} is already in this set.")

        super().set(item, None)
