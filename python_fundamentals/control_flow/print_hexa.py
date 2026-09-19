#!/usr/bin/env python3

text = ""
for i in range(100):
    text += "{} = {}\n".format(i, hex(i))
print(text, end="")
