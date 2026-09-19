#!/usr/bin/env python3

number = __import__('random').randint(-10, 10)

if number < 0:
    print(str(number) + " is negative")
elif number > 0:
    print(str(number) + " is positive")
else:
    print(str(number) + " is zero")
