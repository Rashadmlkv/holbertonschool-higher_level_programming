#!/usr/bin/python3
"""
    Class Square
"""
BaseGeometry = __import__('9-rectangle').BaseGeometry


class Square(BaseGeometry):
    """ Square class """

    def __init__(self, size):
        BaseGeometry.integer_validator(self, "size", size)

        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"

