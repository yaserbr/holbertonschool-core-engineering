#!/usr/bin/env python3
def pow(a, b):
    result = 1
    exponent = b if b >= 0 else -b
    for i in range(exponent):
        result = result * a
    if b < 0:
        result = 1 / result
    return result
