#!/usr/bin/python3
"""
    file write
"""


def append_write(filename="", text=""):
    """ returns bytes """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
