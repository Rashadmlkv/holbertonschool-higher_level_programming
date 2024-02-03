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
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end='')
                print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        except TypeError:
            raise TypeError("size must be an integer")

    pass
