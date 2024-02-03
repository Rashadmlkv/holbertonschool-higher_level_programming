#!/usr/bin/python3
"""
    Square class
"""


class Square:
    """
    Square class

    Atributes:
    size: private instance attribute
    """

    def __init__(self, size=0):
        try:
            if float(size):
                raise TypeError
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")

    pass
