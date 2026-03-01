#!/usr/bin/python3
"""Module that defines Shape abstract class and its subclasses"""


class VerboseList(list):
    """A list that prints a message when an item is added"""

    def append(self, item):
        """Override the append method to print a message"""
        super().append(item)
        print(f"Added [{item}] to the list.")


    def extend(self, x):
        """Override the extend method to print a message"""
        super().extend(x)
        print(f"Extended the list with [{len(x)}] items.")


    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        return super().remove(item)
    
           
    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
