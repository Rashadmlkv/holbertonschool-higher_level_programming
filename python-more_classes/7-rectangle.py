#!/usr/bin/python3
"""
    salam
"""


class Rectangle:
    """
        necesen
    """

    array = ""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        self.array = ""
        if (self.width == 0 or self.height == 0):
            return self.array
        for i in range(self.height):
            self.array += (f"{self.print_symbol}" * self.width)
            if i != self.height - 1:
                self.array += "\n"
        return self.array

    def __repr__(self):
        return (f"{self.__class__.__name__}{self.width, self.height}")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
