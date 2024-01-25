#!/usr/bin/python3
"""prints the ASCII, in reverse order, alternating lowercase and uppercase"""
for i in reversed(range(97, 123)):
    if (i % 2 != 0):
        i = i - 32
    print("{}".format(chr(i)), end='')
