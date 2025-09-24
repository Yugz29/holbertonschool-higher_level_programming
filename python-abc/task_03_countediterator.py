#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        """
        Initialize an iterable obj and a counter
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Increment the counter and return the next element
        """
        self.count += 1
        return next(self.iterator)

    def get_count(self):
        """
        Return the number of element iterated
        """
        return self.count
