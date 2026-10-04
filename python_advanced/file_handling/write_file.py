#!/usr/bin/env python3
"""function that writes text in a file"""


def write_file(filename="", text=""):
    """function started"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return text
