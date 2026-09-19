#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        number = -number
    temp = str(number)
    last_digit = int(temp[-1])
    print(last_digit, end="")
    return last_digit
