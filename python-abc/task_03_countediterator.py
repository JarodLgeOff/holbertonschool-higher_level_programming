#!/usr/bin.python3
"""Task 03. CountedIterator"""


class CountedIterator:
    """An iterator that counts the number of iterations"""
    def __init__(self, iterable):
        """Initializes the CountedIterator with the given iterable"""
        self.iterable = iterable
        self.count = 0

    def __iter__(self):
        """Returns the iterator object itself"""
        return self

    def __next__(self):
        """
        Returns the next item from the iterable and increments the count.
        Raises StopIteration when the end of the iterable is reached.
        """
        if self.count >= len(self.iterable):
            raise StopIteration
        value = self.iterable[self.count]
        self.count += 1
        return value

    def get_count(self):
        """Returns the number of iterations performed"""
        return self.count
