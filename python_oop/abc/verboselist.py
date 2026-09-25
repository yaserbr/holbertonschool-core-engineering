#!/usr/bin/env python3
"""Module that demonstrates mixins with a Dragon class."""

class VerboseList(list):
    """New class"""

    def append(self, object):
        """Override"""
        super().append(object)
        print("Added [{}] to the list.".format(object))

    def extend(self, iterable):
        """Override"""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, value):
        """remove"""
        print("Removed [{}] from the list.".format(value))
        return super().remove(value)

    def pop(self, index = -1):
        """pop"""
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)