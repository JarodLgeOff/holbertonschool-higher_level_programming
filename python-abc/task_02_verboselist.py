#!/usr/bin/python3
"""Task 2: Verbose List"""


class VerboseList(list):
    """A list that prints a message when an item is added or removed."""

    def append(self, item):
        """Add an item to the end of the list and print a message."""
        super().append(item)
        print(f"Added {item} to the list.")

    def remove(self, item):
        """Remove an item from the list and print a message."""
        super().remove(item)
        print(f"Removed {item} from the list.")

    def extend(self, iterable):
        """Extend the list appending elements iterable and print a message."""
        super().extend(iterable)
        print(f"Extended the list with {iterable}.")

    def pop(self, index=-1):
        """Remove and return item at index (default last) and print message."""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
