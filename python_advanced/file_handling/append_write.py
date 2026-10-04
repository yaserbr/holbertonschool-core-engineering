#!/usr/bin/env python3
"""function that Append text in last line of file"""


def append_write(filename="", text=""):
    """Append text in last line of file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
