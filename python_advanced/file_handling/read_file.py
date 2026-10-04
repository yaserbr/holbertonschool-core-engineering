#!/usr/bin/env python3
"""function that prints text file content"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
