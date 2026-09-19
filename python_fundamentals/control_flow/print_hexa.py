#!/usr/bin/env python3

text = ""
for i in range(99):
    text = text + "" + str(i) + " = " + str(hex(i)) + "\n"
print(text, end="")
