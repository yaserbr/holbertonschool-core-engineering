#!/usr/bin/env python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            raise IndexError("list index out of range")
        except TypeError:
            raise TypeError("my_list must be a list")
    print()
    return count
