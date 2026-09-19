#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        number = -number
    temp = str(number)
    return int(temp[-1])
