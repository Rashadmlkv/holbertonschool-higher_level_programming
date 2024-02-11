#!/usr/bin/python3
"""
    file write
"""


def write_file(filename="", text=""):
    """ returns bytes """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
