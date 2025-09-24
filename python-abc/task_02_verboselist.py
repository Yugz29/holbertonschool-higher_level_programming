#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        """
        Add item and print a message
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, numb):
        """
        Extend the list and print a message
        """
        super().extend(numb)
        print(f"Extended the list with [{len(numb)}] items.")

    def remove(self, item):
        """
        Print a message and delete an item
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        super().pop(index)
